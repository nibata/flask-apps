import jwt
import os
import requests


class User:
    def __init__(self, jwt_token):
        _jwt_key = os.environ.get("JWT_KEY")
        _jwt_algorithm = os.environ.get("JWT_ALGORITHM")
        _url_base = os.environ.get("DB_API_URL")
        self._token = jwt_token

        _decoded_jwt = jwt.decode(jwt=self._token, key=_jwt_key, algorithms=[_jwt_algorithm])

        self._user_mail = _decoded_jwt["user_id"]
        self._roles = _decoded_jwt["roles"]

        _url = f"{_url_base}/users/q?user_email={self._user_mail}"
        _response = requests.get(_url)
        self._response_json = _response.json()

    @property
    def is_authenticated(self) -> bool:
        return True

    @property
    def is_active(self) -> bool:
        return self._response_json["is_active"]

    @property
    def is_anonymous(self) -> bool:
        return False

    @property
    def roles_list(self):
        return self._roles

    @property
    def fullname(self) -> str:
        return self._response_json["fullname"]

    @property
    def user_email(self) -> str:
        return self._user_mail

    def get_id(self) -> str:
        return self._token



