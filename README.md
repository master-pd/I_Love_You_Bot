# 💖 I LOVE YOU BOT  

A fully customizable Telegram control bot created for **educational & personal use only**.  
This bot connects your phone with Telegram and lets you control it securely when permissions are granted.  

---

## 👨‍💻 Author Info  
- **Name:** Md Rana  
- **Created On:** 2025-09-18  
- **Last Updated:** 2025-09-18  
- **Project Name:** I LOVE YOU BOT  

---

## ✨ Features  

- 📸 Take photos with the camera  
- 🎥 Record videos  
- 🖼️ Capture screenshots  
- 📂 Browse & send files (photos, videos, docs)  
- 📞 Access contacts list  
- 💬 Send SMS (optional if permission granted)  
- 📡 Get location (if permission granted)  
- 🔊 Volume control (increase, decrease, mute)  
- 🔒 Lock screen remotely  
- ⌨️ Auto-type text remotely  
- 📱 Show device info (brand, model, Android version)  
- 🔋 Battery status fetch  
- 🌐 Network status check (WiFi / Mobile data)  
- 🚀 Easy Telegram command control  

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/master-pd/I_Love_You_Bot.git
cd ILoveYou-Bot
```

2️⃣ Install dependencies

Create requirements.txt with:
```
python-telegram-bot==20.3
requests
```
Then run:
```
pip install -r requirements.txt
```
3️⃣ Configure your bot

Create config.py with:

# Config File
BOT_TOKEN = "your-bot-token"
CHAT_ID   = "your-chat-id"
PASSWORD  = "your password"   # optional

4️⃣ Run the bot
```
python bot.py


```
🎮 Usage (Telegram Commands)

Command	Action

/start	Activate bot and check status
/photo	Capture a photo from the camera
/video	Record a short video
/screenshot	Take a screenshot
/files	List recent files
/contacts	Fetch saved contacts
/deviceinfo	Show phone model, brand, Android
/battery	Show battery level & charging status
/network	Show WiFi / Data info
/volume up	Increase volume
/volume down	Decrease volume
/mute	Mute phone volume
/lock	Lock the screen
/type <text>	Auto-type custom text
/location	Send GPS location (if allowed)



---

⚠️ Disclaimer

This project is for personal and educational use only.
Do not use it for illegal or unauthorized purposes.
The author is not responsible for any misuse.

## ONE CLICK SETUP ✅

```bash
pkg update -y && pkg upgrade -y
pkg install python git -y
git clone https://github.com/master-pd/I_Love_You_Bot.git
cd ILoveYou-Bot
echo "python-telegram-bot==20.3
requests" > requirements.txt
pip install -r requirements.txt
```
```
echo "BOT_TOKEN = 'your-bot-token'" > config.py
echo "CHAT_ID = 'your-chat-id'" >> config.py
echo "PASSWORD = 'your password'" >> config.py

```
Run bot 
```
python bot.py
```
