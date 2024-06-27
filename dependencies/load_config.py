import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
API_URL_V3 = os.getenv("API_URL_V3")
API_URL_V2 = os.getenv("API_URL_V2")
MESSAGE_CONTENT = os.getenv("MESSAGE_CONTENT")
MESSAGE_FILE_PATH = os.getenv("MESSAGE_FILE_PATH")
IMAGE_FILE_PATH = os.getenv("IMAGE_FILE_PATH")
SEND_ALL_USERS = os.getenv("SEND_ALL_USERS")
SEND_USER_LIST = os.getenv("SEND_USER_LIST")
SEND_MESSAGE_TEXT = os.getenv("SEND_MESSAGE_TEXT")
SEND_MESSAGE_WITH_IMAGE = os.getenv("SEND_MESSAGE_WITH_IMAGE")