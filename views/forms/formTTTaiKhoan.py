import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
from controllers.taiKhoanController import TaiKhoanController
class FormThongTinTaiKhoan(tk.Toplevel):
    def __init__(self, parent , maNV=None):
        super().__init__(parent)
        self.title("Thông tin tài khoản")
        self.geometry("600x800")
        self.configure(bg="white")
        self.maNV = maNV
        self.controller = TaiKhoanController()
        self.accountInfor = self.controller.getInforAccountController(self.maNV)
        print(self.accountInfor)
        # Tạo giao diện
        self.create_form()
        self.render_data()

    def create_form(self):
        """Tạo form nhập liệu"""
        form_frame = tk.Frame(self, bg="white")
        form_frame.pack(expand=True, padx=20, pady=10)

        # Tiêu đề
        tk.Label(form_frame, text="Sửa thông tin tài khoản", font=("Arial", 16, "bold"),
                 bg="white").pack(pady=(0, 20))

        # Tên đăng nhập
        tk.Label(form_frame, text="Tên đăng nhập *", font=("Arial",14,), bg="white").pack(anchor="w")
        self.accountName = tk.Entry(form_frame, font=("Arial", 12), width=50, state="readonly")
        self.accountName.pack(pady=5)

        # Họ và tên
        tk.Label(form_frame, text="Họ và tên *", font=("Arial", 14), bg="white").pack(anchor="w", pady=(20,0))
        self.nameStaff = tk.Entry(form_frame, font=("Arial", 12), width=50, state="readonly")
        self.nameStaff.pack(pady=5)

        # Email
        tk.Label(form_frame, text="Email *", font=("Arial", 14), bg="white").pack(anchor="w", pady=(20,0))
        self.email = tk.Entry(form_frame, font=("Arial", 12), width=50)
        self.email.pack(pady=5)

        # Số điện thoại
        tk.Label(form_frame, text="Số điện thoại *", font=("Arial", 14), bg="white").pack(anchor="w", pady=(20,0))
        self.phone = tk.Entry(form_frame, font=("Arial", 12), width=50, state="readonly")
        self.phone.pack(pady=5)

        # Phân quyền
        tk.Label(form_frame, text="Phân quyền", font=("Arial", 14), bg="white").pack(anchor="w", pady=(20,0))
        self.role = ttk.Combobox(form_frame, values=["nhanvien", "admin"], font=("Arial", 12),
                                 state="readonly", width=48)
        self.role.pack(pady=5)

        # Trạng thái tài khoản
        tk.Label(form_frame, text="Trạng thái tài khoản", font=("Arial", 14), bg="white").pack(anchor="w", pady=(20,0))
        self.statusAcc = ttk.Combobox(form_frame, values=["Active", "Blocked"], font=("Arial", 12),
                                      state="readonly", width=48)
        self.statusAcc.pack(pady=5)

        # Mật khẩu
        tk.Label(form_frame, text="Mật khẩu *", font=("Arial", 14), bg="white").pack(anchor="w", pady=(20,0))
        self.password = tk.Entry(form_frame, font=("Arial", 12), width=50, show="*")
        self.password.pack(pady=5)

        # Xác nhận mật khẩu
        tk.Label(form_frame, text="Xác nhận mật khẩu *", font=("Arial", 14), bg="white").pack(anchor="w", pady=(20,0))
        self.confirmPass = tk.Entry(form_frame, font=("Arial", 12), width=50, show="*")
        self.confirmPass.pack(pady=5)

        # Nút Lưu
        save_button = tk.Button(form_frame, text="Lưu", bg="#007BFF", fg="white",
                                font=("Arial", 14), width=10, command=self.update_data)
        save_button.pack(pady=20)

    def render_data(self):
        """Hiển thị dữ liệu từ self.accountInfor vào các Entry và Combobox"""
        if self.accountInfor:
            # Xóa nội dung hiện tại của các Entry
            self.accountName.delete(0, tk.END)
            self.nameStaff.delete(0, tk.END)
            self.email.delete(0, tk.END)
            self.phone.delete(0, tk.END)
            self.password.delete(0, tk.END)
            self.confirmPass.delete(0, tk.END)

            # Chèn dữ liệu từ self.accountInfor vào các Entry
            self.accountName.config(state="normal")
            self.accountName.insert(0, self.accountInfor[0])  # Tên đăng nhập
            self.accountName.config(state="readonly")

            self.nameStaff.config(state="normal")
            self.nameStaff.insert(0, self.accountInfor[5])  # Họ và tên
            self.nameStaff.config(state="readonly")

            self.email.insert(0, self.accountInfor[4])  # Email

            self.phone.config(state="normal")
            self.phone.insert(0, self.accountInfor[6])  # Số điện thoại
            self.phone.config(state="readonly")

            self.role.set(self.accountInfor[2])  # Phân quyền
            self.statusAcc.set(self.accountInfor[3])  # Trạng thái tài khoản
            self.password.insert(0, self.accountInfor[1])  # Mật khẩu

    def validate_data(self, data):
        # Kiểm tra các trường bắt buộc không được để trống
        if not data['ma_nguoi_dung']:
            return "Mã người dùng không được để trống"
        if not data['email']:
            return "Email không được để trống"
        if not data['mat_khau']:
            return "Mật khẩu không được để trống"
        if not data['confirm_password']:
            return "Xác nhận mật khẩu không được để trống"
        if not data['vai_tro']:
            return "Phân quyền không được để trống"
        if not data['trang_thai_tai_khoan']:
            return "Trạng thái tài khoản không được để trống"

        # Kiểm tra định dạng email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, data['email']):
            return "Email không hợp lệ"

        # Kiểm tra mật khẩu (tối thiểu 6 ký tự)
        if len(data['mat_khau']) < 6:
            return "Mật khẩu phải có ít nhất 6 ký tự"

        # Kiểm tra mật khẩu và xác nhận mật khẩu có khớp hay không
        if data['mat_khau'] != data['confirm_password']:
            return "Mật khẩu và xác nhận mật khẩu không khớp"

        # Nếu tất cả các điều kiện đều hợp lệ, trả về True
        return True

    def get_data(self):
        email_value = self.email.get()  # Email
        password_value = self.password.get()  # Mật khẩu
        confirmPass_value = self.confirmPass.get()  # Xác nhận mật khẩu
        role_value = self.role.get()  # Phân quyền (Combobox)
        statusAcc_value = self.statusAcc.get()  # Trạng thái tài khoản (Combobox)

        data = {
            "ma_nguoi_dung": self.accountInfor[7],
            "email": email_value,
            "mat_khau": password_value,
            "confirm_password": confirmPass_value,
            "vai_tro": role_value,
            "trang_thai_tai_khoan": statusAcc_value
        }
        validation_result = self.validate_data(data)
        if validation_result == True:
            print("check data >>>>> ", data)
        else:
           messagebox.showerror("Cảnh báo", validation_result)
        # Return or process the collected data if needed
        return data

    def update_data(self):
        data = self.get_data()
        isAccept = messagebox.askyesno("Thông báo!", "Xác nhận lưu thay đổi?")
        if isAccept:
            result = self.controller.updateAccountController(data)
            if result:
                messagebox.showinfo("Thông báo!", "Cập nhập thành công!")
            else:
                messagebox.showinfo("Thông báo!", "Cập nhập thất bại!")
    # Chạy ứng dụng
if __name__ == "__main__":
    app = FormThongTinTaiKhoan(None)
    app.mainloop()