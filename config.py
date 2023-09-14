from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
AUTH_SECRET = os.environ.get("AUTH_SECRET")
RESET_PASS_SECRET = os.environ.get("RESET_PASS_SECRET")