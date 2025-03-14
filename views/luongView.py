import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from openpyxl import Workbook

class LuongView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Bảng tính lương")
        self.geometry("900x450")
        self.configure(bg="white")

        self.create_table()
        self.load_salary_data(parent.listEmployees)
        self.create_export_button()

    def create_table(self):
        columns = ("ma_nhan_vien", "ho_ten", "he_so_luong", "luong_co_ban", "phu_cap", "thuong", "ngay_cong", "tong")

        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("ma_nhan_vien", text="Mã nhân viên")
        self.tree.heading("ho_ten", text="Họ tên")
        self.tree.heading("he_so_luong", text="Hệ số lương")
        self.tree.heading("luong_co_ban", text="Lương cơ bản")
        self.tree.heading("phu_cap", text="Phụ cấp")
        self.tree.heading("thuong", text="Thưởng")
        self.tree.heading("ngay_cong", text="Ngày công")
        self.tree.heading("tong", text="Tổng lương")

        for col in columns:
            self.tree.column(col, width=120, anchor="center")

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def create_export_button(self):
        button_frame = tk.Frame(self, bg="white")
        button_frame.pack(fill=tk.X, padx=10, pady=10)

        export_button = tk.Button(button_frame, text="Xuất Excel", font=("Arial", 12, "bold"),
                                  bg="#4CAF50", fg="white", padx=10, pady=5, command=self.export_to_excel)
        export_button.pack(side=tk.RIGHT)

    def load_salary_data(self, employees):
        self.salary_data = []

        for item in self.tree.get_children():
            self.tree.delete(item)

        for emp in employees:
            if emp['chuc_vu'].lower() == "trưởng phòng":
                luong_co_ban = 10000000
                he_so_luong = 1.5
            else:
                luong_co_ban = 5000000
                he_so_luong = 1.2

            phu_cap = 0
            thuong = 0
            ngay_cong = 28
            tong_luong = (luong_co_ban * he_so_luong) + phu_cap + thuong

            values = (emp['ma_nhan_vien'], emp['ho_ten'], he_so_luong, luong_co_ban, phu_cap, thuong, ngay_cong, tong_luong)
            self.tree.insert("", tk.END, values=values)
            self.salary_data.append(values)

    def export_to_excel(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                 filetypes=[("Excel Files", "*.xlsx")],
                                                 title="Lưu file Excel")

        if not file_path:
            return

        wb = Workbook()
        ws = wb.active
        ws.title = "Bảng lương nhân viên"

        headers = ["Mã nhân viên", "Họ Tên", "Hệ số lương", "Lương cơ bản", "Phụ cấp", "Thưởng", "Ngày công", "Tổng lương"]
        ws.append(headers)

        for row in self.salary_data:
            ws.append(row)

        wb.save(file_path)
        tk.messagebox.showinfo("Thành công", "Xuất file Excel thành công!")

