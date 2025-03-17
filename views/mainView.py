import tkinter as tk
from tkinter import PhotoImage
from views.khachHangView import KhachHangFrame
from views.sanPhamView import SanPhamFrame
from views.donHangView import DonHangFrame
from views.khoHangView import KhoHangFrame
from views.nhanVienView import NhanVienFrame
from views.nhaCungCapView import NhaCungCapFrame
from views.baoCaoView import BaoCaoFrame
from views.phanQuyenView import PhanQuyenFrame
class MainView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Giao diện chính")
        self.geometry("1100x1000")

        # SIDEBAR bên trái
        self.sidebar_frame = tk.Frame(self, bg="#f0f0f0", width=200, padx=10, pady=10)
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.selected_button = None
        # Các nút menu
        self.khach_hang_icon = PhotoImage(file="assets/img/icon/iconKhachHang.png")
        self.khach_hang_icon_selected = PhotoImage(file="assets/img/iconSelected/iconKHColor.png")
        self.btn_khach_hang = tk.Button(self.sidebar_frame,text="  Khách hàng",
                                        image=self.khach_hang_icon, compound='left',
                                        anchor='w', borderwidth=0, font=("Arial", 14, "bold"),
                                        command=lambda: self.select_button("khach_hang","KhachHangFrame"))
        self.btn_khach_hang.pack(fill=tk.X, padx=10, pady=5)

        # Nút sản phẩm
        self.san_pham_icon = PhotoImage(file="assets/img/icon/iconSanPham.png")
        self.san_pham_icon_selected = PhotoImage(file="assets/img/iconSelected/iconSanPhamColor.png")
        self.btn_san_pham = tk.Button(self.sidebar_frame, text="  Sản phẩm", image=self.san_pham_icon, compound='left',anchor='w',borderwidth=0, font=("Arial", 14, "bold"),
                                      command=lambda: self.select_button("san_pham","SanPhamFrame"))
        self.btn_san_pham.pack(fill=tk.X, padx=10, pady=5)

        # Nút đơn hàng
        self.don_hang_icon = PhotoImage(file="assets/img/icon/iconDonHang.png")
        self.don_hang_icon_selected = PhotoImage(file="assets/img/iconSelected/iconDonHangColor.png")
        self.btn_don_hang = tk.Button(self.sidebar_frame, text="  Đơn hàng", borderwidth=0, image=self.don_hang_icon, compound='left',anchor='w',
                                      font=("Arial", 14, "bold"),command=lambda: self.select_button("don_hang","DonHangFrame"))
        self.btn_don_hang.pack(fill=tk.X, padx=10, pady=5)

        # Nút Kho Hàng
        self.kho_hang_icon = PhotoImage(file="assets/img/icon/iconKhoHang.png")
        self.kho_hang_icon_selected = PhotoImage(file="assets/img/iconSelected/iconKhoHangColor.png")
        self.btn_kho_hang = tk.Button(self.sidebar_frame, text="  Kho hàng", image=self.kho_hang_icon, compound='left',
                                      anchor='w', borderwidth=0,
                                      font=("Arial", 14, "bold"),command=lambda: self.select_button("kho_hang","KhoHangFrame"))
        self.btn_kho_hang.pack(fill=tk.X, padx=10, pady=5)

        # Nút Nhân Viên
        self.nhan_vien_icon = PhotoImage(file="assets/img/icon/iconKhachHang.png")
        self.nhan_vien_icon_selected = PhotoImage(file="assets/img/iconSelected/iconKHColor.png")
        self.btn_nhan_vien = tk.Button(self.sidebar_frame, text="  Nhân viên", image=self.nhan_vien_icon, compound='left',
                                      anchor='w',borderwidth=0,
                                      font=("Arial", 14, "bold"), command=lambda: self.select_button("nhan_vien","NhanVienFrame"))
        self.btn_nhan_vien.pack(fill=tk.X, padx=10, pady=5)

        # Nút Nhà Cung Cấp
        self.nha_cung_cap_icon = PhotoImage(file="assets/img/icon/iconNCC.png")
        self.nha_cung_cap_icon_selected = PhotoImage(file="assets/img/iconSelected/iconNCCColor.png")
        self.btn_nha_cung_cap = tk.Button(self.sidebar_frame, text="  Nhà cung cấp", image=self.nha_cung_cap_icon,
                                       compound='left',
                                       anchor='w', borderwidth=0,
                                       font=("Arial", 14, "bold"), command=lambda: self.select_button("nha_cung_cap","NhaCungCapFrame"))
        self.btn_nha_cung_cap.pack(fill=tk.X, padx=10, pady=5)

        # Nút Báo cáo
        self.bao_cao_icon = PhotoImage(file="assets/img/icon/iconBaoCao.png")
        self.bao_cao_icon_selected = PhotoImage(file="assets/img/iconSelected/iconBaoCaoColor.png")
        self.btn_bao_cao = tk.Button(self.sidebar_frame, text="  Báo cáo", image=self.bao_cao_icon,
                                          compound='left',
                                          anchor='w', borderwidth=0,
                                          font=("Arial", 14, "bold"), command=lambda: self.select_button("bao_cao","BaoCaoFrame"))
        self.btn_bao_cao.pack(fill=tk.X, padx=10, pady=5)

        # Nút Phân Quyền
        self.phan_quyen_icon = PhotoImage(file="assets/img/icon/iconPhanQuyen.png")
        self.phan_quyen_icon_selected = PhotoImage(file="assets/img/iconSelected/iconPhanQuyenColor.png")
        self.btn_phan_quyen = tk.Button(self.sidebar_frame, text="  Phân Quyền", image=self.phan_quyen_icon,
                                     compound='left',
                                     anchor='w', borderwidth=0,
                                     font=("Arial", 14, "bold"), command=lambda: self.select_button("phan_quyen","PhanQuyenFrame"))
        self.btn_phan_quyen.pack(fill=tk.X, padx=10, pady=5)

        # Nút Đăng xuat
        self.dang_xuat_icon = PhotoImage(file="assets/img/icon/iconDangXuat.png")
        self.btn_dang_xuat = tk.Button(self.sidebar_frame, text="  Đăng xuất", image=self.dang_xuat_icon,
                                        compound='left',
                                        anchor='w', borderwidth=0,
                                        font=("Arial", 14, "bold"))
        self.btn_dang_xuat.pack(fill=tk.X, padx=10, pady=5)
        # CONTENT bên phải
        self.content_frame = tk.Frame(self, bg="white")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Tạo container để chứa các sub-frame
        self.main_container = tk.Frame(self.content_frame, bg="white")
        self.main_container.pack(fill=tk.BOTH, expand=True)

        # Từ điển để lưu các frame
        self.frames = {}

        for F in (KhachHangFrame, SanPhamFrame, DonHangFrame, KhoHangFrame, NhanVienFrame, NhaCungCapFrame, BaoCaoFrame,
                  PhanQuyenFrame):
            page_name = F.__name__
            try:
                frame = F(self.main_container)
                self.frames[page_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")
                print(f"Đã thêm khung: {page_name}")
            except Exception as e:
                print(f"Lỗi khi khởi tạo {page_name}: {e}")
                break  # hoặc continue, tùy thuộc vào mong muốn
        print("Các khung có sẵn:", self.frames.keys())
        self.select_button("khach_hang", "KhachHangFrame")

    def select_button(self, button_name, button_frame):
        print("check button >> ",button_name)
        print("check frame >> ",button_frame)
        # Đặt lại màu sắc của nút trước đó (nếu có)
        if self.selected_button:
            self.selected_button.config(bg="#f0f0f0", fg='#000')  # Reset màu sắc
            if self.selected_button == self.btn_khach_hang:
                self.btn_khach_hang.config(image=self.khach_hang_icon)
            elif self.selected_button == self.btn_san_pham:
                self.btn_san_pham.config(image=self.san_pham_icon)
            elif self.selected_button == self.btn_don_hang:
                self.btn_don_hang.config(image=self.don_hang_icon)
            elif self.selected_button == self.btn_kho_hang:
                self.btn_kho_hang.config(image=self.kho_hang_icon)
            elif self.selected_button == self.btn_nhan_vien:
                self.btn_nhan_vien.config(image=self.nhan_vien_icon)
            elif self.selected_button == self.btn_nha_cung_cap:
                self.btn_nha_cung_cap.config(image=self.nha_cung_cap_icon)
            elif self.selected_button == self.btn_bao_cao:
                self.btn_bao_cao.config(image=self.bao_cao_icon)
            elif self.selected_button == self.btn_phan_quyen:
                self.btn_phan_quyen.config(image=self.phan_quyen_icon)

        # Kiểm tra và thay đổi màu của nút đang được chọn
        if button_name == "khach_hang":
            self.btn_khach_hang.config(fg="#38b6ff", image=self.khach_hang_icon_selected)  # Nút "Khách hàng" được chọn
            self.selected_button = self.btn_khach_hang
        elif button_name == "san_pham":
            self.btn_san_pham.config(fg="#38b6ff", image=self.san_pham_icon_selected)  # Nút "Sản phẩm" được chọn
            self.selected_button = self.btn_san_pham
        elif button_name == "don_hang":
            self.btn_don_hang.config(fg="#38b6ff", image=self.don_hang_icon_selected)
            self.selected_button = self.btn_don_hang
        elif button_name == "kho_hang":
            self.btn_kho_hang.config(fg="#38b6ff", image=self.kho_hang_icon_selected)
            self.selected_button = self.btn_kho_hang
        elif button_name == "nhan_vien":
            self.btn_nhan_vien.config(fg="#38b6ff", image=self.nhan_vien_icon_selected)
            self.selected_button = self.btn_nhan_vien
        elif button_name == "nha_cung_cap":
            self.btn_nha_cung_cap.config(fg="#38b6ff", image=self.nha_cung_cap_icon_selected)
            self.selected_button = self.btn_nha_cung_cap
        elif button_name == "bao_cao":
            self.btn_bao_cao.config(fg="#38b6ff", image=self.bao_cao_icon_selected)
            self.selected_button = self.btn_bao_cao
        elif button_name == "phan_quyen":
            self.btn_phan_quyen.config(fg="#38b6ff", image=self.phan_quyen_icon_selected)
            self.selected_button = self.btn_phan_quyen

        # Chuyển đến giao diện mới (ví dụ: "KhachHangFrame")
        self.show_frame(button_frame)

    def show_frame(self, page_name):
        """
        Đưa frame tương ứng với page_name lên trên cùng.
        """
        print("Các khung có sẵn:", self.frames.keys())
        if page_name not in self.frames:
            print(f"Frame '{page_name}' không tìm thấy.")
            return
        frame = self.frames[page_name]
        frame.tkraise()
