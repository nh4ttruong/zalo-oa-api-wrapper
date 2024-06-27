import requests
import json
import os
from dependencies.load_config import *

def upload_media(access_token, file_path, type="image"):
    file_path = os.path.abspath(file_path)

    if type == "image":
        url = API_URL_V2 + "upload/image"
    elif type == "gif":
        url = API_URL_V2 + "upload/gif"
    else:
        raise ValueError("Invalid media type")

    headers = {
        "access_token": access_token
    }
    files = {
        "file": open(file_path, "rb")
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        response_json = response.json()
        if response_json["error"] == 0:
            return response_json["data"]["attachment_id"]
        else:
            raise Exception("Upload failed: {}".format(response_json["message"]))
    else:
        raise Exception("Upload failed: {}".format(response.status_code))