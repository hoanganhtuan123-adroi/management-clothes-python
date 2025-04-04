import tkinter as tk
from tkinter import ttk
from controllers.nhaCungCapController import NhaCungCapController
from views.forms.formThemMoiNCC import ThemNhaCungCapForm
from views.forms.formSuaTTNCC import ThongTinNCCForm
class NhaCungCapFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.contrller = NhaCungCapController()
        self.create_ui()
        self.create_table()
        self.update_treeview()

    def create_ui(self):
        """Tạo giao diện cho cửa sổ danh sách đơn hàng."""
        # Frame chính
        main_frame = tk.Frame(self, bg="#ffffff")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Tiêu đề
        tk.Label(main_frame, text="Quản lý nhà cung cấp", font=("Helvetica", 16, "bold"), fg="#000",
                 bg="#ffffff").pack(anchor="w", pady=5)

        # Frame cho các nút lọc và tìm kiếm
        filter_frame = tk.Frame(main_frame, bg="#ffffff")
        filter_frame.pack(fill="x", pady=5)

        # Các nút
        tk.Button(filter_frame, text="Thêm nhà cung cấp", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5, command=self.open_form_add_supplier
                  ).pack(
            side="right", padx=5)
        # Ô tìm kiếm
        search_frame = tk.Frame(filter_frame, bg="#ffffff")
        search_frame.pack(side="right", padx=5)
        tk.Entry(search_frame, font=("Helvetica", 10), width=20).pack(side="left", padx=5)
        tk.Button(search_frame, text="Tìm kiếm",font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5,).pack(side="left")

        # Bảng hiển thị dữ liệu
        self.tree_frame = tk.Frame(main_frame, bg="#ffffff")
        self.tree_frame.pack(fill="both", expand=True, pady=10)

    def create_table(self):
        for widget in self.tree_frame.winfo_children():
            widget.destroy()
        # Tạo Treeview
        self.tree = ttk.Treeview(self.tree_frame, columns=(
            "ma_nha_cung_cap", "don_vi_cung_cap", "mat_hang", "email", "so_dien_thoai", "dia_chi"),
                                 show="headings")
        self.tree.heading("ma_nha_cung_cap", text="Mã nhà cung cấp")
        self.tree.heading("don_vi_cung_cap", text="Đơn vị cung cấp")
        self.tree.heading("mat_hang", text="Mặt hàng")
        self.tree.heading("email", text="Email")
        self.tree.heading("so_dien_thoai", text="Số điện thoại")
        self.tree.heading("dia_chi", text="Địa chỉ")

        # Điều chỉnh độ rộng cột
        self.tree.column("ma_nha_cung_cap", width=100)
        self.tree.column("don_vi_cung_cap", width=100)
        self.tree.column("mat_hang", width=100)
        self.tree.column("email", width=100)
        self.tree.column("so_dien_thoai", width=100)
        self.tree.column("dia_chi", width=100)

        # Thêm scrollbar
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)
        # Gắn sự kiện khi chọn một hàng
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    def update_treeview(self):
        list_suppliers = self.contrller.getAllSuppliersControlller()
        for item in self.tree.get_children():
            self.tree.delete(item)

        if list_suppliers:
            for row in list_suppliers:
                values = (
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6]
                )
                self.tree.insert("", tk.END, values=values, tags=(row))
        else:
            self.tree.insert("", tk.END, values=["Không có nhà cung cấp", "", "", "", "", ""])

    def on_tree_select(self, event):
        selected_items = self.tree.selection()
        if selected_items:
            selected_item = selected_items[0]
            values = self.tree.item(selected_item)['tags']
            print(f"Selected: {values}")
            ThongTinNCCForm(self, values)
        else:
            print("No item selected")

    def open_form_add_supplier(self):
        ThemNhaCungCapForm(self)