import os
import datetime
from telegram.ext import Update

# Log unauthorized access
def log_unauthorized(update: Update):
    username = update.effective_user.username
    chat_id = update.effective_chat.id
    with open("logs/unauthorized.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - Unauthorized access by {username} ({chat_id})\n")

# Camera
def take_photo(cam=0):
    try:
        file_path = f"logs/photo_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
        os.system(f"termux-camera-photo -c {cam} {file_path}")
        return file_path
    except Exception as e:
        return None

# TODO: add more helper functions: video, screenshot, flashlight, volume, screen lock, battery info, shell commands, location, files, media, reminder
