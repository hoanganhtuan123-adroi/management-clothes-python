from database import Database
class KhachHangModel:
    def __init__(self):
        self.db = Database()

    def getAllCustomersModel(self):
        try:
            conn = self.db.get_connection()
            if not conn.is_connected():
                print("Connection lost. Attempting to reconnect...")
                conn.reconnect()
            listCustomers = []
            cursor = conn.cursor()
            query = "SELECT * FROM khachhang"
            cursor.execute(query)
            customers = cursor.fetchall()
            if customers :
                for customer in customers:
                    customer_dict = {
                        "id": customer[0],
                        "hoten": customer[1],
                        "sdt": customer[2],
                        "email": customer[3],
                        "diachi": customer[4],
                        "gioitinh": customer[5],
                        "hinhanh": customer[6]
                    }
                    listCustomers.append(customer_dict)
            conn.close()
            return listCustomers
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

    def createCustomerModel(self, data):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            cursor = conn.cursor()
            query = "INSERT INTO khachhang (ho_va_ten, so_dien_thoai, email, dia_chi, gioi_tinh, hinh_anh) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (data['hoten'], data['sdt'], data['email'], data['diachi'], data['gioitinh'], data['hinhanh']))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

    def updateCustomerModel(self, data):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            cursor = conn.cursor()
            query = "UPDATE khachhang SET ho_va_ten = %s, so_dien_thoai = %s, email = %s, dia_chi = %s, gioi_tinh = %s, hinh_anh = %s WHERE id = %s"
            cursor.execute(query,(data['hoten'], data['sdt'], data['email'], data['diachi'], data['gioitinh'], data['hinhanh'], data['id']))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

    def deleteCustomerModel(self, id):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            cursor = conn.cursor()
            query = "DELETE FROM khachhang WHERE id = %s"
            cursor.execute(query, (id,))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")