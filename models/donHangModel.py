import datetime
import random


from database import Database
class DonHangModel:
    def __init__(self):
        self.db = Database()
    def getOrdersModel(self):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        if not conn.is_connected():
            print("Connection lost. Attempting to reconnect...")
            conn.reconnect()
        try:
            query = f"""
                     SELECT dh.id, dh.ma_don_hang,  sp.ten_sp, dh.ngay_dat, tt.trang_thai_thanh_toan, dh.trang_thai_don, kh.ho_va_ten, sp.gia_ban,  ctdh.so_luong, dh.tong_tien from donhang dh 
                        LEFT JOIN chitietdonhang ctdh on ctdh.id_don_hang = dh.id
                        LEFT JOIN sanpham sp on sp.id = ctdh.id_san_pham
                        LEFT JOIN thanhtoan tt on tt.id_don_hang = dh.id
                        LEFT JOIN khachhang kh on kh.id = dh.id_khach_hang
                        """
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            conn.close()
            return result
        except:
            raise Exception("Lỗi trong quá trình truy vấn")

    def getOrdersLatestModel(self):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        if not conn.is_connected():
            print("Connection lost. Attempting to reconnect...")
            conn.reconnect()
        try:
            query = f"""
                       SELECT dh.id, dh.ma_don_hang,  sp.ten_sp, dh.ngay_dat, tt.trang_thai_thanh_toan, dh.trang_thai_don, kh.ho_va_ten, sp.gia_ban,  ctdh.so_luong, dh.tong_tien from donhang dh 
                          LEFT JOIN chitietdonhang ctdh on ctdh.id_don_hang = dh.id
                          LEFT JOIN sanpham sp on sp.id = ctdh.id_san_pham
                          LEFT JOIN thanhtoan tt on tt.id_don_hang = dh.id
                          LEFT JOIN khachhang kh on kh.id = dh.id_khach_hang
                          ORDER BY dh.ngay_dat DESC
                          """
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            conn.close()
            return result
        except:
            raise Exception("Lỗi trong quá trình truy vấn")

    def getOrdersHasntPaidModel(self):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Loi ket noi csdl")
        if not conn.is_connected():
            print("Connection lost. Attempting to reconnect...")
            conn.reconnect()
        try:
            query = f"""
            SELECT dh.id, dh.ma_don_hang,  sp.ten_sp, dh.ngay_dat, tt.trang_thai_thanh_toan, dh.trang_thai_don, kh.ho_va_ten, sp.gia_ban,  ctdh.so_luong, dh.tong_tien from donhang dh 
            LEFT JOIN chitietdonhang ctdh on ctdh.id_don_hang = dh.id
            LEFT JOIN sanpham sp on sp.id = ctdh.id_san_pham
            LEFT JOIN thanhtoan tt on tt.id_don_hang = dh.id
            LEFT JOIN khachhang kh on kh.id = dh.id_khach_hang
            WHERE tt.trang_thai_thanh_toan = 'Chưa thanh toán' """
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            conn.close()
            if result:
                return result
            else:
                return []
        except:
            raise Exception("Loi trong qua trinh truy van")

    def getOrdersHasntDeliveredModel(self):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Loi ket noi csdl")
        if not conn.is_connected():
            print("Connection lost. Attempting to reconnect...")
            conn.reconnect()
        try:
            query = f"""
              SELECT dh.id, dh.ma_don_hang,  sp.ten_sp, dh.ngay_dat, tt.trang_thai_thanh_toan, dh.trang_thai_don, kh.ho_va_ten, sp.gia_ban,  ctdh.so_luong, dh.tong_tien from donhang dh 
              LEFT JOIN chitietdonhang ctdh on ctdh.id_don_hang = dh.id
              LEFT JOIN sanpham sp on sp.id = ctdh.id_san_pham
              LEFT JOIN thanhtoan tt on tt.id_don_hang = dh.id
              LEFT JOIN khachhang kh on kh.id = dh.id_khach_hang
              WHERE dh.trang_thai_don = 'Chưa giao hàng' """
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            conn.close()
            if result:
                return result
            else:
                return []
        except:
            raise Exception("Loi trong qua trinh truy van")

    def random_order_code(self, length=3):
        prefix = "DH"
        random_number = random.randint(10**(length-1), (10**length)-1)
        return f"{prefix}{random_number:0{length}d}"

    def createOrderModal(self, data):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Loi ket noi csdl")
        try:
            cursor = conn.cursor()
            ngay_dat = datetime.datetime.now()
            query = "INSERT INTO donhang (id_khach_hang, ma_don_hang, tong_tien, dia_chi_giao_hang, trang_thai_don, ngay_dat) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (data['customer_id'], self.random_order_code(), data['total'], data['dia_chi'], "Chưa giao hàng", ngay_dat))
            id_don_hang = cursor.lastrowid

            query_ctdh = "INSERT INTO chitietdonhang(id_san_pham, id_don_hang, so_luong) VALUES (%s, %s, %s)"
            for index in range(len(data['id_san_pham'])):
                cursor.execute(query_ctdh, (data['id_san_pham'][index], id_don_hang, data['so_luong'][index]))

            # Chèn dữ liệu vào bảng thanh_toan
            query_thanh_toan = "INSERT INTO thanhtoan (id_don_hang, so_tien, ma_giao_dich, trang_thai_thanh_toan, ngay_thanh_toan, phuong_thuc_thanh_toan) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query_thanh_toan, (
                id_don_hang,
                data['total'],  # Số tiền thanh toán
                f"TT{id_don_hang:03d}",  # Ví dụ: ma_giao_dich như TT002
                'Chưa thanh toán',
                ngay_dat,  # Ngày thanh toán
                data.get('payment_method')  # Phương thức thanh toán
            ))

            conn.commit()
            conn.close()
            return True
        except:
            raise Exception("Loi trong qua trinh truy van")

    def deleteOrderModal(self, id):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Loi ket noi csdl")
        try:
            cursor = conn.cursor()
            query_delte = "DELETE FROM donhang WHERE ma_don_hang= %s"
            cursor.execute(query_delte, (id,))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình truy vấn: {str(e)}")