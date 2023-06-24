from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
APP_NAME = os.environ.get("APP_NAME")
