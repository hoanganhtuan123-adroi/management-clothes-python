from models.nhanVienModel import NhanVienModel
class NhanVienController:
    def __init__(self):
        self.employee_model = NhanVienModel()

    def getAllEmployeesController(self):
        listEmployees = self.employee_model.getAllEmployeesModel()
        return listEmployees

    def createEmployeeController(self, data):
        employee = self.employee_model.createEmployeeModel(data)
        if employee:
            return True
        else:
            return False

    def updateEmployeeController(self, data):
        employee = self.employee_model.updateEmployeeModel(data)
        if employee:
            return True
        else:
            return False

    def deleteEmployeeController(self, id):
        employee = self.employee_model.deleteEmployeeModel(id)
        if employee:
            return True
        else:
            return False
