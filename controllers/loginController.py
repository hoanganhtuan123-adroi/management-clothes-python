from views.loginView import LoginView
from models.userModel import UserModel
from views.mainView import  MainView
class LoginController:
    def __init__(self, view: LoginView, user_model: UserModel):
        self.view = view
        self.user_model = user_model
        self.view.set_login_handler(self.login)

    def login(self):
        username = self.view.get_username()
        password = self.view.get_password()

        try:
            authenticated = self.user_model.authenticate(username, password)
            if authenticated:
                self.view.show_message("Thành công", "Đăng nhập thành công!")
                self.open_main_view()
            else:
                self.view.show_error("Thất bại", "Đăng nhập thất bại!")
        except Exception as e:
            self.view.show_error("Lỗi", f"Có lỗi xảy ra: {e}")

    def open_main_view(self):
        # Ẩn cửa sổ đăng nhập và mở giao diện chính
        self.view.withdraw()  # Ẩn cửa sổ đăng nhập
        main_view = MainView(master=self.view)
        main_view.grab_set()  # Đảm bảo giao diện chính nhận được sự kiện bàn phím và chuột
        # Khi giao diện chính đóng, đóng luôn cửa sổ đăng nhập
        main_view.protocol("WM_DELETE_WINDOW", self.on_main_view_close)

    def on_main_view_close(self):
        self.view.destroy()