from http.server import BaseHTTPRequestHandler, HTTPServer
from config import PERMISSION_SERVER_PORT, CHAT_ID, BOT_TOKEN
import telegram

bot = telegram.Bot(token=BOT_TOKEN)

PERMISSION_GRANTED = False  # Initially False

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global PERMISSION_GRANTED
        if self.path == "/grant":
            PERMISSION_GRANTED = True
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(b"<h1>Permission Granted ✅</h1>")
            # Notify via Telegram
            bot.send_message(chat_id=CHAT_ID, text="✅ Permission granted by target device.")
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    server_address = ('', PERMISSION_SERVER_PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"🌐 Permission server running at http://<TARGET_IP>:{PERMISSION_SERVER_PORT}/grant")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
