from models.khoHangModel import  KhoHangModel

class KhoHangController:
    def __init__(self):
        self.khoHangModel = KhoHangModel()
    def getAllProductsController(self):
        result = self.khoHangModel.getAllProducts()
        return result
    def getAllHistoryController(self):
        result = self.khoHangModel.getHistoryTrade()
        return result