import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from controllers.sanPhamController import SanPhamController
from controllers.khoHangController import KhoHangController
class NhapKhoForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Quản lý Nhập Kho")
        self.geometry("1200x700")
        self.configure(bg="#F5F5F5")
        self.contrller_khohang = KhoHangController()
        self.controller_product = SanPhamController()
        self.list_products = self.controller_product.getProductsController()
        self.list_suppliers = self.contrller_khohang.getAllSponsersController()

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
        tk.Label(main_frame, text="NHẬP KHO HÀNG", font=("Arial", 16, "bold"),
                 bg="#F5F5F5", fg="#2C3E50").grid(row=0, column=0, columnspan=4, pady=15, sticky="w")

        # Danh sách sản phẩm và nhà cung cấp
        list_container = tk.Frame(main_frame, bg="#F5F5F5")
        list_container.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # Product Listbox
        product_frame = tk.Frame(list_container, bg="#FFFFFF", bd=2, relief="groove")
        product_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        tk.Label(product_frame, text="Danh sách Sản phẩm", bg="#FFFFFF",
                 font=("Arial", 11, "bold")).pack(pady=10)

        self.product_listbox = tk.Listbox(product_frame, width=30, height=15,
                                          font=("Arial", 10), selectbackground="#3498DB", exportselection=False)
        scroll_product = tk.Scrollbar(product_frame, orient="vertical")
        scroll_product.config(command=self.product_listbox.yview)
        scroll_product.pack(side="right", fill="y")
        self.product_listbox.pack(expand=True, fill="both", padx=10, pady=5, )


        for product in self.list_products:
            self.product_listbox.insert(tk.END, f"{product['id']} - {product['ten_sp']}")

        # Supplier Listbox
        supplier_frame = tk.Frame(list_container, bg="#FFFFFF", bd=2, relief="groove")
        supplier_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        tk.Label(supplier_frame, text="Danh sách Nhà cung cấp", bg="#FFFFFF",
                 font=("Arial", 11, "bold")).pack(pady=10)

        self.supplier_listbox = tk.Listbox(supplier_frame, width=30, height=15,
                                           font=("Arial", 10), selectbackground="#2ecc71", exportselection=False)
        scroll_supplier = tk.Scrollbar(supplier_frame, orient="vertical")
        scroll_supplier.config(command=self.supplier_listbox.yview)
        scroll_supplier.pack(side="right", fill="y")
        self.supplier_listbox.pack(expand=True, fill="both", padx=10, pady=5, )


        for supplier in self.list_suppliers:
            self.supplier_listbox.insert(tk.END, f"{supplier[0]} - {supplier[1]}")

        # Input Form
        input_frame = tk.Frame(main_frame, bg="#F5F5F5")
        input_frame.grid(row=1, column=2, columnspan=2, padx=20, pady=10, sticky="nsew")

        # Input fields
        ttk.Label(input_frame, text="Số lượng nhập:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.sl_nhap = ttk.Entry(input_frame, width=25)
        self.sl_nhap.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Giá nhập (đ):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.gia_nhap = ttk.Entry(input_frame, width=25)
        self.gia_nhap.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Số lượng tồn kho:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.sl_ton = ttk.Entry(input_frame, width=25)
        self.sl_ton.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Ngày nhập:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.ngay_nhap = ttk.Entry(input_frame, width=25)
        self.ngay_nhap.insert(0, datetime.now().strftime("%Y/%m/%d"))
        self.ngay_nhap.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Số lượng bán ra:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.sl_ban = ttk.Entry(input_frame, width=25)
        self.sl_ban.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Giá bán:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.gia_ban = ttk.Entry(input_frame, width=25)
        self.gia_ban.grid(row=5, column=1, padx=5, pady=5)

        # Action buttons
        button_frame = tk.Frame(main_frame, bg="#F5F5F5")
        button_frame.grid(row=6, column=0, columnspan=4, pady=20)

        ttk.Button(button_frame, text="Nhập kho", command=self.nhap_kho).pack(side="left", padx=15)
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

    def extract_number(self,text):
        try:
            number_part = text.split(' - ')[0].strip()
            return int(number_part)
        except (IndexError, ValueError) as e:
            return None

    def nhap_kho(self):
        """Xử lý sự kiện nhập kho"""
        # Kiểm tra sản phẩm và nhà cung cấp được chọn
        selected_product = self.product_listbox.curselection()
        selected_supplier = self.supplier_listbox.curselection()

        if not selected_product:
            messagebox.showerror("Lỗi", "Vui lòng chọn sản phẩm")
            return
        if not selected_supplier:
            messagebox.showerror("Lỗi", "Vui lòng chọn nhà cung cấp")
            return

        # Lấy thông tin đã chọn
        product = self.product_listbox.get(selected_product[0])
        supplier = self.supplier_listbox.get(selected_supplier[0])

        # Lấy các giá trị từ form
        data = {
            "id_san_pham": int(self.extract_number(product)), # id san pham
            "id_nha_cung_cap": int(supplier[0]), #id nha cung cap
            "sl_nhap": int(self.sl_nhap.get()),
            "gia_nhap": float(self.gia_nhap.get()),
            "sl_ton": int(self.sl_ton.get()),
            "ngay_nhap": self.ngay_nhap.get(),
            "sl_ban": int(self.sl_ban.get()),
            "gia_ban": int(self.gia_ban.get())
        }

        result_inserted = self.contrller_khohang.insertHistoryStockController(data)
        if result_inserted:
            messagebox.showinfo("Thành công", "Nhập kho thanh cong")
            self.parent.update_table_kiem_kho(self.parent.controller.getAllHistoryController())
            self.destroy()
        else:
            messagebox.showerror("Lỗi", "Nhập kho khong thanh cong")

        # Hiển thị thông tin
        info_message = (
            "Thông tin nhập kho:\n\n"
            f"Sản phẩm: {data['id_san_pham']}\n"
            f"Nhà cung cấp: {data['id_nha_cung_cap']}\n"
            f"Số lượng nhập: {data['sl_nhap']}\n"
            f"Giá nhập: {data['gia_nhap']} đ\n"
            f"Số lượng tồn: {data['sl_ton']}\n"
            f"Ngày nhập: {data['ngay_nhap']}\n"
            f"Số lượng bán: {data['sl_ban']}\n"
            f"Lô hàng: {data['lo_hang']}"
        )

        messagebox.showinfo("Thành công", info_message)
        self.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    form = NhapKhoForm(root)
    root.mainloop()