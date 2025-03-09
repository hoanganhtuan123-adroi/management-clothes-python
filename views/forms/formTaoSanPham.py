import tkinter as tk
from tkinter import ttk, filedialog, PhotoImage, messagebox
from PIL import Image, ImageTk
from ttkthemes import ThemedTk
from controllers.sanPhamController import SanPhamController
import os

class FormTaoSanPham(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Tạo sản phẩm")
        self.geometry("800x700")
        self.configure(bg="white")
        self.resizable(False, False)
        self.controller = SanPhamController()
        self.img_list = []
        # Variables
        self.img_path = None
        self.img_data = None

        self.create_widgets()

        # Center the window
        # self.update_idletasks()
        # width = self.winfo_width()
        # height = self.winfo_height()
        # x = (self.winfo_screenwidth() // 2) - (width // 2)
        # y = (self.winfo_screenheight() // 2) - (height // 2)
        # self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        # Make sure this window stays on top of its parent
        self.transient(parent)
        self.grab_set()

    def create_widgets(self):
        # Main container with padding
        main_frame = tk.Frame(self, padx=20, pady=20, bg="white")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = tk.Label(main_frame, text="Tạo sản phẩm", font=("Arial", 14, "bold"), bg="white")
        title_label.pack(anchor=tk.W, pady=(0, 10))

        # Form container with light border
        form_frame = tk.Frame(main_frame, bg="white", relief=tk.SOLID, borderwidth=1)
        form_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        # Section 1: General Information
        section1_frame = tk.Frame(form_frame, bg="white", padx=10, pady=10)
        section1_frame.pack(fill=tk.X)

        general_label = tk.Label(section1_frame, text="Thông tin chung", font=("Arial", 12), bg="white")
        general_label.pack(anchor=tk.W)

        # Separator line
        separator1 = ttk.Separator(section1_frame, orient='horizontal')
        separator1.pack(fill=tk.X, pady=5)

        # Section 2: Product Details
        section2_frame = tk.Frame(form_frame, bg="white", padx=10, pady=5)
        section2_frame.pack(fill=tk.X)

        # Left column
        left_frame = tk.Frame(section2_frame, bg="white")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Product Name
        name_label = tk.Label(left_frame, text="Tên sản phẩm", bg="white")
        name_label.pack(anchor=tk.W, pady=(5, 2))
        self.name_entry = tk.Entry(left_frame, font=("Arial", 11), bd=1, relief=tk.SOLID)
        self.name_entry.pack(fill=tk.X, pady=(0, 5))

        # Product Code
        code_label = tk.Label(left_frame, text="Mã sản phẩm", bg="white")
        code_label.pack(anchor=tk.W, pady=(5, 2))
        self.code_entry = tk.Entry(left_frame, font=("Arial", 11), bd=1, relief=tk.SOLID)
        self.code_entry.pack(fill=tk.X, pady=(0, 5))

        # Product Category
        category_label = tk.Label(left_frame, text="Loại sản phẩm", bg="white")
        category_label.pack(anchor=tk.W, pady=(5, 2))
        self.category_entry = tk.Entry(left_frame, font=("Arial", 11), bd=1, relief=tk.SOLID)
        self.category_entry.pack(fill=tk.X, pady=(0, 5))

        # Product Description
        desc_label = tk.Label(left_frame, text="Mô tả sản phẩm", bg="white")
        desc_label.pack(anchor=tk.W, pady=(5, 2))

        # Right column
        right_frame = tk.Frame(section2_frame, bg="white")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))

        # Price
        price_label = tk.Label(right_frame, text="Giá bán", bg="white")
        price_label.pack(anchor=tk.W, pady=(5, 2))
        self.price_entry = tk.Entry(right_frame, font=("Arial", 11), bd=1, relief=tk.SOLID)
        self.price_entry.pack(fill=tk.X, pady=(0, 5))

        # Dimensions
        dimensions_label = tk.Label(right_frame, text="Kích thước", bg="white")
        dimensions_label.pack(anchor=tk.W, pady=(5, 2))
        self.dimensions_entry = tk.Entry(right_frame, font=("Arial", 11), bd=1, relief=tk.SOLID)
        self.dimensions_entry.pack(fill=tk.X, pady=(0, 5))

        # Color
        color_label = tk.Label(right_frame, text="Màu sắc", bg="white")
        color_label.pack(anchor=tk.W, pady=(5, 2))
        self.color_entry = tk.Entry(right_frame, font=("Arial", 11), bd=1, relief=tk.SOLID)
        self.color_entry.pack(fill=tk.X, pady=(0, 5))

        # Description Text Area
        desc_frame = tk.Frame(form_frame, bg="white", padx=10, pady=5)
        desc_frame.pack(fill=tk.X)

        self.desc_text = tk.Text(desc_frame, height=5, font=("Arial", 11), bd=1, relief=tk.SOLID)
        self.desc_text.pack(fill=tk.X, pady=(0, 10))

        # Product Image Section
        image_section_frame = tk.Frame(form_frame, bg="white", padx=10, pady=5)
        image_section_frame.pack(fill=tk.X, pady=(0, 10))

        image_section_label = tk.Label(image_section_frame, text="Hình ảnh sản phẩm", bg="white")
        image_section_label.pack(anchor=tk.W, pady=(5, 5))

        # Image Preview Area
        self.image_frame = tk.Frame(image_section_frame, bg="white", width=460, height=100, bd=1, relief=tk.SOLID)
        self.image_frame.pack(fill=tk.X, pady=(0, 10))
        self.image_frame.pack_propagate(False)  # Prevent frame from resizing

        # Add placeholder image and text
        self.image_placeholder = tk.Frame(self.image_frame, bg="white")
        self.image_placeholder.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Placeholder image icon
        # self.placeholder_icon = tk.Label(self.image_placeholder, text="🖼️", font=("Arial", 24), bg="white",
        #                                  fg="#c0c0c0")
        # self.placeholder_icon.pack()
        self.placeholder_icon = PhotoImage(file="assets/img/icon/imageUpload.png")

        # Add image text
        self.add_image_button = tk.Label(self.image_placeholder, image=self.placeholder_icon, compound="top" ,text="Thêm ảnh", font=("Arial", 10),
                                          fg="#38b6ff", bg="white", bd=0, cursor="hand2")
        self.add_image_button.pack()
        self.add_image_button.bind("<Button-1>", self.upload_image)

        # Buttons Section
        button_frame = tk.Frame(main_frame, bg="white", pady=10)
        button_frame.pack(fill=tk.X)

        # Cancel button
        self.cancel_button = tk.Button(button_frame, text="Hủy", font=("Arial", 11),
                                       bg="#c0c0c0", fg="white", bd=0, padx=20, pady=5,
                                       command=self.destroy)
        self.cancel_button.pack(side=tk.LEFT)

        # Add button
        self.add_button = tk.Button(button_frame, text="Thêm mới", font=("Arial", 11),
                                    bg="#38b6ff", fg="white", bd=0, padx=20, pady=5,
                                    command=self.save_product)
        self.add_button.pack(side=tk.RIGHT)

    def upload_image(self, event=None):
        # Open file dialog to select an image
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
        )

        if file_path:
            try:
                # Clear the placeholder
                for widget in self.image_placeholder.winfo_children():
                    widget.destroy()

                # Load and resize the image
                image = Image.open(file_path)
                image = image.resize((50, 50), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)

                # Store the path and photo
                self.img_path = file_path
                self.img_data = photo

                # Create a label to display the image
                img_label = tk.Label(self.image_placeholder, image=photo, bg="white")
                img_label.image = photo  # Keep a reference to avoid garbage collection
                img_label.pack(side="left", anchor="w", padx=10, pady=10)

                # Add remove button
                remove_btn = tk.Button(self.image_placeholder, text="Xóa", fg="red", bg="white", bd=0,
                                       command=self.remove_image)
                remove_btn.pack(side="left", anchor="w", padx=10, pady=10)
                self.img_list.append((img_label, remove_btn))
            except Exception as e:
                print(f"Error loading image: {e}")

    def remove_image(self):
        # Clear the image and reset
        for widget in self.image_placeholder.winfo_children():
            widget.destroy()

        # Reset the image data
        self.img_path = None
        self.img_data = None

        # Add placeholder image icon again
        self.placeholder_icon = tk.Label(self.image_placeholder, text="🖼️", font=("Arial", 24), bg="white",
                                         fg="#c0c0c0")
        self.placeholder_icon.pack()

        # Add image text again
        self.add_image_button = tk.Button(self.image_placeholder, text="Thêm ảnh", font=("Arial", 10),
                                          fg="#38b6ff", bg="white", bd=0, cursor="hand2", command=self.upload_image)
        self.add_image_button.pack()

    def save_product(self):
        # Get all the form data
        product_data = {
            'ten_sp': self.name_entry.get(),
            'ma_sp': self.code_entry.get(),
            'loai_sp': self.category_entry.get(),
            'mo_ta': self.desc_text.get("1.0", tk.END),
            'gia_ban': self.price_entry.get(),
            'kich_thuoc': self.dimensions_entry.get(),
            'mau_sac': self.color_entry.get(),
            'hinh_anh': self.img_path
        }

        # Validate data
        errors = self.validate_data(product_data)
        if len(errors) == 0:
            isSuccess = self.controller.createProductController(product_data)
            if isSuccess:
             messagebox.showinfo("Thông báo", "Thêm sản phẩm thành công!")
             self.parent.reload_data()
             self.destroy()
        else:
            messagebox.showerror("Lỗi", errors[0])


    def validate_data(self, product_data):
        errors = []

        # Validate name_sp (product name)
        if not product_data['ten_sp']:
            errors.append("Mời nhập tên sản phẩm.")

        # Validate ma_sp (product code)
        if not product_data['ma_sp']:
            errors.append("Vui lòng điền mã sản phâm.")

        # Validate loai_sp (product category)
        if not product_data['loai_sp']:
            errors.append("Vui lòng nhập loại sản phẩm.")

        # Validate mo_ta (product description)
        if not product_data['mo_ta'].strip():
            errors.append("Vui lòng nhập mô tả.")

        # Validate gia_ban (price)
        try:
            price = float(product_data['gia_ban'])
            if price <= 0:
                errors.append("Giá sản phẩm không được âm.")
        except ValueError:
            errors.append("Giá sản phẩm phải là số.")

        # Validate kich_thuoc (dimensions)
        if not product_data['kich_thuoc']:
            errors.append("Vui lòng nhập kích thước.")

        # Validate mau_sac (color)
        if not product_data['mau_sac']:
            errors.append("Vui lòng nhập màu sắc.")

        # Validate hinh_anh (image path)
        if not product_data['hinh_anh']:
            errors.append("Vui lòng chọn ảnh sản phẩm.")

        return errors


# Running the application
if __name__ == "__main__":
    root = ThemedTk(theme="arc")  # Using the "arc" theme for rounded corners
    app = FormTaoSanPham(root)
    root.mainloop()
