from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

MYSQL_PASSCODE = os.getenv("MYSQL_PASSCODE")
MYSQL_USER = os.getenv("MYSQL_USER")