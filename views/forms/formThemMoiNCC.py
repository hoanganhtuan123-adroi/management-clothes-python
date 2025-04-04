import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controllers.nhaCungCapController import NhaCungCapController
class ThemNhaCungCapForm:
    def __init__(self, parent):
        self.parent = parent
        self.controller = NhaCungCapController()
        # Tạo cửa sổ Toplevel
        self.top = tk.Toplevel(parent)
        self.top.title("Thêm nhà cung cấp")
        self.top.geometry("500x400")
        self.top.resizable(False, False)
        self.top.transient(parent)  # Đặt cửa sổ này là transient với cửa sổ chính
        self.top.grab_set()  # Đặt trạng thái modal

        self.create_widgets()

    def create_widgets(self):
        # Tạo main frame
        main_frame = tk.Frame(self.top, padx=15, pady=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Tạo frame cho form sử dụng LabelFrame
        form_frame = tk.LabelFrame(main_frame, text="Thêm nhà cung cấp", padx=10, pady=10)
        form_frame.pack(fill=tk.BOTH, expand=True)

        # Tạo các fields
        fields = [
            "Mã nhà cung cấp",
            "Đơn vị cung cấp",
            "Mặt hàng cung cấp",
            "Email",
            "Số điện thoại",
            "Địa chỉ"
        ]

        # Tạo entries để lưu giá trị
        self.entries = {}

        # Tạo grid cho các fields
        for i, label_text in enumerate(fields):
            label = tk.Label(form_frame, text=label_text, anchor=tk.W)
            label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=10)

            entry = tk.Entry(form_frame, width=30)
            entry.grid(row=i, column=1, sticky=tk.W, padx=10, pady=10)

            # Lưu entry vào dictionary để dễ truy cập sau này
            self.entries[label_text] = entry

        # Tạo separator
        separator = ttk.Separator(form_frame, orient=tk.HORIZONTAL)
        separator.grid(row=len(fields), column=0, columnspan=2, sticky=tk.EW, pady=10)

        # Tạo frame cho buttons
        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=len(fields) + 1, column=0, columnspan=2, pady=10)

        # Tạo nút "Thêm mới"
        them_moi_button = tk.Button(
            button_frame,
            text="Thêm mới",
            bg="#00a8e8",
            fg="white",
            padx=20,
            pady=5,
            cursor="hand2",
            command=self.them_moi
        )
        them_moi_button.pack(side=tk.LEFT, padx=10)

        # Tạo nút "Đóng"
        dong_button = tk.Button(
            button_frame,
            text="Đóng",
            bg="#c0c0c0",
            padx=20,
            pady=5,
            cursor="hand2",
            command=self.dong
        )
        dong_button.pack(side=tk.LEFT, padx=10)

    def them_moi(self):
        # Lấy giá trị từ các entry
        values = {field: entry.get() for field, entry in self.entries.items()}
        print("Giá trị nhập vào:")
        result = self.controller.addNewSupplierController(values)
        if result:
            messagebox.showinfo("Thong bao", "Them nha cung cap thanh cong!")
            self.parent.update_treeview()
            self.dong()
        else:
            messagebox.showerror("Thong bao", "Them that bai!")

    def dong(self):
        self.top.destroy()


# Ví dụ sử dụng:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Thêm mới nhà cung cấp")
    root.geometry("300x200")
    root.mainloop()