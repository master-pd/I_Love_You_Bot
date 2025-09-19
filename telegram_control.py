# telegram_control.py
import os
import sys
import requests
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from modules.helper import *
import webbrowser

# Load config
try:
    from config import BOT_TOKEN, CHAT_ID, PASSWORD
except ImportError:
    print("❌ config.py not found or BOT_TOKEN/CHAT_ID/PASSWORD missing!")
    sys.exit(1)

bot = Bot(token=BOT_TOKEN)

# Global permission flag
permission_granted = False

# Generate permission link (open on spare phone)
PERMISSION_LINK = "https://your-permission-link.com"  # Replace with your real link

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_chat.id) != str(CHAT_ID):
        await update.message.reply_text("❌ Unauthorized user")
        return
    await update.message.reply_text("Welcome! Send /link to generate permission link.")

async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_chat.id) != str(CHAT_ID):
        await update.message.reply_text("❌ Unauthorized user")
        return
    await update.message.reply_text(f"Open this link on your spare phone and allow permissions:\n{PERMISSION_LINK}")

async def check_permission(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global permission_granted
    # Here you would implement your real permission check logic
    # For demo purposes, let's assume permission is granted manually
    permission_granted = True
    await update.message.reply_text("✅ Permission granted! You can now control the phone.")

async def take_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not permission_granted:
        await update.message.reply_text("❌ Permission not granted!")
        return
    photo_path = take_camera_photo()  # From helper.py
    if photo_path:
        await update.message.reply_photo(photo=open(photo_path, 'rb'))
    else:
        await update.message.reply_text("❌ Failed to take photo")

async def get_device_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not permission_granted:
        await update.message.reply_text("❌ Permission not granted!")
        return
    info = get_device_info()  # From helper.py
    await update.message.reply_text(info)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Unknown command")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("link", link))
    app.add_handler(CommandHandler("grant", check_permission))
    app.add_handler(CommandHandler("photo", take_photo))
    app.add_handler(CommandHandler("info", get_device_info))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))
    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
