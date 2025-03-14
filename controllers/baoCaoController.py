from models.baoCaoModel import BaoCaoModel

class BaoCaoController:
    def __init__(self):
        self.model = BaoCaoModel()
    def getTotalOrdersContrller(self):
        result = self.model.getTotalOrders()
        return result;
    def getTotalProfitController(self):
        result = self.model.getTotalProfit()
        return result
    def getTotalProfitPureContrller(self):
        result = self.model.getTotalProfitPure()
        return result
    def getProfitProductController(self):
        result = self.model.getProfitProduct()
        return result
