from dotenv import dotenv_values

config = dotenv_values(".env")

API_URL_V2 = config["API_URL_V2"]
API_URL_V3 = config["API_URL_V3"]
ZALO_OA_ACCESS_TOKEN = config["ZALO_OA_ACCESS_TOKEN"]
SEND_ALL_USERS = config["SEND_ALL_USERS"]
SEND_USER_LIST = config["SEND_USER_LIST"]
SEND_MESSAGE_TEXT = config["SEND_MESSAGE_TEXT"]
SEND_MESSAGE_WITH_IMAGE = config["SEND_MESSAGE_WITH_IMAGE"]
MESSAGE_FILE_PATH = config["MESSAGE_FILE_PATH"]
IMAGE_FILE_PATH = config["IMAGE_FILE_PATH"]
MESSAGE_CONTENT = config["MESSAGE_CONTENT"]
