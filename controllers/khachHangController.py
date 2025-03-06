from models.khachHangModel import KhachHangModel
class KhachHangController:
    def __init__(self):
        self.customer_model = KhachHangModel()

    def getAllCustomersController(self):
        listCustomers = self.customer_model.getAllCustomersModel()
        return listCustomers

    def createCustomerController(self, data):
        customer = self.customer_model.createCustomerModel(data)
        if customer:
            return True
        else:
            return False
    def updateCustomerController(self, data):
        customer = self.customer_model.updateCustomerModel(data)
        if customer:
            return True
        else:
            return False
    def deleteCustomerController(self, id):
        customer = self.customer_model.deleteCustomerModel(id)
        if customer:
            return True
        else:
            return False