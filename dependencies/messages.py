import requests
import json
import time
from dependencies.load_config import *
from dependencies.upload import *

def send_text_message(access_token, user_id, message_text=None, message_file=None):
    url = API_URL_V3 + "message/cs"
    headers = {
        "Content-Type": "application/json",
        "access_token": access_token
    }
    data = {
        "recipient": {
            "user_id": user_id
        },
        "message": {}
    }

    if message_text and message_file:
        raise ValueError("Both message_text and message_file cannot be provided at the same time")
    elif message_text:
        data["message"]["text"] = message_text
    elif message_file:
        with open(message_file, "r") as f:
            data["message"]["text"] = f.read()
    else:
        raise ValueError("Either message_text or message_file must be provided")

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return print(response.json())
    if response.status_code == 200:
        return True
    else:
        return False

def send_message_with_image(access_token, user_id, message_text=None, message_file=None, url=None, attachment_id=None, width=None, height=None):
    url_api = API_URL_V3 + "message/cs"
    headers = {
        "Content-Type": "application/json",
        "access_token": access_token
    }
    data = {
        "recipient": {
            "user_id": user_id
        },
        "message": {}
    }

    if message_text and message_file:
        raise ValueError("Both message_text and message_file cannot be provided at the same time")
    elif message_text:
        data["message"]["text"] = message_text
    elif message_file:
        with open(message_file, "r") as f:
            data["message"]["text"] = f.read()
    else:
        raise ValueError("Either message_text or message_file must be provided")

    if url and attachment_id:
        raise ValueError("Only one of url or attachment_id can be provided")
    elif url or attachment_id:
        data["message"]["attachment"] = {
            "type": "template",
            "payload": {
                "template_type": "media",
                "elements": [{
                    "media_type": "image"
                }]
            }
        }
        if url:
            data["message"]["attachment"]["payload"]["elements"][0]["url"] = url
        if attachment_id:
            data["message"]["attachment"]["payload"]["elements"][0]["attachment_id"] = attachment_id
        if width:
            data["message"]["attachment"]["payload"]["elements"][0]["width"] = width
        if height:
            data["message"]["attachment"]["payload"]["elements"][0]["height"] = height

    response = requests.post(url_api, headers=headers, data=json.dumps(data))

    return response.status_code == 200

def send_message_to_users(access_token, users, message_text=None, message_file=None, url=None, image_file=None, image_type="image", width=None, height=None):
    total_users = len(users)
    send_type = None

    if image_file != None and url != None:
        raise ValueError("Only one of image_file or url can be provided")
    elif image_file != None or image_file != "":
        send_type = "text_with_image"
    elif url != None or url != "":
        send_type = "text_with_image"
    else:
        send_type = "text"

    attachment_ids = {}

    for user in users:
        user_id = user["user_id"]
        print("({}/{})".format(users.index(user) + 1, total_users), "Sending message to user: ", user_id)
        
        if send_type == "text":
            send_text_message(access_token, user_id, message_text=message_text, message_file=message_file)
            time.sleep(0.1)
        elif send_type == "text_with_image":
            if image_file in attachment_ids:
                attachment_id = attachment_ids[image_file]
            else:
                attachment_id = upload_media(access_token, file_path=image_file, type=image_type)
                attachment_ids[image_file] = attachment_id

            send_message_with_image(access_token, user_id, message_text=message_text, message_file=message_file, url=url, attachment_id=attachment_id, width=width, height=height)
            
    return True