from database import Database
from datetime import datetime
class KhoHangModel:
    def __init__(self):
        self.db = Database()

    def getAllProducts(self):
        try:
            conn = self.db.get_connection()  # Lấy kết nối mới
            cursor = conn.cursor()
            query = """
                SELECT 
                    kh.id, 
                    sp.ma_sp,
                    kh.so_luong_nhap,
                    kh.so_luong_ton_kho,
                    kh.so_luong_ban_ra,
                    kh.ngay_nhap,
                    kh.gia_nhap 
                FROM khohang kh 
                INNER JOIN sanpham sp 
                ON sp.id = kh.id_san_pham
            """
            cursor.execute(query)
            result = cursor.fetchall()
            if not result:
                return "Dữ liệu trống"
            return result
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
        finally:
            if hasattr(self, 'conn'):
                conn.close()

    def getHistoryTrade(self):
        try:
            conn = self.db.get_connection()  # Lấy kết nối mới
            cursor = conn.cursor()
            query = """
                SELECT 
                    lsk.id,
                    kh.ma_nhap_hang,
                    sp.ma_sp,
                    lsk.so_luong,
                    lsk.loai_giao_dich,
                    lsk.ngay_giao_dich,
                    (lsk.gia * lsk.so_luong) AS tong_gia_tri
                FROM lichsukho lsk
                INNER JOIN khohang kh 
                    ON kh.id = lsk.id_kho_hang
                INNER JOIN sanpham sp 
                    ON sp.id = kh.id_san_pham
            """
            cursor.execute(query)
            result = cursor.fetchall()

            if not result:
                return "Dữ liệu trống"  # "Empty data"
            return result
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
        finally:
            if hasattr(self, 'conn'):
                conn.close()

    def generate_ma_nhap_hang(self):
        try:
            conn = self.db.get_connection()  # Lấy kết nối mới
            cursor = conn.cursor()
            # Lấy ngày hiện tại
            current_date = datetime.now().strftime("%Y%m%d")
            prefix = f"NH{current_date}"
            # Truy vấn số lượng bản ghi hôm nay
            query = f"""SELECT MAX(id) FROM khohang """

            cursor.execute(query)
            count = cursor.fetchone()[0]

            # Tạo số thứ tự
            sequence = count + 1
            formatted_sequence = f"{sequence:03d}"  # Định dạng 3 chữ số

            # Tạo mã nhập hàng
            ma_nhap_hang = f"{prefix}{formatted_sequence}"
            conn.close()
            return ma_nhap_hang

        except Exception as e:
            raise Exception(f"Lỗi sinh mã nhập hàng: {str(e)}")


    def generate_ma_kho(self):
        try:
            conn = self.db.get_connection()  # Lấy kết nối mới
            cursor = conn.cursor()
            # Truy vấn số lượng bản ghi hôm nay
            query = f"""SELECT MAX(id) FROM lichsukho """
            cursor.execute(query)
            count = cursor.fetchone()[0]
            # Lấy ngày hiện tại
            current_date = datetime.now().strftime("%Y%m%d")
            prefix = f"KH{current_date}"
            # Tạo số thứ tự
            sequence = count + 1
            formatted_sequence = f"{sequence:03d}"  # Định dạng 3 chữ số

            # Tạo mã nhập hàng
            ma_kho = f"{prefix}{formatted_sequence}"
            conn.close()
            return ma_kho
        except Exception as e:
            raise Exception(f"Lỗi sinh mã nhập hàng: {str(e)}")


    def insertStock(self, data):
        try:
            ma_nhap_hang = self.generate_ma_nhap_hang()
            conn = self.db.get_connection()  # Lấy kết nối mới
            cursor = conn.cursor()
            query = """
                INSERT into khohang (ma_nhap_hang, id_san_pham, id_nha_cung_cap, so_luong_nhap, so_luong_ton_kho, so_luong_ban_ra, ngay_nhap, gia_nhap, gia_ban) 
                VALUES(%s, %s, %s,%s, %s, %s,%s, %s, %s)
            """
            # Thực thi query với các tham số
            cursor.execute(query, (
                ma_nhap_hang,
                data['id_san_pham'],
                data['id_nha_cung_cap'],
                data['so_luong_nhap'],
                data['so_luong_ton_kho'],
                data['so_luong_ban_ra'],
                data['ngay_nhap'],
                data['gia_nhap'],
                data['gia_ban']
            ))

            inserted_id = cursor.lastrowid

            # Commit transaction
            conn.commit()

            return inserted_id


        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
        finally:
            if hasattr(self, 'conn'):
                conn.close()

    def insertHistoryStock(self, id_kho_hang):
        try:
            conn = self.db.get_connection()  # Lấy kết nối mới
            cursor = conn.cursor()
            ma_kho = self.generate_ma_kho()
            query = "INSERT INTO lichsukho (id_kho_hang, ma_kho, loai_giao_dich, gia, ngay_giao_dich, so_luong) VALUES(%s, %s,'Nhập Kho', %s,%s, %s )"
            cursor.execute(query,(id_kho_hang,ma_kho, ))

            conn.close()
        except Exception as e:
            raise Exception(f"Lỗi sinh mã nhập hàng: {str(e)}")
