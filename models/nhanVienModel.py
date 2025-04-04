import time
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
            if not conn.is_connected():
                conn.reconnect()
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
            conn.close()
            return listEmployees
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

    def getAllEmployeesByIDModel(self, id):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            if not conn.is_connected():
                conn.reconnect()
            cursor = conn.cursor()
            query = "SELECT * FROM nhanvien WHERE id=%s"
            cursor.execute(query, (id,))
            employees = cursor.fetchall()
            cursor.close()
            conn.close()
            return employees
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")


    def createEmployeeModel(self, data):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            cursor = conn.cursor()
            if not conn.is_connected():
                conn.reconnect()
            timestamp = time.time()
            current_time = time.localtime(timestamp)
            current_date = time.strftime("%Y/%m/%d", current_time)
            he_so_luong = 1
            query = """INSERT INTO nhanvien (ma_nhan_vien, ho_va_ten, dia_chi, sdt, email, luong, chuc_vu, ngay_vao_lam, ngay_cong_chuan, he_so_luong, trang_thai_lam_viec) 
                       VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"""
            if "nhân viên" in str.lower(data['chuc_vu']):
                he_so_luong = 1
            elif data['chuc_vu'] == "Quản lý":
                he_so_luong = 1.5
            elif data['chuc_vu'] == "Giám đốc":
                he_so_luong = 2
            elif data['chuc_vu'] == "Kế toán":
                he_so_luong = 1.2
            cursor.execute(query, (data['ma_nhan_vien'], data['ho_ten'], data['dia_chi'], data['dien_thoai'] ,data['email'], data['luong'], data['chuc_vu'], current_date, 1, he_so_luong, "Đang làm việc"))
            conn.commit()
            conn.close()
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
            conn.close()
            return True
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

    def deleteEmployeeModel(self, id):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        if not conn.is_connected():
            conn.reconnect()
        try:
            cursor = conn.cursor()
            query = "DELETE FROM nhanvien WHERE id = %s"
            cursor.execute(query, (id,))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

