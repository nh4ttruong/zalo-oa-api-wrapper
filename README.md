# Zalo OA API Wrapper

A simple API script for interacting with the [Zalo Official Account (OA)](https://oa.zalo.me/). This script provides an easy-to-use interface to manage users, retrieve user information, send and receive messages, and more. Ideal for automating interactions with your Zalo OA and building customer engagement tools.

## Features
- Get User List: Retrieve a list of users who have interacted with the OA.
- User Information: Fetch detailed information about a specific user.
- Send Message: Send various types of messages (text, image) to users.
- Receive Messages: Get messages sent to the OA.

## Installation
1. Clone the repo:
```bash
git clone https://github.com/nh4ttruong/zalo-oa-api.git
cd zalo-oa-api
```
2. Install Dependencies: Ensure you have Python 3.7+ and install required packages
```bash
pip install -r requirements.txt
```

## Usage
1. Obtain Zalo OA Access Token:
- Go to the [Zalo API Explorer](https://developers.zalo.me/tools/explorer)
- Choose **OA Access Token** and click **Get Access Token**
- Tick to allow Term of User and copy the generated** Access Token**.

2. Configure Your API Credentials: Add your Zalo OA API credentials in a `.env` file:
```bash
ZALO_OA_ZALO_OA_ACCESS_TOKEN=your_ZALO_OA_ACCESS_TOKEN
```

3. Run the Script with `python main.py`

4. Make API Calls: Use the available functions to interact with the Zalo API. See the [API Reference](https://developers.zalo.me/docs/official-account/bat-dau/kham-pha) and Examples for details.

## Examples

### Sending a Message to a Specific User

To send a message to a specific user (e.g., `user_id = "7186086631826132217"`):
```python
from dependencies.messages import *

# User ID of the recipient
user_id = "7186086631826132217"
message_text = "Hello, this is a test message"

# Send a text message to the specified user
send_text_message(ZALO_OA_ACCESS_TOKEN, user_id, message_text)
```

### Sending a Message with an Image

```python
from dependencies.messages import *
from dependencies.upload import *

# Specify the user ID(s) and message content
user_id = "7186086631826132217"
users = [{"user_id": user} for user in user_id.split(",")]
message_text = "Hello, here’s an image for you!"

# Upload the image and retrieve the attachment ID
attachment_id = upload_media(ZALO_OA_ACCESS_TOKEN, file_path=IMAGE_FILE_PATH, type="image")

# Send the message along with the image
send_message_to_users(ZALO_OA_ACCESS_TOKEN, users, message_text=message_text, image_file=IMAGE_FILE_PATH)
```

### Sending to All Users or a Specific List of Users

```python
from dependencies.messages import *
from dependencies.upload import *
from dependencies.users import *

# Check if all users should receive the message
if SEND_ALL_USERS == 'True':
    users = get_all_users(ZALO_OA_ACCESS_TOKEN)
else:
    # Use a comma-separated list of user IDs from SEND_USER_LIST in .env file
    users = [{"user_id": user.strip()} for user in SEND_USER_LIST.split(",")]

# Send text or image message based on configuration
if SEND_MESSAGE_TEXT == 'True':
    if SEND_MESSAGE_WITH_IMAGE == 'True':
        send_message_to_users(ZALO_OA_ACCESS_TOKEN, users, message_text=MESSAGE_CONTENT, image_file=IMAGE_FILE_PATH)
    else:
        send_message_to_users(ZALO_OA_ACCESS_TOKEN, users, message_text=MESSAGE_CONTENT)
elif SEND_MESSAGE_WITH_IMAGE == 'True':
    send_message_to_users(ZALO_OA_ACCESS_TOKEN, users, message_text=MESSAGE_CONTENT, image_file=IMAGE_FILE_PATH)
else:
    print("No message to send")
```

## Authors
- [@nh4ttruong](nh4ttruong.me)