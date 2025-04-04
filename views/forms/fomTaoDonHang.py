import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from controllers.sanPhamController import SanPhamController
from controllers.khachHangController import KhachHangController
from controllers.donHangController import DonHangController
from views.forms.formTaoKhachHang import FormTaoKhachHang
from config.commonDef import CommonDef

class CreateOrderForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Tạo đơn hàng")
        self.geometry("1200x600")
        self.config(bg="#f5f6fa")
        # Tạo container chính
        self.main_container = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.main_container.pack(fill="both", expand=True)

        # Form đơn hàng bên trái
        self.order_frame = ttk.Frame(self.main_container, width=800)
        self.main_container.add(self.order_frame, stretch="always")

        # Form khách hàng bên phải
        self.customer_frame = ttk.Frame(self.main_container, width=400)
        self.main_container.add(self.customer_frame, stretch="never")

        self.orderController = DonHangController()
        self.customerController = KhachHangController()
        self.controller = SanPhamController()
        self.list_customers = self.customerController.getAllCustomersController()
        self.list_products = self.controller.getProductsController()

        self.configDef = CommonDef()

        self.order_items = []
        self.selected_customer = None
        # Dữ liệu mẫu

        # Tạo giao diện
        self.create_ui()
        self.create_ui_customer()
        self.insert_products_to_listbox()
        self.insert_customers_to_listbox()

    def create_ui(self):
        main_frame = tk.Frame(self, bg="#f5f6fa")
        main_frame.pack(side='left' ,fill="both", expand=True, padx=20, pady=20)

        # Tiêu đề
        tk.Label(main_frame, text="Tạo đơn hàng", font=("Helvetica", 18, "bold"),
                 fg="#2d3436", bg="#f5f6fa").pack(anchor="w", pady=10)

        # Phần tìm kiếm
        search_frame = tk.Frame(main_frame, bg="#f5f6fa")
        search_frame.pack(fill="x", pady=5)

        self.product_search_entry = tk.Entry(search_frame, font=("Helvetica", 12),
                                             bd=2, relief=tk.GROOVE, highlightbackground="#dcdde1")
        self.product_search_entry.pack(fill="x", ipady=5)
        self.product_search_entry.bind("<KeyRelease>", self.search_product)

        # Danh sách sản phẩm
        self.product_listbox = tk.Listbox(main_frame, font=("Helvetica", 12),
                                          height=4, bg="white", relief=tk.FLAT)
        self.product_listbox.pack(fill="x", pady=5)
        self.product_listbox.bind("<<ListboxSelect>>", self.select_product)

        # Phần sản phẩm đã chọn
        products_header = tk.Frame(main_frame, bg="#f5f6fa")
        products_header.pack(fill="x", pady=(15, 5))

        tk.Label(products_header, text="Sản phẩm", width=15, anchor="w", font=("Helvetica", 12, "bold"),
                 bg="#f5f6fa").grid(row=0, column=0, sticky="w")
        tk.Label(products_header, text="Số lượng", width=10, font=("Helvetica", 12, "bold"),
                 bg="#f5f6fa").grid(row=0, column=1)
        tk.Label(products_header, text="Thành tiền", width=15, font=("Helvetica", 12, "bold"),
                 bg="#f5f6fa").grid(row=0, column=2)

        # Khung chứa sản phẩm
        self.products_container = tk.Frame(main_frame, bg="#f5f6fa")
        self.products_container.pack(fill="x")

        # Phần thanh toán
        payment_frame = tk.Frame(main_frame, bg="#f5f6fa")
        payment_frame.pack(fill="x", pady=10)

        tk.Label(payment_frame, text="Tiền hàng", font=("Helvetica", 12),
                 bg="#f5f6fa").grid(row=0, column=0, sticky="w")
        self.total_items_label = tk.Label(payment_frame, text="0 sản phẩm", font=("Helvetica", 12),
                                          bg="#f5f6fa")
        self.total_items_label.grid(row=0, column=1, sticky="e", padx=10)

        self.total_price_label = tk.Label(payment_frame, text="0 đ", font=("Helvetica", 12),
                                          bg="#f5f6fa")
        self.total_price_label.grid(row=0, column=2, sticky="e")

        # Phương thức thanh toán
        tk.Label(payment_frame, text="Phương thức thanh toán", font=("Helvetica", 12),
                 bg="#f5f6fa").grid(row=1, column=0, sticky="w", pady=10)
        self.payment_method = ttk.Combobox(payment_frame, values=["Chuyển khoản", "Thanh toán khi nhận hàng"],
                                           state="readonly", font=("Helvetica", 12), width=20)
        self.payment_method.set("Chuyển khoản")
        self.payment_method.grid(row=1, column=1, columnspan=2, sticky="e", padx=10)

        # Tổng tiền
        tk.Label(payment_frame, text="Tổng tiền", font=("Helvetica", 14, "bold"),
                 bg="#f5f6fa").grid(row=2, column=0, sticky="w", pady=10)
        self.total_amount_label = tk.Label(payment_frame, text="0 đ", font=("Helvetica", 14, "bold"),
                                           fg="#e74c3c", bg="#f5f6fa")
        self.total_amount_label.grid(row=2, column=2, sticky="e")

        # Nút điều khiển
        control_frame = tk.Frame(main_frame, bg="#f5f6fa")
        control_frame.pack(fill="x", pady=20)

        tk.Button(control_frame, text="HỦY", font=("Helvetica", 12, "bold"), fg="white",
                  bg="#95a5a6", width=10, command=self.destroy).pack(side="right", padx=10)
        tk.Button(control_frame, text="TẠO ĐƠN HÀNG", font=("Helvetica", 12, "bold"),
                  fg="white", bg="#3498db", width=15, command=self.create_order).pack(side="right")

        self.order_frame.configure(style="TFrame")

    def search_product(self, event=None):
        search_term = self.product_search_entry.get().strip().lower()
        self.product_listbox.delete(0, tk.END)

        if not search_term:
            return

        matching_products = [p for p in self.list_products if (search_term in p["ten_sp"].lower() or search_term in str(p.get("ma_sp", "")).lower() )]
        for product in matching_products:
            self.product_listbox.insert(tk.END, f"{product['ten_sp']} - {product['ma_sp']} - {self.configDef.format_number(product['gia_ban'])}")

    def insert_products_to_listbox(self):
        for product in self.list_products:
            self.product_listbox.insert(tk.END, f"{product['ten_sp']} - {product['ma_sp']} - {self.configDef.format_number(product['gia_ban'])}")

    def select_product(self, event=None):
        if not self.product_listbox.curselection():
            return

        selected_index = self.product_listbox.curselection()[0]
        product_name = self.product_listbox.get(selected_index).split(" - ")[0]

        for product in self.list_products:
            if product["ten_sp"] == product_name:
                self.add_product_to_order(product)
                break

    def add_product_to_order(self, product):
        # Check if product exists
        for item in self.order_items:
            if item["product"]["id"] == product["id"]:
                item["quantity_var"].set(item["quantity_var"].get() + 1)
                self.update_totals()
                return

        # Add new product
        product_frame = tk.Frame(self.products_container, bg="#f5f6fa")
        product_frame.pack(fill="x", pady=3)

        # Checkbox
        product_frame = tk.Frame(self.products_container, bg="#f5f6fa")
        product_frame.pack(fill="x", pady=3)

        try:
            if product["hinh_anh"]:  # Nếu có đường dẫn ảnh
                product_img = product['hinh_anh'].split(", ")[0]
                image = Image.open( product_img)
                image = image.resize((60, 60), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                img_label = tk.Label(product_frame, image=photo, bg="#f5f6fa")
                img_label.image = photo  # Giữ reference
                img_label.grid(row=0, column=0, padx=10)
            else:  # Ảnh mặc định
                no_image = tk.Label(product_frame, text="[Ảnh]", width=6,
                                    font=("Helvetica", 10), bg="#dcdde1")
                no_image.grid(row=0, column=0, padx=10)
        except Exception as e:  # Xử lý lỗi load ảnh
            error_img = tk.Label(product_frame, text="[Lỗi ảnh]", width=6,
                                 fg="red", font=("Helvetica", 10), bg="#f5f6fa")
            error_img.grid(row=0, column=0, padx=10)

        # Product name
        tk.Label(product_frame, text=product["ten_sp"], font=("Helvetica", 12),
                 bg="#f5f6fa").grid(row=0, column=1, sticky="w", padx=10)

        # Quantity controls
        quantity_frame = tk.Frame(product_frame, bg="#f5f6fa")
        quantity_frame.grid(row=0, column=2, padx=10)

        quantity_var = tk.IntVar(value=1)
        tk.Button(quantity_frame, text="−", font=("Helvetica", 10), relief=tk.FLAT,
                  bg="#dcdde1", command=lambda: self.update_quantity(quantity_var, -1)).pack(side="left")
        tk.Label(quantity_frame, textvariable=quantity_var, width=3,
                 font=("Helvetica", 12)).pack(side="left")
        tk.Button(quantity_frame, text="+", font=("Helvetica", 10), relief=tk.FLAT,
                  bg="#dcdde1", command=lambda: self.update_quantity(quantity_var, 1)).pack(side="left")

        # Total price
        total_price = tk.StringVar(value=f"{self.configDef.format_number(product['gia_ban'] * quantity_var.get())}")
        tk.Label(product_frame, textvariable=total_price, font=("Helvetica", 12),
                 bg="#f5f6fa").grid(row=0, column=3, sticky="e")

        # Delete button
        tk.Button(product_frame, text="✕", font=("Helvetica", 12), fg="#e74c3c",
                  bg="#f5f6fa", bd=0, command=lambda f=product_frame: self.remove_product(f, product)) \
            .grid(row=0, column=4, padx=10)

        self.order_items.append({
            "frame": product_frame,
            "product": product,
            "quantity_var": quantity_var,
            "total_price": total_price
        })

        self.update_totals()

    def update_quantity(self, var, delta):
        var.set(max(1, var.get() + delta))
        self.update_totals()

    def remove_product(self, frame, product):
        for item in self.order_items[:]:
            if item["product"] == product:
                item["frame"].destroy()
                self.order_items.remove(item)
        self.update_totals()

    def update_totals(self):
        total_items = sum(item["quantity_var"].get() for item in self.order_items)
        total_price = sum(item["product"]["gia_ban"] * item["quantity_var"].get() for item in self.order_items)

        self.total_items_label.config(text=f"{total_items} sản phẩm")
        self.total_price_label.config(text=f"{self.configDef.format_number(total_price)}")
        self.total_amount_label.config(text=f"{self.configDef.format_number(total_price)}")

        for item in self.order_items:
            total = item["product"]["gia_ban"] * item["quantity_var"].get()
            item["total_price"].set(f"{self.configDef.format_number(total)}")

    # Tạo đơn mới
    def create_order(self):
        if not self.order_items:
            messagebox.showwarning("Cảnh báo", "Vui lòng thêm sản phẩm!")
            return

        order_data = {
            "customer_id": self.selected_customer['id'],
            "dia_chi": self.selected_customer['diachi'],
            "items": [(item["product"]["id"], item["quantity_var"].get()) for item in self.order_items],
            "total": sum(item["product"]["gia_ban"] * item["quantity_var"].get() for item in self.order_items),
            "payment_method": self.payment_method.get()
        }
        data = self.orderController.createOrderController(order_data)
        if data:
            messagebox.showinfo("Thành công", "Tạo đơn hàng thành công!")
            new_data = self.parent.get_orders()
            self.parent.update_treeview(new_data)
            self.destroy()
        else:
            messagebox.showerror("Lỗi", "Tạo đơn hàng thất bại!")

    def create_ui_customer(self):
        main_frame = tk.Frame(self, bg="#f5f6fa")
        main_frame.pack(side='right', fill="both", expand=True, padx=20, pady=20)

        # Phần tìm kiếm
        search_frame = tk.Frame(main_frame, bg="#f5f6fa")
        search_frame.pack(fill="x", pady=5)

        tk.Label(search_frame, text="Tìm kiếm khách hàng", font=("Helvetica", 18, "bold"),
                 bg="#f5f6fa", pady=10).pack(anchor="w")
        self.customer_search_entry = tk.Entry(search_frame, font=("Helvetica", 12),
                                     bd=2, relief=tk.GROOVE)
        self.customer_search_entry.pack(fill="x", pady=5)
        self.customer_search_entry.bind("<KeyRelease>", self.search_customer)
        # Danh sách khách hàng
        self.customer_listbox = tk.Listbox(main_frame, font=("Helvetica", 12),
                                           height=5, bg="white")
        self.customer_listbox.pack(fill="x", pady=5)
        self.customer_listbox.bind("<<ListboxSelect>>", self.show_customer_details)

        # Phần tạo khách hàng mới
        create_frame = tk.Frame(main_frame, bg="#f5f6fa")
        create_frame.pack(fill="x", pady=10)

        tk.Button(create_frame, text="Tạo khách hàng mới", bg="#3498db", fg="white",font=("Helvetica", 12, "bold"),
                  command=self.create_customer).grid(row=0, column=0, columnspan=2, sticky="w", pady=5)

        # Thông tin giao hàng
        shipping_frame = tk.Frame(main_frame, bg="#f5f6fa")
        shipping_frame.pack(fill="x", pady=10)

        tk.Label(shipping_frame, text="Thông tin giao hàng", font=("Helvetica", 12, "bold"),
                 bg="#f5f6fa").pack(anchor="w")

        self.shipping_info = tk.Label(shipping_frame, text="", justify=tk.LEFT,
                                      bg="#f5f6fa", font=("Helvetica", 12), wraplength=300)
        self.shipping_info.pack(anchor="w", fill="x")
        self.order_frame.configure(style="TFrame")

    def show_customer_details(self, event):
        selection = self.customer_listbox.curselection()
        print(selection)
        selection_text = self.customer_listbox.get(selection)
        selection_name = selection_text.split('-')[1].strip()

        if selection:
            for customer in self.list_customers:
                if customer['email'] == selection_name:
                    self.selected_customer = customer
                    details = f"Người nhận: {customer['hoten']}\n"
                    details += f"SĐT: {customer['sdt']}\n"
                    details += f"Địa chỉ: {customer['diachi']}"
                    self.shipping_info.config(text=details)

    def search_customer(self, event=None):
        search_term = self.customer_search_entry.get().strip().lower()  # Lấy chuỗi tìm kiếm và chuẩn hóa
        self.customer_listbox.delete(0, tk.END)  # Xóa toàn bộ danh sách hiện tại

        if not search_term:  # Nếu chuỗi tìm kiếm rỗng, thoát hàm
            return

        # Lọc danh sách khách hàng dựa trên chuỗi tìm kiếm
        filtered_customers = [customer for customer in self.list_customers
                              if search_term in customer["hoten"].lower()]
        # Thêm các khách hàng phù hợp vào Listbox
        for customer in filtered_customers:
            self.customer_listbox.insert(tk.END, f"{customer["hoten"]} - {customer["email"] }" )

    def insert_customers_to_listbox(self):
        self.customer_listbox.delete(0, tk.END)
        for customer in self.list_customers:
            self.customer_listbox.insert(tk.END, f"{customer['hoten']} - {customer['email'] }" )
        print(f"Đã thêm {len(self.list_customers)} khách hàng vào listbox")

    def create_customer(self):
        form = FormTaoKhachHang(self)
        self.wait_window(form)
        if form.result:  # Kiểm tra nếu result là True (thành công)
            self.list_customers = self.customerController.getAllCustomersController()
            if not self.list_customers:  # Kiểm tra nếu danh sách rỗng
                print("Không có dữ liệu khách hàng mới!")
                return
            self.customer_listbox.delete(0, tk.END)
            self.insert_customers_to_listbox()
            print("Khách hàng đã được tạo thành công!")
        else:  # Nếu result là False, thông báo thất bại
            print("Có lỗi khi tạo khách hàng!")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    form = CreateOrderForm(root)
    root.mainloop()