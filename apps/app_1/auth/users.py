from ..modules.encrypter_module import Encrypter
import requests
import jwt
import os


class User:
    def __init__(self, jwt_token):
        _jwt_key = os.environ.get("JWT_KEY")
        _jwt_algorithm = os.environ.get("JWT_ALGORITHM")
        _url_base = os.environ.get("DB_API_URL")
        _decrypter_key = os.environ.get("CRYPTO_KEY").encode()
        _decrypter = Encrypter(key=_decrypter_key)

        self._token = jwt_token

        _decoded_jwt = jwt.decode(jwt=self._token, key=_jwt_key, algorithms=[_jwt_algorithm])["info"]
        _decoded_data = _decrypter.decrypt(encrypted_text=_decoded_jwt)

        self._user_mail = _decoded_data["user_id"]
        self._roles = _decoded_data["roles"]

        _url = f"{_url_base}/users/q?user_email={self._user_mail}"
        _response = requests.get(_url).json()

        self._is_active = _response["IsActive"]
        self._fullname = _response["FullName"]

    @property
    def is_authenticated(self) -> bool:
        return True

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def is_anonymous(self) -> bool:
        return False

    @property
    def roles_list(self):
        return self._roles

    @property
    def fullname(self) -> str:
        return self._fullname

    @property
    def user_email(self) -> str:
        return self._user_mail

    def get_id(self) -> str:
        return self._token



