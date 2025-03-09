from models.donHangModel import DonHangModel

class DonHangController:
    def __init__(self):
        self.donHangModel = DonHangModel()
    def getOrdersController(self):
        orders = self.donHangModel.getOrdersModel()
        if not orders:
            raise Exception("Lỗi lấy danh sách đơn hàng")
        else:
            return orders

    def getOrdersLatestController(self):
        orders = self.donHangModel.getOrdersLatestModel()
        if not orders:
            raise Exception("Lỗi lấy danh sách đơn hàng")
        else:
            return orders
    def getOrdersHasntPaidController(self):
        orders = self.donHangModel.getOrdersHasntPaidModel()
        if not orders:
            raise Exception("Lỗi lấy danh sách đơn hàng")
        else:
            return orders

    def getOrdersHasntDeliveredController(self):
        orders = self.donHangModel.getOrdersHasntDeliveredModel()
        if not orders:
            raise Exception("Lỗi lấy danh sách đơn hàng")
        else:
            return orders

    def createOrderController(self, data):
        id_san_pham = data['items'][0][0]  # Lấy id sản phẩm
        so_luong = data['items'][0][1]  # Lấy số lượng
        data['id_san_pham'] = id_san_pham  # Gán giá trị trực tiếp
        data['so_luong'] = so_luong  # Gán giá trị trực tiếp
        data.pop('items')
        order = self.donHangModel.createOrderModal(data)
        if not order:
            raise Exception("Lỗi tạo đơn hàng")
        else:
            return order