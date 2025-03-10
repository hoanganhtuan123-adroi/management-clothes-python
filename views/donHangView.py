import tkinter as tk
from tkinter import ttk
from controllers.donHangController import DonHangController
from views.forms.fomTaoDonHang import CreateOrderForm
class DonHangFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.controller = DonHangController()
        self.list_orders = self.controller.getOrdersController()

        # Gọi hàm tạo giao diện
        self.create_ui()

        # Hiển thị dữ liệu
        self.update_treeview(self.list_orders)

    def create_ui(self):
        """Tạo giao diện cho cửa sổ danh sách đơn hàng."""
        # Frame chính
        main_frame = tk.Frame(self, bg="#ffffff")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Tiêu đề
        tk.Label(main_frame, text="Danh sách đơn hàng", font=("Helvetica", 16, "bold"), fg="#000",
                 bg="#ffffff").pack(anchor="w", pady=5)

        # Frame cho các nút lọc và tìm kiếm
        filter_frame = tk.Frame(main_frame, bg="#ffffff")
        filter_frame.pack(fill="x", pady=5)

        # Các nút lọc
        tk.Button(filter_frame, text="Tất cả các đơn", font=("Helvetica", 10), bg="#3498db", fg="white", width=15, command=self.get_all_orders).pack(
            side="left", padx=5)
        tk.Button(filter_frame, text="Đơn hàng mới", font=("Helvetica", 10), bg="#3498db", fg="white", width=15, command=self.get_latest_orders).pack(
            side="left", padx=5)
        tk.Button(filter_frame, text="Chưa giao hàng", font=("Helvetica", 10), bg="#3498db", fg="white", width=15, command=self.get_hasnt_delivered_orders).pack(
            side="left", padx=5)
        tk.Button(filter_frame, text="Chưa thanh toán", font=("Helvetica", 10), bg="#3498db", fg="white",
                  width=15, command=self.get_hasnt_paid_orders).pack(side="left", padx=5)

        # Ô tìm kiếm
        search_frame = tk.Frame(filter_frame, bg="#ffffff")
        search_frame.pack(side="right", padx=5)
        tk.Entry(search_frame, font=("Helvetica", 10), width=20).pack(side="left", padx=5)
        tk.Button(search_frame, text="Tìm kiếm", font=("Helvetica", 10), bg="#3498db", fg="white").pack(side="left")

        # Nút tạo đơn mới
        tk.Button(main_frame, text="+ Tạo đơn mới", font=("Helvetica", 12), bg="#3498db", fg="white", command=self.create_order).pack(anchor="e",
                                                                                                           pady=5)

        # Bảng hiển thị dữ liệu
        tree_frame = tk.Frame(main_frame, bg="#ffffff")
        tree_frame.pack(fill="both", expand=True, pady=10)

        # Tạo Treeview
        self.tree = ttk.Treeview(tree_frame, columns=(
        "ma_don_hang", "ten_san_pham", "ngay_tao", "thanh_toan", "giao_hang", "khach_hang", "tong_tien"),
                                 show="headings")
        self.tree.heading("ma_don_hang", text="Mã đơn hàng")
        self.tree.heading("ten_san_pham", text="Tên sản phẩm")
        self.tree.heading("ngay_tao", text="Ngày tạo")
        self.tree.heading("thanh_toan", text="Thanh toán")
        self.tree.heading("giao_hang", text="Giao hàng")
        self.tree.heading("khach_hang", text="Khách hàng")
        self.tree.heading("tong_tien", text="Tổng tiền (VND)")

        # Điều chỉnh độ rộng cột
        self.tree.column("ma_don_hang", width=100)
        self.tree.column("ten_san_pham", width=100)
        self.tree.column("ngay_tao", width=100)
        self.tree.column("thanh_toan", width=100)
        self.tree.column("giao_hang", width=100)
        self.tree.column("khach_hang", width=100)
        self.tree.column("tong_tien", width=120)

        # Thêm scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        # Áp dụng style cho trạng thái thanh toán và giao hàng
        self.tree.tag_configure("paid", foreground="green")
        self.tree.tag_configure("unpaid", foreground="orange")
        self.tree.tag_configure("delivered", foreground="green")
        self.tree.tag_configure("undelivered", foreground="orange")

    def update_treeview(self, orders):
        """Cập nhật dữ liệu vào Treeview."""
        # Xóa dữ liệu cũ
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Thêm dữ liệu mới
        for order in orders:
            tags = []
            # Định dạng màu cho cột Thanh toán
            # if order["thanh_toan"] == "Đã thanh toán":
            #     tags.append("paid")
            # else:
            #     tags.append("unpaid")
            #
            # # Định dạng màu cho cột Giao hàng
            # if order["giao_hang"] == "Đã giao hàng":
            #     tags.append("delivered")
            # else:
            #     tags.append("undelivered")

            values = (
                order[1],
                order[2],
                order[3].strftime("%d-%m-%Y"),
                order[4],
                order[5],
                order[6],
                "{:,.0f}".format(order[7]  * order[8])
            )
            self.tree.insert("", tk.END, values=values, tags=tags)

    def get_all_orders(self):
        self.list_orders = self.controller.getOrdersController()
        self.update_treeview(self.list_orders)

    def get_latest_orders(self):
        self.list_orders = self.controller.getOrdersLatestController()
        self.update_treeview(self.list_orders)

    def get_hasnt_paid_orders(self):
        self.list_orders = self.controller.getOrdersHasntPaidController()
        self.update_treeview(self.list_orders)

    def get_hasnt_delivered_orders(self):
        self.list_orders = self.controller.getOrdersHasntDeliveredController()
        self.update_treeview(self.list_orders)

    def create_order(self):
        CreateOrderForm(self)