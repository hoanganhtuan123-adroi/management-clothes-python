import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from controllers.khachHangController import KhachHangController
from views.forms.formTaoKhachHang import FormTaoKhachHang
from views.forms.formTTKhacHang import FormTTKhachHang
class KhachHangFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.controller = KhachHangController()
        self.listCustomers = self.getAllCustomers()
        # Frame chứa tiêu đề và nút "Tạo khách hàng"
        header_frame = tk.Frame(self, bg="white")
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        # Tiêu đề "Danh sách khách hàng"
        label = tk.Label(header_frame, text="Danh sách khách hàng", font=("Arial", 16, "bold"), bg="white")
        label.pack(side=tk.LEFT)

        # Nút "Tạo khách hàng"
        create_button = tk.Button(header_frame, text=" Tạo khách hàng", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=10, pady=5, command=self.createCustomer)
        create_button.pack(side=tk.RIGHT)

        # Tạo thanh tìm kiếm và nút tìm kiếm
        search_frame = tk.Frame(self, bg="white")
        search_frame.pack(fill=tk.X, padx=10, pady=10)

        # Thanh tìm kiếm
        self.search_entry = tk.Entry( search_frame, font=("Arial", 12), fg="gray",borderwidth=1, relief='solid', bg="white")
        self.search_entry.insert(0, "Tìm kiếm theo tên, số điện thoại, email")  # Placeholder text
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5, ipady=5, ipadx=10)

        # Nút tìm kiếm
        search_button = tk.Button(search_frame, text="Tìm kiếm", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5, command=self.search_customers)
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

        columns = ("khach_hang", "dien_thoai", "dia_chi", "email", "gioi_tinh")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("khach_hang", text="Khách hàng")
        self.tree.heading("dien_thoai", text="Điện thoại")
        self.tree.heading("dia_chi", text="Địa chỉ")
        self.tree.heading("email", text="Email")
        self.tree.heading("gioi_tinh", text="Giới tính")

        self.tree.column("khach_hang", width=200, anchor="w")
        self.tree.column("dien_thoai", width=150, anchor="w")
        self.tree.column("dia_chi", width=200, anchor="w")
        self.tree.column("email", width=200, anchor="w")
        self.tree.column("gioi_tinh", width=100, anchor="w")

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.tree.bind("<Double-Button-1>", self.on_row_select)
        self.update_treeview()


    def update_treeview(self, listCustomers=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        if listCustomers is None:
           listCustomers = self.controller.getAllCustomersController()

        if listCustomers:
            for row in listCustomers:
                values = (
                    row['hoten'],  # Khách hàng
                    row['sdt'],  # Điện thoại
                    row['diachi'],  # Địa chỉ
                    row['email'],  # Email
                    row['gioitinh']  # Giới tính
                )
                self.tree.insert("", tk.END, values=values, tags=(row))
        else:
            self.tree.insert("", tk.END, values=["Không có khách hàng", "", "", "", ""])

    def search_customers(self):
        query = self.search_entry.get().lower()
        # Filter the customers based on the query
        filtered_customers = [customer for customer in self.listCustomers if
                              query in customer['hoten'].lower() or
                              query in customer['sdt'] or
                              query in customer['email'].lower()]

        if filtered_customers:
            # If customers are found, update the treeview with the filtered list
            self.update_treeview(filtered_customers)
        else:
            # If no customers are found, show a "No customers found" message
            self.update_treeview([])

    def getAllCustomers(self):
        listCustomers = self.controller.getAllCustomersController()
        print("Danh sách khách hàng:", listCustomers)  # Debug dữ liệu trả về
        return listCustomers

    def createCustomer(self):
        FormTaoKhachHang(self)

    def on_row_select(self, event):
        # Get selected row data
        selected_item = self.tree.selection()
        if selected_item:
            selected_item = self.tree.selection()[0]
            row_data = self.tree.item(selected_item)["tags"][0]
            print("Row data parent:", row_data)
            FormTTKhachHang(self, customer_data=row_data)
        else:
            print("No item selected")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x600")
    app = KhachHangFrame(root, None)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()