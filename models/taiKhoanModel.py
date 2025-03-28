from database import Database
class TaiKhoanModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()

    def getAllAccounts(self):

        try:
            cursor = self.conn.cursor()
            query = "SELECT nv.ma_nhan_vien, nv.ho_va_ten, tk.tai_khoan, tk.mat_khau, tk.vai_tro, tk.trang_thai_tai_khoan from taikhoan tk INNER JOIN nhanvien nv on nv.id = tk.id_nhan_vien"
            cursor.execute(query)
            result = cursor.fetchall()
            self.conn.close()
            return result
        except:
            raise Exception

    def getInforAccount(self, id):
        try:
            cursor = self.conn.cursor()
            query = "SELECT tk.tai_khoan, tk.mat_khau, tk.vai_tro, tk.trang_thai_tai_khoan, nv.email, nv.ho_va_ten, nv.sdt, tk.ma_nguoi_dung FROM nhanvien nv INNER JOIN taikhoan tk on tk.id_nhan_vien = nv.id WHERE nv.ma_nhan_vien = %s"
            cursor.execute(query, (id,))
            result = cursor.fetchone()
            self.conn.close()
            return result
        except:
            raise Exception

    def updateAccount(self, data):
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor()
            query = "UPDATE taikhoan SET mat_khau = %s , vai_tro = %s, trang_thai_tai_khoan = %s, email = %s WHERE ma_nguoi_dung = %s"
            cursor.execute(query, (data['mat_khau'], data['vai_tro'], data['trang_thai_tai_khoan'], data['email'] ,data['ma_nguoi_dung']))
            conn.commit()
            if cursor.rowcount > 0:
                conn.commit()  # Commit the transaction
                print("Account updated successfully.")
                conn.close()
                return True
            else:
                print("No rows were updated. Please check the provided data.")
                self.conn.close()
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
# md = TaiKhoanModel()
# print(md.getInforAccount('NV001'))