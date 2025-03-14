from database import Database
class UserModel:
    def __init__(self, db: Database):
        self.db = db
        self.conn = self.db.get_connection()

    def authenticate(self, username: str, password: str) -> bool:

        if not self.conn:
            raise Exception("Lỗi kết nối cơ sở dữ liệu")
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM taikhoan WHERE tai_khoan = %s AND mat_khau = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            cursor.close()
            return user is not None
        except Exception as e:
            raise Exception(f"Lỗi trong quá trình xác thực: {e}")

