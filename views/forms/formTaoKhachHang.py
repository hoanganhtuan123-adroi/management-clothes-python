import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import filedialog
import tkinter.messagebox as messagebox
from controllers.khachHangController import KhachHangController
class FormTaoKhachHang(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = KhachHangController()
        self.title("Thêm khách hàng mới")
        self.configure(bg="white")
        self.geometry("800x400")  # Điều chỉnh kích thước cửa sổ
        self.result = None
        self.transient(parent)
        self.create_form()
        self.grab_set()

    def create_form(self):
        # Tùy chỉnh style cho các thành phần
        style = ttk.Style()
        style.configure("TEntry", padding=(10, 5))
        style.configure("Accent.TButton", font=("Arial", 12), padding=(10, 5))
        style.configure("Cancel.TButton", font=("Arial", 12), padding=(10, 5))

        # Tùy chỉnh màu sắc nút
        style.configure("Accent.TButton", background="#38b6ff", foreground="black")  # Nút xanh
        style.configure("Cancel.TButton", background="#ff4d4d", foreground="black")  # Nút đỏ

        # Frame chứa toàn bộ form
        form_frame = tk.Frame(self, bg="white", padx=20, pady=20)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        # Tiêu đề form
        title_label = tk.Label(form_frame, text="Thêm khách hàng mới", font=("Arial", 16, "bold"), bg="white")
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 20), sticky="w")

        # Bố cục 2 cột: bên trái và bên phải
        # Cột trái: Họ và tên, Email, Số điện thoại
        tk.Label(form_frame, text="Họ và tên", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)
        self.name_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.name_entry.grid(row=1, column=1, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Email", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)
        self.email_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.email_entry.grid(row=2, column=1, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Số điện thoại", font=("Arial", 12), bg="white").grid(row=3, column=0, sticky="e", padx=(0, 10), pady=5)
        self.phone_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.phone_entry.grid(row=3, column=1, sticky="w", padx=0, pady=5)

        # Cột phải: Giới tính, Địa chỉ, Ảnh đại diện
        tk.Label(form_frame, text="Giới tính", font=("Arial", 12), bg="white").grid(row=1, column=2, sticky="e", padx=(20, 10), pady=5)
        gender_options = ["Nam", "Nữ"]
        self.gender_var = tk.StringVar()
        self.gender_var.set("Nam")  # Default to "Nam"
        self.gender_menu = ttk.Combobox(form_frame, textvariable=self.gender_var, values=gender_options, font=("Arial", 12), state="readonly", width=17)
        self.gender_menu.grid(row=1, column=3, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Địa chỉ", font=("Arial", 12), bg="white").grid(row=2, column=2, sticky="e", padx=(20, 10), pady=5)
        self.address_entry = ttk.Entry(form_frame, font=("Arial", 12), style="TEntry", width=20)
        self.address_entry.grid(row=2, column=3, sticky="w", padx=0, pady=5)

        tk.Label(form_frame, text="Ảnh đại diện", font=("Arial", 12), bg="white").grid(row=3, column=2, sticky="e", padx=(20, 10), pady=5)
        self.image_button = ttk.Button(form_frame, text="Chọn ảnh", style="Accent.TButton", command=self.choose_image)
        self.image_button.grid(row=3, column=3, sticky="w", padx=0, pady=5)

        # Đường viền ngang phân cách
        separator = ttk.Separator(self, orient="horizontal")
        separator.pack(fill=tk.X, padx=20, pady=10)

        # Lưu và Hủy Buttons
        button_frame = tk.Frame(self, bg="white")
        button_frame.pack(fill=tk.X, padx=20, pady=10)

        self.save_button = ttk.Button(button_frame, text="Lưu", style="Accent.TButton", command=self.save_data)
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.cancel_button = ttk.Button(button_frame, text="Hủy", style="Cancel.TButton", command=self.cancel)
        self.cancel_button.pack(side=tk.LEFT, padx=10)

    def choose_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.image_button.config(text="Ảnh đã chọn")
            self.image_path = file_path

    def validate_form(self):
        # Validate that all required fields are filled
        if not self.name_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập họ và tên.")
            return False
        if not self.email_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập email.")
            return False
        if not self.phone_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập số điện thoại.")
            return False
        if not self.address_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập địa chỉ.")
            return False
        if not self.image_path:  # Check if an image has been selected
            messagebox.showerror("Lỗi", "Vui lòng chọn ảnh đại diện.")
            return False
        return True

    def save_data(self):
        if not self.validate_form():
            return

        customer_data = {
            "hoten": self.name_entry.get(),
            "email": self.email_entry.get(),
            "sdt": self.phone_entry.get(),
            "gioitinh": self.gender_var.get(),
            "diachi": self.address_entry.get(),
            "hinhanh": getattr(self, 'image_path', "")
        }
        isSuccess = self.controller.createCustomerController(customer_data)
        if isSuccess:
            messagebox.showinfo("Thông báo", "Tạo khách hàng thành công!")
            self.result = True
            self.clear_form()
        else:
            messagebox.showerror("Lỗi", "Tạo khách hàng thât bại!")
            self.result = False

    def cancel(self):
        self.result = False
        self.clear_form()

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.image_button.config(text="Chọn ảnh")
        self.gender_var.set("Nam")

# Chạy thử giao diện
if __name__ == "__main__":
    root = ThemedTk(theme="arc")  # Sử dụng chủ đề "arc" để bo tròn viền
    app = FormTaoKhachHang(root)
    root.mainloop()