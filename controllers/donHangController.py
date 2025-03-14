from models.donHangModel import DonHangModel
from decimal import Decimal
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
        id_san_pham_list =[]
        so_luong_list = []
        for item in data['items']:
            id_san_pham_list.append(item[0])
            so_luong_list.append(item[1])

        new_data = {
            'customer_id': data['customer_id'],
            'dia_chi': data['dia_chi'],
            'total': Decimal(str(data['total'])),
            'payment_method': data['payment_method'],
            'id_san_pham': id_san_pham_list,
            'so_luong': so_luong_list
        }
        order = self.donHangModel.createOrderModal(new_data)
        if not order:
            raise Exception("Lỗi tạo đơn hàng")
        else:
            return order

    def deleteOrderContrller(self, id):
        print("chekc id >>> ",id)
        isSuccess = self.donHangModel.deleteOrderModal(id)
        if isSuccess:
            return True
        else:
            return False