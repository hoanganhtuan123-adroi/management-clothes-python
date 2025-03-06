from models.sanPhamModel import SanPhamModel

class SanPhamController:
    def __init__(self):
        self.product_model = SanPhamModel()
    def getProductsController(self):
        products = self.product_model.getAllProductsModel()
        if products:
            return products
        else:
            return []