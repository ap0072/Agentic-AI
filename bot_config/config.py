import os
from dotenv import load_dotenv

load_dotenv()

MICROSOFT_APP_ID = os.getenv("MICROSOFT_APP_ID")
MICROSOFT_APP_PASSWORD = os.getenv("MICROSOFT_APP_PASSWORD")

