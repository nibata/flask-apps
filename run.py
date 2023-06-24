from werkzeug.serving import run_simple
from app import apps_pool

if __name__ == "__main__":
    run_simple(hostname="127.0.0.1", port=5000, application=apps_pool)
