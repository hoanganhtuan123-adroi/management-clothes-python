from database import Database
class BaoCaoModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
    def getTotalOrders(self):
        try:
            query = "SELECT COUNT(*) AS total_order FROM donhang"
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()
            return result
        except:
            raise Exception("Loi")

    def getTotalProfit(self):
        try:
            query = "SELECT SUM(so_tien) FROM thanhtoan WHERE trang_thai_thanh_toan = 'Đã thanh toán'"
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()
            return result
        except:
            raise Exception("Loi")

    def getTotalProfitPure(self):
        try:
            query = "SELECT SUM(so_tien) FROM thanhtoan"
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()
            return result
        except:
            raise Exception("Loi")

    def getProfitProduct(self):
        try:
            query = """
            SELECT sp.ten_sp AS ten_san_pham, 
                   SUM(ctdh.so_luong) AS so_luong_ban, 
                   SUM(ctdh.so_luong * sp.gia_ban) AS doanh_thu 
            FROM sanpham sp 
            JOIN chitietdonhang ctdh ON sp.id = ctdh.id_san_pham 
            GROUP BY sp.id, sp.ten_sp, sp.gia_ban 
            ORDER BY sp.ten_sp
            """
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()  # Lấy tất cả các hàng
            cursor.close()
            return result
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình truy vấn: {str(e)}")
        finally:
            if self.conn:
                self.conn.close()  # Đảm bảo đóng kết nối

