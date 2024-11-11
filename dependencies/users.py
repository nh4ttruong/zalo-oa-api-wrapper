import requests
import json
from dependencies.load_config import *

def get_users(ZALO_OA_ACCESS_TOKEN, offset=0, count=50, is_follower=True):
    url = API_URL_V3 + "user/getlist"
    headers = {"ZALO_OA_ACCESS_TOKEN": ZALO_OA_ACCESS_TOKEN}
    data = {"offset": offset, "count": count, "is_follower": is_follower}

    response = requests.get(url, headers=headers, params={"data": json.dumps(data)})
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_all_users(ZALO_OA_ACCESS_TOKEN, type="all"):
    offset = 0
    count = 50
    users = []

    # get followers is not followers is_follower = False
    if type == "follower":
        is_follower = True
    elif type == "not_follower":
        is_follower = False
    elif type == "all":
        # get two above type recursively
        follower_users = get_all_users(ZALO_OA_ACCESS_TOKEN, type="follower")
        not_follower_users = get_all_users(ZALO_OA_ACCESS_TOKEN, type="not_follower")

        users.extend(follower_users)
        users.extend(not_follower_users)

        return users
        
    while True:
        response = get_users(ZALO_OA_ACCESS_TOKEN, offset, count, is_follower=is_follower)

        if response is None:
            break
        if len(response["data"]["users"]) == 0:
            break
        users.extend(response["data"]["users"])
        offset += count

    print("Total {} users: {}".format(type, len(users)))
    return users

def get_user_detail(ZALO_OA_ACCESS_TOKEN, user_id):
    url = API_URL_V3 + "user/detail"

    headers = {
        "ZALO_OA_ACCESS_TOKEN": ZALO_OA_ACCESS_TOKEN
    }
    params = {
        "data": json.dumps({"user_id": user_id})
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None