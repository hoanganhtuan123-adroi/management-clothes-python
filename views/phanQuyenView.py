import tkinter as tk
from tkinter import ttk
from controllers.taiKhoanController import TaiKhoanController
from views.forms.formTaoTK import CreateAccountApp
from views.forms.formTTTaiKhoan import FormThongTinTaiKhoan
class PhanQuyenFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.controller = TaiKhoanController()
        self.list_accounts = self.controller.getAllAccountsController()

        # Tạo giao diện
        self.create_ui()
        self.update_treview()

    def create_ui(self):
        """Tạo giao diện cho cửa sổ danh sách đơn hàng."""
        # Frame chính
        main_frame = tk.Frame(self, bg="#ffffff")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Tiêu đề
        tk.Label(main_frame, text="Phân quyền tài khoản", font=("Helvetica", 16, "bold"), fg="#000",
                 bg="#ffffff").pack(anchor="w", pady=5)

        # Frame cho các nút lọc và tìm kiếm
        filter_frame = tk.Frame(main_frame, bg="#ffffff")
        filter_frame.pack(fill="x", pady=5)

        # Ô tìm kiếm
        search_frame = tk.Frame(filter_frame, bg="#ffffff")
        search_frame.pack(side="right", padx=5)
        tk.Entry(search_frame, font=("Helvetica", 10), width=20).pack(side="left", padx=5)
        tk.Button(search_frame, text="Tìm kiếm", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5,).pack(side="left")

        # Nút tạo đơn mới
        tk.Button(main_frame, text="+ Tạo mới", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5, command=self.open_form_create_account).pack(anchor="e")

        # Bảng hiển thị dữ liệu
        tree_frame = tk.Frame(main_frame, bg="#ffffff")
        tree_frame.pack(fill="both", expand=True, pady=10)

        # Tạo Treeview
        self.tree = ttk.Treeview(tree_frame, columns=(
            "ma_nhan_vien", "ten_nhan_vien", "tai_khoan", "mat_khau", "vai_tro", "trang_thai_tai_khoan"),
                                 show="headings")
        self.tree.heading("ma_nhan_vien", text="Mã nhân viên")
        self.tree.heading("ten_nhan_vien", text="Tên nhân viên")
        self.tree.heading("tai_khoan", text="Tài khoản")
        self.tree.heading("mat_khau", text="Mật khẩu")
        self.tree.heading("vai_tro", text="Vai trò")
        self.tree.heading("trang_thai_tai_khoan", text="Trạng thái tài khoản")

        # Điều chỉnh độ rộng cột
        self.tree.column("ma_nhan_vien", width=100)
        self.tree.column("ten_nhan_vien", width=100)
        self.tree.column("tai_khoan", width=100)
        self.tree.column("mat_khau", width=100)
        self.tree.column("vai_tro", width=100)
        self.tree.column("trang_thai_tai_khoan", width=100)

        # Thêm scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    def update_treview(self):
        for item in self.list_accounts:
            values = [
                item[0],
                item[1],
                item[2],
                item[3],
                item[4],
                item[5]
            ]
            self.tree.insert("", tk.END, values=values)


    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        row_data = self.tree.item(selected_item)['values'][0]
        FormThongTinTaiKhoan(self, row_data)


    def open_form_create_account(self):
        CreateAccountApp(self)

