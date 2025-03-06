import tkinter as tk
from tkinter import messagebox
class LoginView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Đăng nhập")
        self.geometry("300x200")

        # Tạo giao diện đăng nhập
        self.lbl_username = tk.Label(self, text="Username:")
        self.lbl_username.pack(pady=5)

        self.entry_username = tk.Entry(self)
        self.entry_username.pack(pady=5)

        self.lbl_password = tk.Label(self, text="Password:")
        self.lbl_password.pack(pady=5)

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        self.btn_login = tk.Button(self, text="Đăng nhập")
        self.btn_login.pack(pady=20)

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