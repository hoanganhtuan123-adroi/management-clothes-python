from models.taiKhoanModel import TaiKhoanModel

class TaiKhoanController:
    def __init__(self):
        self.model = TaiKhoanModel()
    def getAllAccountsController(self):
        result = self.model.getAllAccounts()
        return result

    def getInforAccountController(self, id):
        try:
            result = self.model.getInforAccount(id)
            return result
        except:
            raise Exception

    def updateAccountController(self, data):
        result = self.model.updateAccount(data)
        return result