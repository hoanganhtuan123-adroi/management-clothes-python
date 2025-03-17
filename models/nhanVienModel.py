from database import Database

class NhanVienModel:
    def __init__(self):
        self.db = Database()

    def getAllEmployeesModel(self):
        conn = self.db.get_connection()
        listEmployees = []
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM nhanvien"
            cursor.execute(query)
            employees = cursor.fetchall()
            if employees:
                for employee in employees:
                    employee_dict = {
                        "id": employee[0],
                        "ma_nhan_vien": employee[1],
                        "ho_ten": employee[2],
                        "email": employee[3],
                        "chuc_vu": employee[4],
                        "dien_thoai": employee[5],
                    }
                    listEmployees.append(employee_dict)
            cursor.close()
            return listEmployees
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

    def createEmployeeModel(self, data):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            cursor = conn.cursor()
            query = """INSERT INTO nhanvien (ma_nhan_vien, ho_va_ten, email, chuc_vu, sdt) 
                       VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(query, (data['ma_nhan_vien'], data['ho_ten'], data['email'], data['chuc_vu'], data['dien_thoai']))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

    def updateEmployeeModel(self, data):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            cursor = conn.cursor()
            query = """UPDATE nhanvien SET ho_va_ten = %s, email = %s, chuc_vu = %s, sdt = %s 
                       WHERE ma_nhan_vien = %s"""
            cursor.execute(query, (data['ho_ten'], data['email'], data['chuc_vu'], data['dien_thoai'], data['ma_nhan_vien']))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

    def deleteEmployeeModel(self, id):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            cursor = conn.cursor()
            query = "DELETE FROM nhanvien WHERE ma_nhan_vien = %s"
            cursor.execute(query, (id,))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")
