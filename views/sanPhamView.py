import tkinter as tk
from tkinter import ttk
from controllers.sanPhamController import SanPhamController
from views.forms.formTaoSanPham import FormTaoSanPham
from views.forms.formTTSanPham import ProductForm
class SanPhamFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.controller = SanPhamController()
        self.list_products = self.getProducts()
        # Frame chứa tiêu đề và nút "Tạo khách hàng"
        header_frame = tk.Frame(self, bg="white")
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        # Tiêu đề "Danh sách khách hàng"
        label = tk.Label(header_frame, text="Danh sách sản phẩm", font=("Arial", 16, "bold"), bg="white")
        label.pack(side=tk.LEFT)

        # Nút "Tạo sản phẩm
        create_button = tk.Button(header_frame, text=" Thêm sản phẩm", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=10, pady=5, command=self.createProduct)
        create_button.pack(side=tk.RIGHT)

        # Tạo thanh tìm kiếm và nút tìm kiếm
        search_frame = tk.Frame(self, bg="white")
        search_frame.pack(fill=tk.X, padx=10, pady=10)

        # Thanh tìm kiếm
        self.search_entry = tk.Entry(search_frame, font=("Arial", 12), fg="gray", borderwidth=1, relief='solid',
                                     bg="white")
        self.search_entry.insert(0, "Tìm kiếm theo tên, mã sản phẩm")  # Placeholder text
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5, ipady=5, ipadx=10)

        # Nút tìm kiếm
        search_button = tk.Button(search_frame, text="Tìm kiếm", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5, command=self.search_products)
        search_button.pack(side=tk.RIGHT)

        # Tìm kiếm khách hàng
        style = ttk.Style()
        style.configure("Treeview",
                        font=("Arial", 12),
                        rowheight=30,  # Chiều cao mỗi dòng
                        borderwidth=1,
                        relief="solid", padding=(5, 5))
        style.configure("Treeview.Heading",
                        font=("Arial", 12, "bold"),
                        background="#f0f0f0",
                        foreground="black")

        columns = ("ma_san_pham", "ten_san_pham", "gia_ban", "kich_thuoc")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("ma_san_pham", text="Mã sản phẩm")
        self.tree.heading("ten_san_pham", text="Tên sản phẩm")
        self.tree.heading("gia_ban", text="Giá bán (VND)")
        self.tree.heading("kich_thuoc", text="Kích thước")

        self.tree.column("ma_san_pham", width=200, anchor="w")
        self.tree.column("ten_san_pham", width=250, anchor="w")
        self.tree.column("gia_ban", width=150, anchor="w")
        self.tree.column("kich_thuoc", width=150, anchor="w")

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.update_treeview(self.list_products)
        self.tree.bind("<Double-Button-1>", self.on_row_select)

    def getProducts(self):
        products = self.controller.getProductsController()
        return products

    def update_treeview(self, products):
        for item in self.tree.get_children():
            self.tree.delete(item)

        if products:
            for row in products:
                values = (
                    row['ma_sp'],
                    row['ten_sp'],
                    "{:,.0f} VND".format(row['gia_ban']),
                    row['kich_thuoc'],
                )
                self.tree.insert("", tk.END, values=values, tags=(row))
        else:
            self.tree.insert("", tk.END, values=["Không có sản phẩm", "", "", ""])

    def reload_data(self):
        # Reload the data
        self.list_products = self.getProducts()
        self.update_treeview(self.list_products)

    def on_row_select(self, event):
        # Get selected row data
        selected_item = self.tree.selection()[0]
        row_data = self.tree.item(selected_item)["tags"][0]
        ProductForm(self, row_data)

    def search_products(self):
        query = self.search_entry.get().lower()
        # Filter the customers based on the query
        filtered_product = [product for product in self.list_products if
                              query in product['ten_sp'].lower() or
                              query in product['ma_sp'].lower()]

        if filtered_product:
            # If customers are found, update the treeview with the filtered list
            self.update_treeview(filtered_product)
        else:
            # If no customers are found, show a "No customers found" message
            self.update_treeview([])

    def createProduct(self):
        FormTaoSanPham(self)
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x600")
    app = SanPhamFrame(root, None)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()