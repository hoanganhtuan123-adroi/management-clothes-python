import tkinter as tk
from tkinter import ttk, messagebox
from controllers.khoHangController import KhoHangController
from config.commonDef import  CommonDef
from views.forms.formNhapKho import NhapKhoForm
from views.forms.formXuatKho import XuatKhoForm
class KhoHangFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.controller = KhoHangController()
        self.commondef = CommonDef()
        self.create_ui()
        # self.table_kiem_kho()
        self.table_kiem_kho()

    def create_ui(self):
        """Tạo giao diện cho cửa sổ danh sách đơn hàng."""
        # Frame chính
        main_frame = tk.Frame(self, bg="#ffffff")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Tiêu đề
        tk.Label(main_frame, text="Quản lý kho hàng", font=("Helvetica", 16, "bold"), fg="#000",
                 bg="#ffffff").pack(anchor="w", pady=5)

        # Frame cho các nút lọc và tìm kiếm
        filter_frame = tk.Frame(main_frame, bg="#ffffff")
        filter_frame.pack(fill="x", pady=5)

        # Các nút
        tk.Button(filter_frame, text="Kiểm kho",font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5, command=self.on_kiem_kho_click).pack(
            side="left", padx=5)
        tk.Button(filter_frame, text="Tồn kho", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5,command=self.on_ton_kho_click ).pack(
            side="left", padx=5)
        tk.Button(filter_frame, text="Nhập kho", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5, command=self.open_form_nhapkho).pack(
            side="left", padx=5)
        tk.Button(filter_frame, text="Xuất kho", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5,command=self.open_form_xuatkho).pack(side="left", padx=5)

        # Ô tìm kiếm
        search_frame = tk.Frame(filter_frame, bg="#ffffff")
        search_frame.pack(side="right", padx=5)
        tk.Entry(search_frame, font=("Helvetica", 10), width=20).pack(side="left", padx=5)
        tk.Button(search_frame, text="Tìm kiếm", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5,).pack(side="left")

        # Bảng hiển thị dữ liệu
        self.tree_frame = tk.Frame(main_frame, bg="#ffffff")
        self.tree_frame.pack(fill="both", expand=True, pady=10)

        # # Gắn sự kiện khi chọn một hàng
        # # self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    # bảng tồn kho
    def table_ton_kho(self):
        for widget in self.tree_frame.winfo_children():
            widget.destroy()
        # Tạo Treeview
        self.tree = ttk.Treeview(self.tree_frame, columns=(
        "ma_san_pham", "so_luong_nhap", "so_luong_ton_kho", "so_luong_ban_ra", "ngay_nhap", "gia_nhap"),
                                 show="headings")
        self.tree.heading("ma_san_pham", text="Mã sản phẩm")
        self.tree.heading("so_luong_nhap", text="Số lượng nhập")
        self.tree.heading("so_luong_ton_kho", text="Số lượng tồn kho")
        self.tree.heading("so_luong_ban_ra", text="Số lượng bán ra")
        self.tree.heading("ngay_nhap", text="Ngày nhập")
        self.tree.heading("gia_nhap", text="Giá nhập")

        # Điều chỉnh độ rộng cột
        self.tree.column("ma_san_pham", width=100)
        self.tree.column("so_luong_nhap", width=100)
        self.tree.column("so_luong_ton_kho", width=100)
        self.tree.column("so_luong_ban_ra", width=100)
        self.tree.column("ngay_nhap", width=100)
        self.tree.column("gia_nhap", width=100)

        # Thêm scrollbar
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        listProducts = self.controller.getAllProductsController()
        self.update_table_ton_kho(listProducts)

    # Đẩy giá trị vào bảng tồn kho
    def update_table_ton_kho(self, listProducts):
        # Xóa dữ liệu cũ
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Thêm dữ liệu mới

        for product in listProducts:
            tags = []
            values = (
                product[1],
                product[2],
                product[3],
                product[4],
                product[5].strftime("%Y-%m-%d"),
                self.commondef.format_number(product[6]),
            )
            self.tree.insert("", tk.END, values=values, tags=tags)

    # Bảng kiểm kho
    def table_kiem_kho(self):
        for widget in self.tree_frame.winfo_children():
            widget.destroy()
        # Tạo Treeview
        self.tree = ttk.Treeview(self.tree_frame, columns=(
            "ma_san_pham", "so_luong", "loai_giao_dich", "ngay_giao_dich", "tong_gia_tri"),
                                 show="headings")
        self.tree.heading("ma_san_pham", text="Mã sản phẩm")
        self.tree.heading("so_luong", text="Số lượng")
        self.tree.heading("loai_giao_dich", text="Loại giao dịch")
        self.tree.heading("ngay_giao_dich", text="Ngày giao dịch")
        self.tree.heading("tong_gia_tri", text="Tổng giá trị")

        # Điều chỉnh độ rộng cột
        self.tree.column("ma_san_pham", width=100)
        self.tree.column("so_luong", width=100)
        self.tree.column("loai_giao_dich", width=100)
        self.tree.column("ngay_giao_dich", width=100)
        self.tree.column("tong_gia_tri", width=100)

        # Thêm scrollbar
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        historyTrades = self.controller.getAllHistoryController()
        self.update_table_kiem_kho(historyTrades)
    # Đẩy giá trị vào bảng kiểm kho
    def update_table_kiem_kho(self, listHistory):
        # Xóa dữ liệu cũ

        for item in self.tree.get_children():
            self.tree.delete(item)
        # Thêm dữ liệu mới
        for product in listHistory:
            tags = []
            values = (
                product[1],
                product[2],
                product[3],
                product[4].strftime("%Y-%m-%d"),
                self.commondef.format_number(product[5]),
            )
            self.tree.insert("", tk.END, values=values, tags=tags)

    def on_kiem_kho_click(self):
        self.table_kiem_kho()

    def on_ton_kho_click(self):
        self.table_ton_kho()

    def open_form_nhapkho(self):
        NhapKhoForm(self)

    def open_form_xuatkho(self):
        XuatKhoForm(self)