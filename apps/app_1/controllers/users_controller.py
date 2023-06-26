from typing import Dict
from flask import render_template
import requests
import os


class UsersController:
    def __init__(self):
        self.url_base = os.environ.get("DB_API_URL")

    def index(self):
        return render_template("views/users/index.html", title="Users Table")

    def data(self):
        url = f"{self.url_base}/users?skip=0&limit=10"
        response = requests.get(url)
        response_json = response.json()
        rtn = {
            "data": response_json,
            "total": len(response_json)
        }

        return rtn

    def get_user_by_id(self, user_id: str) -> Dict:
        url = f"{self.url_base}/users/q?user_id={user_id}"
        response = requests.get(url)
        response_json = response.json()

        return response_json
