from database import Database
class NhaCungCapModel:
    def __init__(self):
        self.db = Database()

    def getAllSuppliers(self):
        try:
            conn = self.db.get_connection()
            if not conn.is_connected():
                print("Connection lost. Attempting to reconnect...")
                conn.reconnect()
            cursor = conn.cursor()
            query = "SELECT id, ma_nha_cung_cap, ten_dai_dien ,ten_mat_hang, email, so_dien_thoai, dia_chi FROM nhacungcap"
            cursor.execute(query)
            result = cursor.fetchall()
            conn.close()
            return result
        except Exception as e:
            # Handle unexpected errors
            print(f"An unexpected error occurred: {e}")
            raise

    def addNewSupplier(self, data):
        try:
            print(data)
            conn = self.db.get_connection()
            cursor = conn.cursor()

            # Sửa câu lệnh INSERT - phải sử dụng dấu %s làm placeholder cho tham số
            query = """INSERT INTO nhacungcap 
                    (ma_nha_cung_cap, ten_mat_hang, ten_dai_dien, email, so_dien_thoai, dia_chi) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""

            cursor.execute(query, (
                data['ma_nha_cung_cap'],
                data['ten_mat_hang'],
                data['ten_dai_dien'],
                data['email'],
                data['so_dien_thoai'],
                data['dia_chi']
            ))

            conn.commit()
            conn.close()

            if cursor.rowcount > 0:
                return True
            return False
        except Exception as e:
            print(f"Error in addNewSupplier: {e}")
            # Bạn có thể log lỗi ở đây
            return False  # Hoặc raise lại exception tùy vào cách xử lý lỗi

    def updateSupplier(self, data):
        try:
            conn = self.db.get_connection()
            if not conn.is_connected():
                print("Connection lost. Attempting to reconnect...")
                conn.reconnect()
            cursor = conn.cursor()
            query = "UPDATE nhacungcap SET ma_nha_cung_cap = %s, ten_mat_hang = %s, ten_dai_dien = %s, email = %s, so_dien_thoai = %s, dia_chi = %s WHERE id = %s"
            cursor.execute(query, (data['ma_nha_cung_cap'], data['ten_mat_hang'], data['ten_dai_dien'], data['email'], data['so_dien_thoai'], data['dia_chi'], data['id']))
            conn.commit()
            conn.close()
            return True
        except:
            raise Exception

    def deleteSupplier(self, id):
        try:
            conn = self.db.get_connection()
            if not conn.is_connected():
                print("Connection lost. Attempting to reconnect...")
                conn.reconnect()
            cursor = conn.cursor()
            query = "DELETE FROM nhacungcap WHERE id = %s"
            cursor.execute(query, (id,))
            if cursor.rowcount >0:
                conn.commit()
                conn.close()
                return True
            else:
                conn.close()
                return False
        except:
            raise Exception
