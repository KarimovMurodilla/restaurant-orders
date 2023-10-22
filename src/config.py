from pathlib import Path
from environs import Env

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

# Status
TESTING = env.bool("TESTING")

# Actually I use postgresql in production, but in tz sayed sqlite3
DATABASE_URL = f"sqlite+aiosqlite:///{BASE_DIR}/database.db"

# Test
DATABASE_URL_TEST = f"sqlite+aiosqlite:///{BASE_DIR}/test.db"

SECRET = env.str("SECRET")