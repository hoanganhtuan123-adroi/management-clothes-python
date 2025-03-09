from database import Database
from config.commonDef import CommonDef
class SanPhamModel:
    def __init__(self):
        self.db = Database()
        self.commonDef = CommonDef()
    def getAllProductsModel(self):
        conn = self.db.get_connection()
        products_list = []
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM sanpham"
            cursor.execute(query)
            products = cursor.fetchall()
            if products:
                for product in products:
                    product_list = {
                        "id": product[0],
                        "ten_sp": product[1],
                        "ma_sp": product[2],
                        "mo_ta": product[3],
                        "loai_san_pham": product[4],
                        "gia_ban": product[5],
                        "hinh_anh": product[6],
                        "kich_thuoc": product[7],
                        "mau_sac": product[8]
                    }
                    products_list.append(product_list)
            cursor.close()
            return products_list
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

    def createProductModel(self, data):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            cursor = conn.cursor()
            query = "INSERT INTO sanpham (ten_sp, ma_sp, mo_ta, loai_san_pham, gia_ban, hinh_anh, kich_thuoc, mau_sac) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (data['ten_sp'], data['ma_sp'], data['mo_ta'], data['loai_sp'], data['gia_ban'],  data['hinh_anh'], data['kich_thuoc'], data['mau_sac']))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

    def deleteProductModel(self, id):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            cursor = conn.cursor()
            query = "DELETE FROM sanpham WHERE id = %s"
            cursor.execute(query, (id,))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

    def updateProductModel(self, data):
        conn = self.db.get_connection()
        if not conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            cursor = conn.cursor()
            hinh_anh = ", ".join(data['hinh_anh'])
            query = "UPDATE sanpham SET ten_sp = %s, ma_sp = %s, mo_ta = %s, loai_san_pham = %s, gia_ban = %s, hinh_anh = %s, kich_thuoc = %s, mau_sac = %s WHERE id = %s"
            cursor.execute(query, (data['ten_sp'], data['ma_sp'], data['mo_ta'], data['loai_sp'], self.commonDef.unformat_number(data['gia_ban']),  hinh_anh, data['kich_thuoc'], data['mau_sac'], data['id']))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")