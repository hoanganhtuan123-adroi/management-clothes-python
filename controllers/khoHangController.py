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
    def getAllSponsersController(self):
        result = self.khoHangModel.getAllSponsers()
        return result
    def insertHistoryStockController(self, data):
        result = self.khoHangModel.insertHistoryStock(data)
        return result

    def xuatKhoController(self, data):
        result = self.khoHangModel.xuatKho(data)
        return result
    def getAllProductsExportController(self):
        result = self.khoHangModel.getAllProductsExport()
        return result