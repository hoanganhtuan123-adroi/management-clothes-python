import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from config.commonDef import CommonDef
from controllers.sanPhamController import SanPhamController
class ProductForm(tk.Toplevel):
    def __init__(self, parent, product_data=None):
        super().__init__(parent)
        self.commonDef = CommonDef()
        self.controller = SanPhamController()
        self.img_list = []
        # Xử lý chuỗi row_data thành từ điển
        if isinstance(product_data, str):
            # Thay thế Decimal(...) thành giá trị số thực
            product_data = product_data.replace("Decimal('", "").replace("')", "")
            # Chuyển chuỗi thành từ điển bằng eval (cẩn thận với eval)
            try:
                self.product_data = eval('{' + product_data + '}')
            except Exception as e:
                print(f"Error parsing row_data: {e}")
                self.product_data = {}
        else:
            self.product_data = product_data or {}

        # Chuẩn hóa key để khớp với render_data
        self.product_data = {
            "id": self.product_data.get("id",0),
            "ten_san_pham": self.product_data.get("ten_sp", ""),
            "ma_san_pham": self.product_data.get("ma_sp", ""),
            "loai_san_pham": self.product_data.get("loai_san_pham", ""),
            "gia_ban": str(self.product_data.get("gia_ban", "")),  # Chuyển Decimal thành string
            "mau_sac": self.product_data.get("mau_sac", ""),  # Dữ liệu không có, mặc định 0
            "kich_thuoc": self.product_data.get("kich_thuoc", "S, M, L"),
            "mo_ta": self.product_data.get("mo_ta", ""),
            "hinh_anh": self.product_data.get("hinh_anh").split(", ") if self.product_data.get("hinh_anh") else []
        }

        # Thiết lập cửa sổ con
        self.title("Thông tin sản phẩm")
        self.geometry("700x800")
        self.configure(bg="#f0f4f8")
        self.transient(parent)
        self.grab_set()

        # Tạo giao diện và lưu trữ các widget cần cập nhật dữ liệu
        self.create_form()
        # Đổ dữ liệu vào giao diện
        self.render_data()

    def create_form(self):
        # Tiêu đề
        title_frame = tk.Frame(self, bg="#f0f4f8", pady=10)
        title_frame.pack(fill="x")
        title_label = tk.Label(title_frame, text="Váy Quý Đại", font=("Helvetica", 18, "bold"), fg="#2c3e50", bg="#f0f4f8")
        title_label.pack()

        # Frame chính với viền
        main_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="groove", padx=20, pady=20)
        main_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Frame chứa thông tin chung
        info_frame = tk.Frame(main_frame, bg="#ffffff")
        info_frame.pack(fill="x", pady=10)

        # Tên sản phẩm
        tk.Label(info_frame, text="Tên sản phẩm: ", font=("Helvetica", 12), fg="#34495e", bg="#ffffff").grid(row=0,
                                                                                                             column=0,
                                                                                                             sticky="w",
                                                                                                             pady=5)
        self.ten_san_pham_entry = tk.Entry(info_frame, font=("Helvetica", 12), width=20)
        self.ten_san_pham_entry.grid(row=0, column=1, sticky="w", pady=5)

        # Mã sản phẩm
        tk.Label(info_frame, text="Mã sản phẩm: ", font=("Helvetica", 12), fg="#34495e", bg="#ffffff").grid(row=1,
                                                                                                            column=0,
                                                                                                            sticky="w",
                                                                                                            pady=5)
        self.ma_san_pham_entry = tk.Entry(info_frame, font=("Helvetica", 12), width=20)
        self.ma_san_pham_entry.grid(row=1, column=1, sticky="w", pady=5)

        # Loại sản phẩm
        tk.Label(info_frame, text="Loại sản phẩm: ", font=("Helvetica", 12), fg="#34495e", bg="#ffffff").grid(row=2,
                                                                                                              column=0,
                                                                                                              sticky="w",
                                                                                                              pady=5)
        self.loai_san_pham_entry = tk.Entry(info_frame, font=("Helvetica", 12), width=20)
        self.loai_san_pham_entry.grid(row=2, column=1, sticky="w", pady=5)

        # Giá bán
        tk.Label(info_frame, text="Giá bán: ", font=("Helvetica", 12), fg="#34495e", bg="#ffffff").grid(row=0, column=3,
                                                                                                        sticky="w",
                                                                                                        padx=50, pady=5)
        self.gia_ban_entry = tk.Entry(info_frame, font=("Helvetica", 12), width=20)
        self.gia_ban_entry.grid(row=0, column=4, sticky="w", padx=5, pady=5)

        # Màu sắc
        tk.Label(info_frame, text="Màu sắc: ", font=("Helvetica", 12), fg="#34495e", bg="#ffffff").grid(row=1, column=3,
                                                                                                        sticky="w",
                                                                                                        padx=50, pady=5)
        self.mau_sac_entry = tk.Entry(info_frame, font=("Helvetica", 12), width=20)
        self.mau_sac_entry.grid(row=1, column=4, sticky="w", padx=5, pady=5)

        # Kích thước
        tk.Label(info_frame, text="Kích thước: ", font=("Helvetica", 12), fg="#34495e", bg="#ffffff").grid(row=2,
                                                                                                           column=3,
                                                                                                           sticky="w",
                                                                                                           padx=50,
                                                                                                           pady=5)
        self.kich_thuoc_entry = tk.Entry(info_frame, font=("Helvetica", 12), width=20)
        self.kich_thuoc_entry.grid(row=2, column=4, sticky="w", padx=5, pady=5)

        # Mô tả sản phẩm
        desc_frame = tk.Frame(main_frame, bg="#ffffff")
        desc_frame.pack(fill="x", pady=10)
        tk.Label(desc_frame, text="Mô tả sản phẩm", font=("Helvetica", 12, "bold"), fg="#2c3e50", bg="#ffffff").pack(
            anchor="w", pady=5)
        self.desc_text = tk.Text(desc_frame, font=("Helvetica", 11), width=60, height=5, wrap="word")
        self.desc_text.pack(anchor="w", padx=10, pady=5)

        # Hình ảnh sản phẩm
        image_frame = tk.Frame(main_frame, bg="#ffffff")
        image_frame.pack(fill="x", pady=10)
        tk.Label(image_frame, text="Hình ảnh sản phẩm", font=("Helvetica", 12, "bold"), fg="#2c3e50", bg="#ffffff").pack(anchor="w", pady=5)

        # Frame chứa hình ảnh
        self.img_container = tk.Frame(image_frame, bg="#ffffff")
        self.img_container.pack(fill="x", pady=5)

        # Nút chức năng
        button_frame = tk.Frame(main_frame, bg="#ffffff")
        button_frame.pack(pady=20)
        # Nút xóa
        delete_btn = tk.Button(button_frame, text="Xóa", font=("Helvetica", 12), bg="#e74c3c", fg="white", activebackground="#c0392b", width=10, command=lambda: self.delete_product(self.product_data["id"]))
        delete_btn.pack(side="left", padx=10)
        delete_btn.bind("<Enter>", lambda e: delete_btn.config(bg="#c0392b"))
        delete_btn.bind("<Leave>", lambda e: delete_btn.config(bg="#e74c3c"))
        # Nút cập nhập
        update_btn = tk.Button(button_frame, text="Cập nhật", font=("Helvetica", 12), bg="#3498db", fg="white", activebackground="#2980b9", width=10, command=self.update_data)
        update_btn.pack(side="left", padx=10)
        update_btn.bind("<Enter>", lambda e: update_btn.config(bg="#2980b9"))
        update_btn.bind("<Leave>", lambda e: update_btn.config(bg="#3498db"))

        # Nút tải ảnh
        self.upload_button = tk.Button(image_frame, text="Tài ảnh", font=("Helvetica", 12), bg="#3498db", fg="white", activebackground="#2980b9", width=10, command=self.upload_image)
        self.upload_button.pack(side="bottom", padx=10, pady=10)

    def render_data(self):
        # Xóa dữ liệu cũ trong các Entry
        self.ten_san_pham_entry.delete(0, tk.END)
        self.ma_san_pham_entry.delete(0, tk.END)
        self.loai_san_pham_entry.delete(0, tk.END)
        self.gia_ban_entry.delete(0, tk.END)
        self.mau_sac_entry.delete(0, tk.END)
        self.kich_thuoc_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)

        # Chèn dữ liệu mới từ product_data vào các Entry
        self.ten_san_pham_entry.insert(0, self.product_data["ten_san_pham"])
        self.ma_san_pham_entry.insert(0, self.product_data["ma_san_pham"])
        self.loai_san_pham_entry.insert(0, self.product_data["loai_san_pham"])
        gia_ban = self.product_data["gia_ban"]
        self.gia_ban_entry.insert(0, self.commonDef.format_number(gia_ban))
        self.mau_sac_entry.insert(0, self.product_data["mau_sac"])
        self.kich_thuoc_entry.insert(0, self.product_data["kich_thuoc"])
        self.desc_text.insert("1.0", self.product_data["mo_ta"])

        # Xóa các hình ảnh cũ trong img_container
        for widget in self.img_container.winfo_children():
            widget.destroy()

        # Tải và hiển thị hình ảnh mới
        image_paths = self.product_data["hinh_anh"]
        try:
            for path in image_paths:
                image = Image.open(path)
                image = image.resize((150, 200), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                img_label = tk.Label(self.img_container, image=photo, bg="#ffffff")
                img_label.image = photo  # Giữ tham chiếu
                img_label.pack(side="left", padx=5)
                remove_btn = tk.Button(self.img_container, text="Xóa", fg="red", bg="white", bd=0,
                                       command=lambda p=path: self.remove_image(p))
                remove_btn.pack(side="left", padx=5)
                self.img_list.append((img_label, remove_btn, photo, path))
        except (FileNotFoundError, IndexError):
            tk.Label(self.img_container, text="Hình ảnh không tải được", font=("Helvetica", 11), fg="#e74c3c",
                     bg="#ffffff").pack()

    def delete_product(self, id):
        if  id != None and id != "":
           isConfirm = messagebox.askyesno("Xóa", "Bạn có chắc muốn xóa sản phẩm này?", parent=self.master)
           if isConfirm:
               isDeleted = self.controller.deleteProductController(id)
               if isDeleted:
                 messagebox.showinfo("Thành công", "Xóa sản phẩm thành công.")
                 self.destroy()
               else:
                 messagebox.showerror("Lỗi", "Xóa sản phẩm thất bại.")

    def upload_image(self, event=None):
        # Giới hạn tối đa 3 ảnh
        if len(self.img_list) >= 3:
            messagebox.showwarning("Cảnh báo", "Bạn chỉ có thể tải lên tối đa 3 ảnh!")
            return

        # Mở hộp thoại chọn file ảnh
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
        )

        if file_path:
            try:
                # Tải và thay đổi kích thước ảnh
                image = Image.open(file_path)
                image = image.resize((150, 200), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)

                # Tạo label hiển thị ảnh
                img_label = tk.Label(self.img_container, image=photo, bg="#ffffff")
                img_label.image = photo  # Giữ tham chiếu
                img_label.pack(side="left", padx=5)

                # Thêm nút xóa
                remove_btn = tk.Button(self.img_container, text="Xóa", fg="red", bg="white", bd=0,
                                       command=lambda p=file_path: self.remove_image(p))
                remove_btn.pack(side="left", padx=5)

                # Thêm vào danh sách
                self.img_list.append((img_label, remove_btn, photo, file_path))

            except Exception as e:
                print(f"Error loading image: {e}")

    def remove_image(self, path):
        # Xóa ảnh cụ thể dựa trên path
        for img_label, remove_btn, photo, img_path in self.img_list:
            if img_path == path:
                img_label.destroy()
                remove_btn.destroy()
                self.img_list.remove((img_label, remove_btn, photo, img_path))
                break

    def update_data(self):
        list_img = []
        for img_path in self.img_list:
           list_img.append(img_path[3])
        data_update = {
            "id": self.product_data["id"],
            "ten_sp": self.ten_san_pham_entry.get(),
            "ma_sp": self.ma_san_pham_entry.get(),
            "mo_ta": self.desc_text.get("1.0", tk.END),
            "loai_sp": self.loai_san_pham_entry.get(),
            "gia_ban": self.gia_ban_entry.get(),
            "hinh_anh": list_img,
            "kich_thuoc": self.kich_thuoc_entry.get(),
            "mau_sac": self.mau_sac_entry.get()
        }
        isUpdated = self.controller.updateProductController(data_update)
        if isUpdated:
            messagebox.showinfo("Thành công", "Sửa thống tin sản phẩm thành công.")
            self.destroy()
        else:
            messagebox.showerror("Lỗi", "Sửa thống tin sản phẩm thất bại.")


# Ví dụ cách sử dụng

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductForm(root)
    root.mainloop()