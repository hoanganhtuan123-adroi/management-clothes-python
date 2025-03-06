from database import Database
class SanPhamModel:
    def __init__(self):
        self.db = Database()
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
                        "so_luong_con": product[6],
                        "hinh_anh": product[7],
                        "kich_thuoc": product[8],
                        "mau_sac": product[9]
                    }
                    products_list.append(product_list)
            cursor.close()
            return products_list
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

md = SanPhamModel()
print(md.getAllProductsModel())