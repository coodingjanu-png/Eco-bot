import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX", ">")

if not TOKEN:
    raise RuntimeError("TOKEN is missing from .env")
