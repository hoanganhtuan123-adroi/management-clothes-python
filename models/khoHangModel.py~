import random
import string
from database import Database
from datetime import datetime
class KhoHangModel:
    def __init__(self):
        self.db = Database()

    def getAllProducts(self):
        try:
            conn = self.db.get_connection()  # Lấy kết nối mới
            if not conn.is_connected():
                print("Connection lost. Attempting to reconnect...")
                conn.reconnect()
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
            conn.close()
            if not result:
                return "Dữ liệu trống"
            return result
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
        finally:
            if hasattr(self, 'conn'):
                conn.close()

    def getAllSponsers(self):
        try:
            conn = self.db.get_connection()  # Lấy kết nối mới
            if not conn.is_connected():
                print("Connection lost. Attempting to reconnect...")
                conn.reconnect()
            cursor = conn.cursor()
            query = """SELECT id, ma_nha_cung_cap FROM nhacungcap """
            cursor.execute(query)
            result = cursor.fetchall()
            conn.close()
            if not result:
                return "Dữ liệu trống"
            return result
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

    def getHistoryTrade(self):
        try:
            conn = self.db.get_connection()  # Lấy kết nối mới
            if not conn.is_connected():
                print("Connection lost. Attempting to reconnect...")
                conn.reconnect()
            cursor = conn.cursor()
            query = """
                SELECT 
                    lsk.id,
                    sp.ma_sp,
                    lsk.so_luong,
                    lsk.loai_giao_dich,
                    lsk.ngay_giao_dich,
                    (lsk.gia * lsk.so_luong) AS tong_gia_tri
                FROM lichsukho lsk
                INNER JOIN sanpham sp 
                    ON sp.id = lsk.id_san_pham
            """
            cursor.execute(query)
            result = cursor.fetchall()
            conn.close()
            if not result:
                return "Dữ liệu trống"  # "Empty data"
            return result
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

    def getAllProducts(self):
        try:
            conn = self.db.get_connection()  # Lấy kết nối mới
            if not conn.is_connected():
                print("Connection lost. Attempting to reconnect...")
                conn.reconnect()
            cursor = conn.cursor()
            query = """
                SELECT kh.id_san_pham, sp.ten_sp FROM khohang kh LEFT JOIN sanpham sp on sp.id = kh.id_san_pham 
            """
            cursor.execute(query)
            result = cursor.fetchall()
            conn.close()
            if not result:
                return "Dữ liệu trống"
            return result
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

    def generate_ma_kho(self):
        try:
            conn = self.db.get_connection()  # Lấy kết nối mới
            cursor = conn.cursor()
            # Truy vấn số lượng bản ghi hôm nay
            query = f"""SELECT MAX(id) FROM lichsukho """
            cursor.execute(query)
            count = cursor.fetchone()[0]
            conn.close()
            # Lấy ngày hiện tại
            current_date = datetime.now().strftime("%Y%m%d")
            prefix = f"KH{current_date}"
            # Tạo số thứ tự
            sequence = count + 1
            formatted_sequence = f"{sequence:03d}"  # Định dạng 3 chữ số

            # Tạo mã nhập hàng
            ma_kho = f"{prefix}{formatted_sequence}"
            return ma_kho
        except Exception as e:
            raise Exception(f"Lỗi sinh mã nhập hàng: {str(e)}")

    # Trong phương thức them vao kho hang
    def insertStock(self, data):
        conn = None
        try:
            conn = self.db.get_connection()
            if not conn.is_connected():
                print("Connection lost. Attempting to reconnect...")
                conn.reconnect()
            cursor = conn.cursor()

            # Sửa tên key trong data
            query_pd = "SELECT gia_ban FROM sanpham WHERE id = %s"
            cursor.execute(query_pd, (data['id_san_pham'],))  # Đúng key
            result = cursor.fetchone()

            if not result:
                raise ValueError("Không tìm thấy sản phẩm")

            gia_ban = result[0]

            query = """
                INSERT INTO khohang 
                (id_san_pham, id_nha_cung_cap, so_luong_nhap, 
                 so_luong_ton_kho, so_luong_ban_ra, ngay_nhap, gia_nhap, gia_ban) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
            """
            # Sửa các key trong data
            cursor.execute(query, (
                data['id_san_pham'],  # Sửa từ 'san_pham'
                data['id_nha_cung_cap'],  # Sửa từ 'nha_cung_cap'
                data['sl_nhap'],
                data['sl_ton'],
                data['sl_ban'],
                data['ngay_nhap'],
                data['gia_nhap'],
                gia_ban
            ))
            conn.commit()
            conn.close()
            return

        except Exception as e:
            raise Exception(f"Lỗi khi nhập kho: {str(e)}")

    # Thêm vao lich su kho
    def insertHistoryStock(self, data):
        conn = None
        try:
            print("Data received:", data)
            conn = self.db.get_connection()
            if not conn.is_connected():
                print("Connection lost. Attempting to reconnect...")
                conn.reconnect()
            cursor = conn.cursor()

            check_query = "SELECT id FROM sanpham WHERE id = %s"
            cursor.execute(check_query, (data['id_san_pham'],))
            if not cursor.fetchone():
                raise Exception(f"Sản phẩm với id {data['id_san_pham']} không tồn tại trong bảng sanpham")
            ma_kho = self.generate_random_ma_kho()
            # self.insertStock(data)
            query = """
                INSERT INTO lichsukho 
                (id_san_pham, ma_kho, loai_giao_dich, gia, ngay_giao_dich, so_luong) 
                VALUES(%s, %s, %s, %s, %s, %s)
            """
            # Sửa thứ tự parameters và syntax
            cursor.execute(query, (
                data['id_san_pham'],
                ma_kho,
                'Nhập Kho',
                data['gia_nhap'],
                data['ngay_nhap'],
                data['sl_nhap']
            ))

            query_khohang = "INSERT INTO khohang(id_san_pham, id_nha_cung_cap, so_luong_nhap, so_luong_ton_kho, so_luong_ban_ra, ngay_nhap, gia_nhap, gia_ban) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query_khohang, (
                data['id_san_pham'],
                data['id_nha_cung_cap'],
                data['sl_nhap'],
                data['sl_ton'],
                data['sl_ban'],
                data['ngay_nhap'],
                data['gia_nhap'],
                data['gia_ban']
            ))
            conn.commit()
            conn.close()
            return cursor.rowcount > 0  # Sửa rowcount thành attribute
        except Exception as e:
            print(f"Chi tiết lỗi: {e}")
            raise Exception(f"Lỗi lịch sử kho: {e}")  # Thông báo lỗi chính xác
        finally:
            if conn:
                conn.close()

    def generate_random_ma_kho(self,length=6):
        characters = string.ascii_uppercase + string.digits

        # Sinh chuỗi ngẫu nhiên
        random_part = ''.join(random.choices(characters, k=length))

        # Format mã kho
        return f"KHO-{random_part}"

    def xuatKho(self, data):
        conn = None
        try:
            print("Check data received:", data)
            conn = self.db.get_connection()
            if not conn.is_connected():
                print("Connection lost. Attempting to reconnect...")
                conn.reconnect()
            cursor = conn.cursor(buffered=True)

            # 1. Lấy giá bán từ bảng sanpham
            cursor.execute("SELECT gia_ban FROM sanpham WHERE id = %s", (data['id_san_pham'],))
            result = cursor.fetchone()

            if not result:
                raise Exception("Không tìm thấy sản phẩm")
            gia_ban = result[0]

            # 2. Kiểm tra tồn kho
            cursor.execute("""
                SELECT so_luong_ton_kho 
                FROM khohang 
                WHERE id_san_pham = %s
            """, (data['id_san_pham'],))

            ton_kho_result = cursor.fetchone()
            if not ton_kho_result:
                raise Exception("Không tìm thấy tồn kho cho sản phẩm này")

            ton_kho = ton_kho_result[0]

            if ton_kho < data['so_luong_xuat']:
                raise Exception("Số lượng xuất vượt quá tồn kho")

            # 3. Cập nhật tồn kho
            new_ton_kho = ton_kho - data['so_luong_xuat']
            cursor.execute("""
                UPDATE khohang 
                SET so_luong_ton_kho = %s 
                WHERE id_san_pham = %s
            """, (new_ton_kho, data['id_san_pham']))
            ma_kho = self.generate_random_ma_kho()
            # 4. Ghi lịch sử với id_san_pham và giá
            cursor.execute("""
                INSERT INTO lichsukho (
                    id_san_pham, 
                    ma_kho,
                    loai_giao_dich, 
                    gia, 
                    ngay_giao_dich, 
                    so_luong
                ) VALUES (%s, %s ,'Xuất kho', %s, %s, %s)
            """, (
                data['id_san_pham'],
                ma_kho,
                gia_ban,
                data['ngay_xuat'],
                data['so_luong_xuat']
            ))

            conn.commit()
            conn.close()
            return True
        except Exception as e:
            if conn:
                conn.rollback()
            raise Exception(f"Lỗi xuất kho: {e}")
        finally:
            if conn:
                conn.close()