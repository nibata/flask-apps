from flask_login import LoginManager
from ..controllers.users_controller import UsersController

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: str):
    user = UsersController().get_user_by_id(user_id=user_id)
    return user
