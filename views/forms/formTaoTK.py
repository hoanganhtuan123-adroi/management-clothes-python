import tkinter as tk
from tkinter import ttk

class CreateAccountApp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Tạo mới tài khoản")
        self.geometry("600x800")
        self.configure(bg="white")

        # Tạo giao diện
        self.create_form()

    def create_form(self):
        """Tạo form nhập liệu"""
        form_frame = tk.Frame(self, bg="white")
        form_frame.pack(expand=True, padx=20, pady=20)

        # Tiêu đề
        tk.Label(form_frame, text="Tạo mới tài khoản", font=("Arial", 16, "bold"),
                 bg="white").pack(pady=(0, 20))

        # Tên đăng nhập
        tk.Label(form_frame, text="Tên đăng nhập *", font=("Arial", 12), bg="white").pack(anchor="w")
        tk.Entry(form_frame, font=("Arial", 12), width=50).pack(pady=5)

        # Họ và tên
        tk.Label(form_frame, text="Họ và tên *", font=("Arial", 12), bg="white").pack(anchor="w")
        tk.Entry(form_frame, font=("Arial", 12), width=50).pack(pady=5)

        # Email
        tk.Label(form_frame, text="Email *", font=("Arial", 12), bg="white").pack(anchor="w")
        tk.Entry(form_frame, font=("Arial", 12), width=50).pack(pady=5)

        # Số điện thoại
        tk.Label(form_frame, text="Số điện thoại *", font=("Arial", 12), bg="white").pack(anchor="w")
        tk.Entry(form_frame, font=("Arial", 12), width=50).pack(pady=5)

        # Phân quyền
        tk.Label(form_frame, text="Phân quyền", font=("Arial", 12), bg="white").pack(anchor="w")
        ttk.Combobox(form_frame, values=["Accounting"], font=("Arial", 12),
                     state="readonly", width=48).pack(pady=5)

        # Trạng thái tài khoản
        tk.Label(form_frame, text="Trạng thái tài khoản", font=("Arial", 12), bg="white").pack(anchor="w")
        ttk.Combobox(form_frame, values=["Hoạt động"], font=("Arial", 12),
                     state="readonly", width=48).pack(pady=5)

        # Mật khẩu
        tk.Label(form_frame, text="Mật khẩu *", font=("Arial", 12), bg="white").pack(anchor="w")
        tk.Entry(form_frame, font=("Arial", 12), width=50, show="*").pack(pady=5)

        # Xác nhận mật khẩu
        tk.Label(form_frame, text="Xác nhận mật khẩu *", font=("Arial", 12), bg="white").pack(anchor="w")
        tk.Entry(form_frame, font=("Arial", 12), width=50, show="*").pack(pady=5)

        # Nút Lưu
        save_button = tk.Button(form_frame, text="Lưu", bg="#007BFF", fg="white",
                                font=("Arial", 12), width=10)
        save_button.pack(pady=20)

# Chạy ứng dụng
if __name__ == "__main__":
    app = CreateAccountApp()
    app.mainloop()