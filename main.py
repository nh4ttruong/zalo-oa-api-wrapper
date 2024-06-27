import requests
import json
from dependencies.messages import *
from dependencies.users import *
from dependencies.upload import *
from dependencies.load_config import *

if __name__ == "__main__":  
    user_id = "7186086631826132217" # truongtbn

    ## send message to 7186086631826132217
    # user_id = "7186086631826132217"
    # message_text = "Hello, this is a test message"

    # send_message(access_token, user_id, message_file="message.txt")    

    # upload image
    # attachment_id = upload_media(ACCESS_TOKEN, file_path=IMAGE_FILE_PATH, type="image")

    ## send message with image
    # users = [{"user_id": user} for user in user_id.split(",")]
    # send_message_to_users(ACCESS_TOKEN, users, message_text=MESSAGE_CONTENT, message_file=MESSAGE_FILE_PATH, image_file=IMAGE_FILE_PATH)

    if SEND_ALL_USERS == 'True':
        print("SEND_ALL_USERS: ", SEND_ALL_USERS)
        users = get_all_users(ACCESS_TOKEN)
        print("users: ", users)
    elif SEND_USER_LIST != None:
        print("SEND_USER_LIST: ", SEND_USER_LIST)
        users = [{"user_id": user.strip()} for user in SEND_USER_LIST.split(",")]
        print("users: ", users)

    if SEND_MESSAGE_TEXT == 'True':
        if SEND_MESSAGE_WITH_IMAGE == 'True':
            print("SEND_MESSAGE_WITH_IMAGE: ", SEND_MESSAGE_WITH_IMAGE)
            send_message_to_users(ACCESS_TOKEN, users, message_file=MESSAGE_FILE_PATH, image_file=IMAGE_FILE_PATH)
        else:
            print("SEND_MESSAGE_TEXT: ", SEND_MESSAGE_TEXT)
            send_message_to_users(ACCESS_TOKEN, users, message_file=MESSAGE_FILE_PATH)
    elif SEND_MESSAGE_WITH_IMAGE == 'True':
        send_message_to_users(ACCESS_TOKEN, users, message_file=MESSAGE_FILE_PATH, image_file=IMAGE_FILE_PATH)
    else:
        print("No message to send")
        exit()