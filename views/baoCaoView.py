import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from controllers.baoCaoController import BaoCaoController
from config.commonDef import CommonDef
class BaoCaoFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.controller =BaoCaoController()
        self.commonDef = CommonDef()
        self.totalOrders = self.controller.getTotalOrdersContrller()
        self.totalProfit = self.controller.getTotalProfitController()
        self.totalProfitPure = self.controller.getTotalProfitPureContrller()
        self.productProfit = self.controller.getProfitProductController()
        print(self.productProfit)
        label = tk.Label(self, text="Giao diện Báo Cáo", bg="#fff",font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Header Section
        self.create_header()

        # Top Row (Statistical Boxes + Graph)
        self.create_top_row()

        # Bottom Section (Table + Customer Stats)
        self.create_bottom_section()

    def create_header(self):
        """Tạo phần tiêu đề với title và dropdown"""
        header_frame = tk.Frame(self, bg="white")
        header_frame.pack(fill="x", pady=10)

        # Tiêu đề "Tổng quan"
        tk.Label(header_frame, text="Tổng quan", font=("Arial", 18, "bold"),
                 bg="white").pack(side="left", padx=10)

        # Dropdown "Biểu đồ theo thời gian"
        time_combobox = ttk.Combobox(header_frame, values=["Biểu đồ theo thời gian"],
                                     state="readonly", font=("Arial", 12))
        time_combobox.set("Biểu đồ theo thời gian")
        time_combobox.pack(side="right", padx=10)

    def create_top_row(self):
        """Tạo hàng trên cùng với các hộp thống kê và biểu đồ"""
        top_frame = tk.Frame(self, bg="white")
        top_frame.pack(fill="x", pady=10)

        # Statistical Boxes
        stats_frame = tk.Frame(top_frame, bg="white")
        stats_frame.pack(side="left", padx=10)

        stats = [
            ("Số đơn hàng", self.totalOrders),
            ("Doanh thu thuần", self.commonDef.format_number(self.totalProfitPure[0])),
            ("Thực nhận", self.commonDef.format_number(self.totalProfit[0]) )
        ]

        for i, (label, value) in enumerate(stats):
            box = tk.Frame(stats_frame, bg="white", bd=1, relief="solid", width=150, height=100)
            box.grid(row=i // 2, column=i % 2, padx=5, pady=5)
            box.pack_propagate(False)  # Ngăn Frame co lại theo nội dung
            tk.Label(box, text=label, font=("Arial", 12), bg="white").pack(pady=5)
            tk.Label(box, text=value, font=("Arial", 16, "bold"), bg="white").pack(pady=5)

        # Line Graph
        graph_frame = tk.Frame(top_frame, bg="white", bd=1, relief="solid")
        graph_frame.pack(side="right", padx=10, fill="both", expand=True)

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(["1/2", "2/2", "3/2", "4/2"], [5, 4, 10, 18], color="lightblue")
        ax.set_xlabel("Thời gian")
        ax.set_ylabel("Giá trị")
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def create_bottom_section(self):
        """Tạo phần dưới cùng với bảng và thông tin khách hàng"""
        bottom_frame = tk.Frame(self, bg="white")
        bottom_frame.pack(fill="both", expand=True, pady=10)

        # Table "Sản phẩm đã bán"
        table_frame = tk.Frame(bottom_frame, bg="white", bd=1, relief="solid")
        table_frame.pack(side="left", padx=10, fill="both", expand=True)

        tk.Label(table_frame, text="Sản phẩm đã bán", font=("Arial", 14, "bold"),
                 bg="white").pack(pady=5)

        tree = ttk.Treeview(table_frame, columns=("Tên sản phẩm", "Số lượng bán", "Doanh thu"),
                            show="headings", height=10)
        for col in ("Tên sản phẩm", "Số lượng bán", "Doanh thu"):
            tree.heading(col, text=col)
            tree.column(col, width=150)
        tree.pack(fill="both", expand=True)

        format_data = []
        for name, quantity, rev in self.productProfit:
            new_data = (name, quantity, self.commonDef.format_number(rev))
            format_data.append(new_data)

        for item in format_data:
            tree.insert("", "end", values=item)


