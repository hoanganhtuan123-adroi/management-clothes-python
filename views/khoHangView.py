import tkinter as tk
from tkinter import ttk
class KhoHangFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")

        label = tk.Label(self, text="Giao diện Kho Hang", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Ví dụ bảng Treeview để hiển thị danh sách khách hàng
        columns = ("khach_hang", "dien_thoai", "dia_chi")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("khach_hang", text="Khách hàng")
        self.tree.heading("dien_thoai", text="Điện thoại")
        self.tree.heading("dia_chi", text="Địa chỉ")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Thêm dữ liệu mẫu
        sample_data = [
            ("Haravan Demo", "01234567", "HCM"),
            ("Nguyen Van A", "09876543", "Ha Noi"),
            ("Tran Thi B", "09123456", "Da Nang"),
        ]
        for row in sample_data:
            self.tree.insert("", tk.END, values=row)