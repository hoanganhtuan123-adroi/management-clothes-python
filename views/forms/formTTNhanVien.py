import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.messagebox as messagebox
from config.commonDef import CommonDef
from controllers.nhanVienController import NhanVienController


class FormTTNhanVien(tk.Toplevel):
    def __init__(self, parent, id=None):
        super().__init__(parent)
        self.parent = parent
        self.employee_id = id
        self.controller = NhanVienController()
        self.commondef = CommonDef()
        self.employee_data = self.controller.getAllEmployeesByIDController(self.employee_id)[0]
        print(self.employee_data)
        self.title("Xem thông tin nhân viên")
        self.configure(bg="white")
        self.geometry("800x400")
        self.create_form()
        self.render_data()

    def create_form(self):
        style = ttk.Style()
        style.configure("TEntry", padding=(10, 5))
        style.configure("Accent.TButton", font=("Arial", 12), padding=(10, 5))
        style.configure("Cancel.TButton", font=("Arial", 12), padding=(10, 5))

        style.configure("Accent.TButton", background="#38b6ff", foreground="black")
        style.configure("Cancel.TButton", background="#ff4d4d", foreground="black")

        form_frame = tk.Frame(self, bg="white", padx=20, pady=20)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        title_label = tk.Label(form_frame, text="Thông tin nhân viên", font=("Arial", 16, "bold"), bg="white")
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 20), sticky="w")

        tk.Label(form_frame, text="Họ và tên", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky="e",
                                                                                    padx=(0, 10), pady=5)
        self.name_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.name_entry.grid(row=1, column=1, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Email", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky="e",
                                                                                padx=(0, 10), pady=5)
        self.email_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.email_entry.grid(row=2, column=1, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Số điện thoại", font=("Arial", 12), bg="white").grid(row=3, column=0, sticky="e",
                                                                                        padx=(0, 10), pady=5)
        self.phone_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.phone_entry.grid(row=3, column=1, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Ngày vào làm", font=("Arial", 12), bg="white").grid(row=4, column=0, sticky="e",
                                                                                        padx=(0, 10), pady=5)
        self.date_work_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.date_work_entry.grid(row=4, column=1, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Chức vụ", font=("Arial", 12), bg="white").grid(row=1, column=2, sticky="e",
                                                                                  padx=(20, 10), pady=5)
        self.job_title_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.job_title_entry.grid(row=1, column=3, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Lương cơ bản", font=("Arial", 12), bg="white").grid(row=2, column=2, sticky="e",
                                                                                       padx=(20, 10), pady=5)
        self.salary_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20, state="readonly")
        self.salary_entry.grid(row=2, column=3, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Hệ số lương", font=("Arial", 12), bg="white").grid(row=3, column=2, sticky="e",
                                                                                      padx=(20, 10), pady=5)
        self.coefficient_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20, state="readonly")
        self.coefficient_entry.grid(row=3, column=3, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Địa chỉ", font=("Arial", 12), bg="white").grid(row=4, column=2, sticky="e",
                                                                                  padx=(20, 10), pady=5)
        self.address_text = tk.Text(form_frame, font=("Arial", 12), width=20, height=4, wrap=tk.WORD)
        self.address_text.grid(row=4, column=3, sticky="w", padx=0, pady=5)

        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(fill=tk.X, padx=20, pady=10)

        button_frame = tk.Frame(self, bg="white")
        button_frame.pack(fill=tk.X, padx=20, pady=10)
        self.save_button = ttk.Button(button_frame, text="Chỉnh sửa", style="Accent.TButton", command=self.save_data)
        self.save_button.pack(side=tk.LEFT, padx=10)
        self.cancel_button = ttk.Button(button_frame, text="Xóa", style="Cancel.TButton", command=self.handleDelete)
        self.cancel_button.pack(side=tk.LEFT, padx=10)

    def validate_form(self):
        if not self.name_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập họ và tên.")
            return False
        if not self.email_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập email.")
            return False
        if not self.phone_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập số điện thoại.")
            return False
        if not self.job_title_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập chức vụ.")
            return False
        return True

    def save_data(self):
        if not self.validate_form():
            return

        employee_data = {
            "ma_nhan_vien": self.employee_data['ma_nhan_vien'],
            "ho_ten": self.name_entry.get(),
            "email": self.email_entry.get(),
            "chuc_vu": self.job_title_entry.get(),
            "dien_thoai": self.phone_entry.get()
        }
        isSuccess = self.controller.updateEmployeeController(employee_data)
        if isSuccess:
            messagebox.showinfo("Thành công", "Sửa thông tin nhân viên thành công.")
            self.destroy()
        else:
            messagebox.showerror("Lỗi", "Sửa nhân viên thất bại.")

    def render_data(self):
        self.name_entry.insert(0, self.employee_data[2])
        self.phone_entry.insert(0, str(self.employee_data[4]))
        self.job_title_entry.insert(0, self.employee_data[7])
        self.email_entry.insert(0, self.employee_data[5])
        self.salary_entry.config(state="normal")
        self.salary_entry.insert(0, self.commondef.format_number(self.employee_data[6]))
        self.salary_entry.config(state="readonly")

        self.coefficient_entry.config(state="normal")
        self.coefficient_entry.insert(0, self.employee_data[9])
        self.coefficient_entry.config(state="readonly")

        self.address_text.insert("1.0", self.employee_data[3])
        self.date_work_entry.insert(0, self.employee_data[8])

    def cancel(self):
        self.clear_form()

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.job_title_entry.delete(0, tk.END)

    def handleDelete(self):
        isSuccess = self.controller.deleteEmployeeController(self.employee_data[0])
        if isSuccess:
            messagebox.showinfo("Thành công", "Xóa nhân viên thành công.")
            self.parent.reload_data()
            self.destroy()
        else:
            messagebox.showerror("Lỗi", "Xóa nhân viên thất bại.")


if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    app = FormTTNhanVien(root)
    root.mainloop()
