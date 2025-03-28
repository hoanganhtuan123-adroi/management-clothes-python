import tkinter as tk
from tkinter import ttk
from controllers.donHangController import DonHangController
from views.forms.fomTaoDonHang import CreateOrderForm
from config.commonDef import CommonDef
from tkinter import messagebox
class DonHangFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.controller = DonHangController()
        self.list_orders = self.controller.getOrdersController()
        self.commonDef = CommonDef()
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
        tk.Button(filter_frame, text="Tất cả các đơn", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5, command=self.get_all_orders).pack(
            side="left", padx=5)
        tk.Button(filter_frame, text="Đơn hàng mới",font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5, command=self.get_latest_orders).pack(
            side="left", padx=5)
        tk.Button(filter_frame, text="Chưa giao hàng", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5, command=self.get_hasnt_delivered_orders).pack(
            side="left", padx=5)
        tk.Button(filter_frame, text="Chưa thanh toán", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5, command=self.get_hasnt_paid_orders).pack(side="left", padx=5)

        # Ô tìm kiếm
        search_frame = tk.Frame(filter_frame, bg="#ffffff")
        search_frame.pack(side="right", padx=5)
        tk.Entry(search_frame, font=("Helvetica", 10), width=20).pack(side="left", padx=5)
        tk.Button(search_frame, text="Tìm kiếm",font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5,).pack(side="left")

        # Nút tạo đơn mới
        tk.Button(main_frame, text="+ Tạo đơn mới",font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5, command=self.create_order).pack(anchor="e")

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

        # Gắn sự kiện khi chọn một hàng
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Nút tạo đơn mới
        tk.Button(main_frame, text="Xóa đơn hàng", font=("Helvetica", 12), bg="#3498db", fg="white",command= self.delete_selected_order).pack(anchor="e",pady=5)

    def get_orders(self):
        list_orders = self.controller.getOrdersController()
        return list_orders

    def update_treeview(self, orders):
        # Xóa dữ liệu cũ
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Thêm dữ liệu mới
        for order in orders:
            tags = []
            values = (
                order[1],
                order[2],
                order[3].strftime("%d-%m-%Y"),
                order[4],
                order[5],
                order[6],
                self.commonDef.format_number(order[9])
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

    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một đơn hàng để xóa!")
            return
        if selected_item:
            item = self.tree.item(selected_item[0])
            values = item["values"]
            self.selected_id_delete = values[0]

    def delete_selected_order(self):
        if self.selected_id_delete is not None:
            # Gọi hàm xóa
            self.delete_order(self.selected_id_delete)

    def delete_order(self, id):
        isConfirm =  messagebox.askyesno("Thông báo", "Bạn có chắc chắn xóa đơn hàng này không?")
        if isConfirm:
            isSuccess = self.controller.deleteOrderContrller(id)
            if isSuccess:
                messagebox.showinfo("Thông báo", "Xóa thành công!")
            else:
                messagebox.showerror("Thông báo", "Xóa thất bại")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x600")
    app = DonHangFrame(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()