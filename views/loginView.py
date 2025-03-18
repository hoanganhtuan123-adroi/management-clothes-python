import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  # Để thêm biểu tượng
from tkinter import PhotoImage

class LoginView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Đăng nhập")
        self.geometry("400x300")
        self.configure(bg="#d3d3d3")  # Nền xám nhạt

        # Tạo khung chính để chứa giao diện
        main_frame = tk.Frame(self, bg="#ffffff", padx=20, pady=20, relief=tk.RAISED, borderwidth=2)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Căn giữa

        # Tiêu đề
        title_label = tk.Label(main_frame, text="Admin", font=("Arial", 24, "bold"), bg="#ffffff", fg="#000000")
        title_label.pack(pady=(0, 30))

        # Frame cho trường Email
        email_frame = tk.Frame(main_frame, bg="#ffffff")
        email_frame.pack(fill=tk.X, pady=5)
        tk.Label(email_frame, text="Email", font=("Arial", 12), bg="#ffffff", anchor="w").pack(side=tk.LEFT,
                                                                                               padx=(0, 10))
        self.entry_username = tk.Entry(email_frame, font=("Arial", 12), width=25)
        self.entry_username.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        # Thêm biểu tượng email
        # email_icon = PhotoImage(file="/assets/img/icon/email_icon.png")  # Thay bằng đường dẫn biểu tượng email
        # # email_icon = email_icon.resize((20, 20), Image.Resampling.LANCZOS)
        # # email_icon_img = ImageTk.PhotoImage(email_icon)
        # tk.Label(email_frame, image=email_icon, bg="#ffffff").pack(side=tk.RIGHT)
        # self.email_icon_img = email_icon  # Giữ tham chiếu để tránh garbage collected

        # Frame cho trường Mật khẩu
        password_frame = tk.Frame(main_frame, bg="#ffffff")
        password_frame.pack(fill=tk.X, pady=5)
        tk.Label(password_frame, text="Mật khẩu", font=("Arial", 12), bg="#ffffff", anchor="w").pack(side=tk.LEFT,
                                                                                                     padx=(0, 10))
        self.entry_password = tk.Entry(password_frame, font=("Arial", 12), show="*", width=25)
        self.entry_password.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        # Thêm biểu tượng khóa
        # lock_icon = PhotoImage(file="assets/img/icon/pass_icon.png")  # Thay bằng đường dẫn biểu tượng khóa
        # # lock_icon = lock_icon.resize((20, 20), Image.Resampling.LANCZOS)
        # # lock_icon_img = ImageTk.PhotoImage(lock_icon)
        # tk.Label(password_frame, image=lock_icon, bg="#ffffff").pack(side=tk.RIGHT)
        # self.lock_icon_img = lock_icon  # Giữ tham chiếu

        # Nút Đăng nhập
        self.btn_login = tk.Button(main_frame, text="Đăng nhập", font=("Arial", 12, "bold"), bg="#2196F3", fg="white",
                                   activebackground="#1976D2", cursor="hand2")
        self.btn_login.pack(pady=20, fill=tk.X)

    def set_login_handler(self, handler):
        self.btn_login.config(command=handler)

    def get_username(self) -> str:
        return self.entry_username.get()

    def get_password(self) -> str:
        return self.entry_password.get()

    def show_message(self, title: str, message: str):
        messagebox.showinfo(title, message)

    def show_error(self, title: str, message: str):
        messagebox.showerror(title, message)


if __name__ == "__main__":
    app = LoginView()

