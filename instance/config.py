from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
APP_NAME = os.environ.get("APP_NAME")
DB_API_URL = os.environ.get("DB_API_URL")
JWT_KEY = os.environ.get("JWT_KEY")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")
BABEL_DEFAULT_LOCALE = os.environ.get("BABEL_DEFAULT_LOCALE")
CRYPTO_KEY = os.environ.get("CRYPTO_KEY").encode()
