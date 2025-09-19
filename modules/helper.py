import os
import platform
import subprocess

def take_photo():
    # simulation for Termux / Android
    return "📸 Photo captured! (simulation)"

def record_video():
    return "🎥 Video recorded! (simulation)"

def screenshot():
    return "🖼️ Screenshot taken! (simulation)"

def list_files(path="."):
    try:
        files = os.listdir(path)
        return "\n".join(files)
    except Exception as e:
        return f"❌ Error: {e}"

def get_contacts():
    # simulation
    return "📞 Contacts fetched! (simulation)"

def send_sms(number, message):
    # simulation
    return f"💬 SMS sent to {number} (simulation)"

def get_location():
    # simulation
    return "📡 Location fetched! (simulation)"

def volume_control(action):
    # action = increase/decrease/mute
    return f"🔊 Volume {action} (simulation)"

def lock_screen():
    return "🔒 Screen locked! (simulation)"

def auto_type(text):
    return f"⌨️ Typed text: {text} (simulation)"

def device_info():
    return f"Device: {platform.node()}\nSystem: {platform.system()} {platform.release()}\nPlatform: {platform.platform()}"

def battery_status():
    return "🔋 Battery status fetched! (simulation)"

def network_status():
    return "🌐 Network status fetched! (simulation)"
