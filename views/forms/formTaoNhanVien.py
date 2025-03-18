import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.messagebox as messagebox
from controllers.nhanVienController import NhanVienController  # Change to NhanVienController

class FormTaoNhanVien(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.controller = NhanVienController()
        self.title("Thêm nhân viên mới")
        self.configure(bg="white")
        self.geometry("800x400")
        self.create_form()

    def create_form(self):
        style = ttk.Style()
        style.configure("TEntry", padding=(10, 5))
        style.configure("Accent.TButton", font=("Arial", 12), padding=(10, 5))
        style.configure("Cancel.TButton", font=("Arial", 12), padding=(10, 5))

        style.configure("Accent.TButton", background="#38b6ff", foreground="black")
        style.configure("Cancel.TButton", background="#ff4d4d", foreground="black")

        form_frame = tk.Frame(self, bg="white", padx=20, pady=20)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        title_label = tk.Label(form_frame, text="Thêm nhân viên mới", font=("Arial", 16, "bold"), bg="white")
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 20), sticky="w")

        tk.Label(form_frame, text="Mã nhân viên", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)
        self.employee_id_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.employee_id_entry.grid(row=1, column=1, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Họ và tên", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)
        self.name_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.name_entry.grid(row=2, column=1, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Email", font=("Arial", 12), bg="white").grid(row=3, column=0, sticky="e", padx=(0, 10), pady=5)
        self.email_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.email_entry.grid(row=3, column=1, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Số điện thoại", font=("Arial", 12), bg="white").grid(row=4, column=0, sticky="e", padx=(0, 10), pady=5)
        self.phone_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.phone_entry.grid(row=4, column=1, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Chức vụ", font=("Arial", 12), bg="white").grid(row=1, column=2, sticky="e", padx=(20, 10), pady=5)
        self.position_combobox = ttk.Combobox(form_frame, font=("Arial", 12), width=20, state="readonly")
        self.position_combobox.grid(row=1, column=3, sticky="w", padx=0, pady=5)

        # Thêm các lựa chọn vào Listbox
        positions = ["Nhân viên", "Quản lý", "Giám đốc", "Kế toán"]
        self.position_combobox['values'] = positions
        self.position_combobox.set(positions[0])  # Đặt mục đầu tiên làm mặc định

        tk.Label(form_frame, text="Mức lương", font=("Arial", 12), bg="white").grid(row=2, column=2, sticky="e",
                                                                                  padx=(20, 10), pady=5)
        self.salary_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.salary_entry.grid(row=2, column=3, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Địa chỉ", font=("Arial", 12), bg="white").grid(row=3, column=2, sticky="e",
                                                                                    padx=(20, 10), pady=5)
        self.address_text = tk.Text(form_frame, font=("Arial", 12), width=20, height=4, wrap=tk.WORD)
        self.address_text.grid(row=3, column=3, sticky="w", padx=0, pady=5)

        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(fill=tk.X, padx=20, pady=10)

        button_frame = tk.Frame(self, bg="white")
        button_frame.pack(fill=tk.X, padx=20, pady=10)

        self.save_button = ttk.Button(button_frame, text="Lưu", style="Accent.TButton", command=self.save_data)
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.cancel_button = ttk.Button(button_frame, text="Hủy", style="Cancel.TButton", command=self.cancel)
        self.cancel_button.pack(side=tk.LEFT, padx=10)

    def validate_form(self):
        if not self.employee_id_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập mã nhân viên.")
            return False
        if not self.name_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập họ và tên.")
            return False
        if not self.email_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập email.")
            return False
        if not self.phone_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập số điện thoại.")
            return False
        if not self.address_text.get("1.0", tk.END).strip():
            messagebox.showerror("Lỗi", "Vui lòng nhập địa chỉ.")
            return False
        return True

    def save_data(self):
        if not self.validate_form():
            return

        employee_data = {
            "ma_nhan_vien": self.employee_id_entry.get(),
            "ho_ten": self.name_entry.get(),
            "email": self.email_entry.get(),
            "chuc_vu": self.position_combobox.get(),
            "dien_thoai": self.phone_entry.get(),
            "dia_chi" : self.address_text.get("1.0", tk.END).strip(),
            "luong": self.salary_entry.get(),
        }
        print("Data:", employee_data)
        isSuccess = self.controller.createEmployeeController(employee_data)  # Use createEmployeeController
        if isSuccess:
            messagebox.showinfo("Thông báo", "Tạo nhân viên thành công!")
            self.parent.reload_data()
            self.clear_form()
        else:
            messagebox.showerror("Lỗi", "Tạo nhân viên thất bại!")

    def cancel(self):
        self.clear_form()

    def clear_form(self):
        self.employee_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.position_combobox.delete(0, tk.END)

if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    app = FormTaoNhanVien(root)
    root.mainloop()
