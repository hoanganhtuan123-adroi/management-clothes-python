import tkinter as tk
class DonHangFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")

        label = tk.Label(self, text="Giao diện Đơn hàng", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Ở đây bạn có thể tùy chỉnh thêm các widget cho đơn hàng
        tk.Label(self, text="Đây là nơi hiển thị danh sách đơn hàng").pack()