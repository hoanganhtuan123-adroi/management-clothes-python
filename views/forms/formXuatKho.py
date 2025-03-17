import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from controllers.sanPhamController import SanPhamController
from controllers.khoHangController import KhoHangController

class XuatKhoForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Quản lý Xuất Kho")
        self.geometry("800x600")
        self.configure(bg="#F5F5F5")
        self.controller_kho = KhoHangController()
        self.controller_product = SanPhamController()
        self.list_products = self.controller_product.getProductsController()

        # Style configuration
        self.style = ttk.Style()
        self.style.configure("TLabel", background="#F5F5F5", font=("Arial", 10))
        self.style.configure("TButton", font=("Arial", 10), padding=6)
        self.style.map("TButton",
                       foreground=[('active', 'black'), ('!active', 'black')],
                       background=[('active', '#E1E1E1'), ('!active', '#F0F0F0')]
                       )

        # Main container
        main_frame = tk.Frame(self, bg="#F5F5F5", padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)

        # Title
        tk.Label(main_frame, text="XUẤT KHO HÀNG", font=("Arial", 16, "bold"),
                 bg="#F5F5F5", fg="#2C3E50").grid(row=0, column=0, columnspan=4, pady=15, sticky="w")

        # Danh sách sản phẩm
        list_container = tk.Frame(main_frame, bg="#F5F5F5")
        list_container.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Product Listbox
        product_frame = tk.Frame(list_container, bg="#FFFFFF", bd=2, relief="groove")
        product_frame.pack(fill="both", expand=True, padx=5, pady=5)

        tk.Label(product_frame, text="Danh sách Sản phẩm", bg="#FFFFFF",
                 font=("Arial", 11, "bold")).pack(pady=10)

        self.product_listbox = tk.Listbox(product_frame, width=30, height=15,
                                          font=("Arial", 10), selectbackground="#3498DB",
                                          exportselection=False)
        scroll_product = tk.Scrollbar(product_frame, orient="vertical")
        scroll_product.config(command=self.product_listbox.yview)
        scroll_product.pack(side="right", fill="y")
        self.product_listbox.pack(expand=True, fill="both", padx=10, pady=5)

        for product in self.list_products:
            self.product_listbox.insert(tk.END, f"{product['id']} - {product['ten_sp']}")

        # Input Form
        input_frame = tk.Frame(main_frame, bg="#F5F5F5")
        input_frame.grid(row=1, column=2, columnspan=2, padx=20, pady=10, sticky="nsew")

        # Input fields
        ttk.Label(input_frame, text="Số lượng xuất:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.sl_xuat = ttk.Entry(input_frame, width=25)
        self.sl_xuat.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Ngày xuất:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.ngay_xuat = ttk.Entry(input_frame, width=25)
        self.ngay_xuat.insert(0, datetime.now().strftime("%Y/%m/%d"))
        self.ngay_xuat.grid(row=1, column=1, padx=5, pady=5)

        # Action buttons
        button_frame = tk.Frame(main_frame, bg="#F5F5F5")
        button_frame.grid(row=6, column=0, columnspan=4, pady=20)

        ttk.Button(button_frame, text="Xuất kho", command=self.xuat_kho).pack(side="left", padx=15)
        ttk.Button(button_frame, text="Hủy", command=self.destroy).pack(side="left", padx=15)

        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=2)
        main_frame.rowconfigure(1, weight=1)

    def is_valid_number(self, value, field_name):
        """Kiểm tra giá trị nhập có phải là số nguyên dương"""
        try:
            num = int(value)
            if num <= 0:
                raise ValueError
            return True
        except ValueError:
            messagebox.showerror("Lỗi", f"{field_name} phải là số nguyên dương")
            return False

    def xuat_kho(self):
        """Xử lý sự kiện xuất kho"""
        # Kiểm tra sản phẩm được chọn
        selected_product = self.product_listbox.curselection()

        if not selected_product:
            messagebox.showerror("Lỗi", "Vui lòng chọn sản phẩm")
            return

        # Lấy thông tin đã chọn
        product = self.product_listbox.get(selected_product[0])
        product_id = int(product.split(" - ")[0])

        # Validate số lượng
        if not self.is_valid_number(self.sl_xuat.get(), "Số lượng xuất"):
            return

        # Tạo dữ liệu xuất kho
        data = {
            "id_san_pham": product_id,
            "so_luong_xuat": int(self.sl_xuat.get()),
            "ngay_xuat": self.ngay_xuat.get()
        }

        # Gọi controller xử lý
        try:
            result = self.controller_kho.xuatKhoController(data)
            if result:
                messagebox.showinfo("Thành công", "Xuất kho thành công")
                self.parent.update_table_kiem_kho(self.parent.controller.getAllHistoryController())
                self.destroy()
            else:
                messagebox.showerror("Lỗi", "Xuất kho không thành công")
        except Exception as e:
            messagebox.showerror("Lỗi hệ thống", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    form = XuatKhoForm(root)
    root.mainloop()