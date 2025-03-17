from models.nhaCungCapModel import NhaCungCapModel

class NhaCungCapController:
    def __init__(self):
        self.model = NhaCungCapModel()
    def getAllSuppliersControlller(self):
        result = self.model.getAllSuppliers()
        return result

    def addNewSupplierController(self, data):
        converted_data = {
            'ma_nha_cung_cap': data['Mã nhà cung cấp'],
            'ten_dai_dien': data['Đơn vị cung cấp'],
            'ten_mat_hang': data['Mặt hàng cung cấp'],
            'email': data['Email'],
            'so_dien_thoai': data['Số điện thoại'],
            'dia_chi': data['Địa chỉ']
        }
        print(converted_data)
        result = self.model.addNewSupplier(converted_data)
        return result

    def updateSupplierController(self, data):
        converted_data = {
            'id': data['id'],
            'ma_nha_cung_cap': data['Mã nhà cung cấp'],
            'ten_dai_dien': data['Đơn vị cung cấp'],
            'ten_mat_hang': data['Mặt hàng cung cấp'],
            'email': data['Email'],
            'so_dien_thoai': data['Số điện thoại'],
            'dia_chi': data['Địa chỉ']
        }
        if converted_data is not None:
            result = self.model.updateSupplier(converted_data)
            return result

    def deleteSupplierController(self, id):
        id_supplier = id
        print("Check id s", id_supplier)
        result = self.model.deleteSupplier(id_supplier)
        return result