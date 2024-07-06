from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv
import os

# Replace these with your own values
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

def main():
    print("Press Ctrl+C to stop this script")
    with TelegramClient(StringSession(), api_id, api_hash) as client:
        print("Session string:", client.session.save())
        client.run_until_disconnected()

if __name__ == "__main__":
    main()
