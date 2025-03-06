from database import Database
from models.userModel import UserModel
from views.loginView import LoginView
from controllers.loginController import LoginController
def main():
    db = Database()
    user_model = UserModel(db)
    view = LoginView()
    LoginController(view, user_model)
    view.mainloop()

if __name__ == "__main__":
    main()