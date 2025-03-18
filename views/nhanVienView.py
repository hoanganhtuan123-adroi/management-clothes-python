import tkinter as tk
from tkinter import ttk
import ast
from controllers.nhanVienController import NhanVienController  # Update to your employee controller
from views.forms.formTaoNhanVien import FormTaoNhanVien  # Update form for creating an employee
from views.forms.formTTNhanVien import FormTTNhanVien  # Update form for employee details
from views.luongView import LuongView


class NhanVienFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.controller = NhanVienController()  # Employee controller
        self.listEmployees = self.getAllEmployees()

        # Frame chứa tiêu đề và nút "Tạo nhân viên"
        header_frame = tk.Frame(self, bg="white")
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        # Tiêu đề "Danh sách nhân viên"
        label = tk.Label(header_frame, text="Danh sách nhân viên", font=("Arial", 16, "bold"), bg="white")
        label.pack(side=tk.LEFT)

        # Nút "Tạo nhân viên"
        create_button = tk.Button(header_frame, text=" Tạo nhân viên", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=10, pady=5, command=self.createEmployee)
        create_button.pack(side=tk.RIGHT)

        # Tạo thanh tìm kiếm và nút tìm kiếm
        search_frame = tk.Frame(self, bg="white")
        search_frame.pack(fill=tk.X, padx=10, pady=10)

        # Thanh tìm kiếm
        self.search_entry = tk.Entry(search_frame, font=("Arial", 12), fg="gray", borderwidth=1, relief='solid',
                                     bg="white")
        self.search_entry.insert(0, "Tìm kiếm theo tên, số điện thoại, email")  # Placeholder text
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5, ipady=5, ipadx=10)

        # Nút tìm kiếm
        search_button = tk.Button(search_frame, text="Tìm kiếm", font=("Arial", 12, "bold"),
                                  bg="#38b6ff", fg="white", bd=0, padx=20, pady=5, command=self.search_employees)
        search_button.pack(side=tk.RIGHT)

        # Tìm kiếm nhân viên
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

        columns = ("ma_nhan_vien", "ho_ten", "email", "chuc_vu", "dien_thoai")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("ma_nhan_vien", text="Mã nhân viên")
        self.tree.heading("ho_ten", text="Họ tên")
        self.tree.heading("email", text="Email")
        self.tree.heading("chuc_vu", text="Chức vụ")
        self.tree.heading("dien_thoai", text="Số điện thoại")

        self.tree.column("ma_nhan_vien", width=150, anchor="w")
        self.tree.column("ho_ten", width=200, anchor="w")
        self.tree.column("email", width=200, anchor="w")
        self.tree.column("chuc_vu", width=150, anchor="w")
        self.tree.column("dien_thoai", width=150, anchor="w")

        # Tạo menu chuột phải
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Xem thông tin", command=self.show_selected_employee)

        # Gán sự kiện chuột phải
        self.tree.bind("<Button-3>", self.on_right_click)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.update_treeview(self.listEmployees)
        self.tree.bind("<Double-Button-1>", self.on_row_select)

        # Thêm nút "Bảng tính lương"
        salary_button = tk.Button(header_frame, text="Bảng tính lương", font=("Arial", 12, "bold"),
                                  bg="#ff914d", fg="white", bd=0, padx=10, pady=5, command=self.show_salary_view)
        salary_button.pack(side=tk.RIGHT, padx=(10, 0))

    def show_salary_view(self):
        LuongView(self)

    def on_right_click(self, event):
        selected_item = self.tree.identify_row(event.y)
        if selected_item:
            self.tree.selection_set(selected_item)
            self.context_menu.post(event.x_root, event.y_root)

    def show_selected_employee(self):
        selected_item = self.tree.selection()[0]
        row_data = self.tree.item(selected_item)["tags"][0]
        FormTTNhanVien(self, employee_data=row_data)

    def update_treeview(self, employees):
        for item in self.tree.get_children():
            self.tree.delete(item)

        if employees:
            for row in employees:
                values = (
                    row['ma_nhan_vien'],
                    row['ho_ten'],
                    row['email'],
                    row['chuc_vu'],
                    row['dien_thoai']
                )
                self.tree.insert("", tk.END, values=values, tags=(row))
        else:
            self.tree.insert("", tk.END, values=["Không có nhân viên", "", "", "", ""])

    def search_employees(self):
        query = self.search_entry.get().lower()
        filtered_employees = [employee for employee in self.listEmployees if
                              query in employee['ho_ten'].lower() or
                              query in employee['dien_thoai'] or
                              query in employee['email'].lower()]

        if filtered_employees:
            self.update_treeview(filtered_employees)
        else:
            self.update_treeview([])

    def reload_data(self):
        self.listEmployees = self.getAllEmployees()
        self.update_treeview(self.listEmployees)

    def getAllEmployees(self):
        listEmployees = self.controller.getAllEmployeesController()
        return listEmployees

    def createEmployee(self):
        FormTaoNhanVien(self)

    def on_row_select(self, event):
        selected_item = self.tree.selection()[0]
        row_data = self.tree.item(selected_item)["tags"][0]
        id = self.extract_id_from_string(row_data)
        print("Check row data : ", id)
        FormTTNhanVien(self, id)

    def extract_id_from_string(self,raw_string):
        try:
            if not raw_string.startswith("{"):
                raw_string = "{" + raw_string + "}"

            data = ast.literal_eval(raw_string)

            # Lấy giá trị của 'id'
            if 'id' in data:
                return data['id']
            else:
                raise Exception("Không tìm thấy khóa 'id' trong chuỗi")

        except (SyntaxError, ValueError) as e:
            raise Exception(f"Không thể chuyển đổi chuỗi thành dictionary: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x600")
    app = NhanVienFrame(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
