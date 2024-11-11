import requests
import json
from dependencies.messages import *
from dependencies.users import *
from dependencies.upload import *
from dependencies.load_config import *

# User ID of the recipient
user_id = "7186086631826132217"
message_text = "Hello, this is a test message"

# Send a text message to the specified user
send_text_message(ZALO_OA_ACCESS_TOKEN, user_id, message_text)