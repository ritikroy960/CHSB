from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Replace these with your own values
api_id = '1438953'
api_hash = '96f1dcc409aa62f5762e8f75e57834d9'

def main():
    print("Press Ctrl+C to stop this script")
    with TelegramClient(StringSession(), api_id, api_hash) as client:
        print("Session string:", client.session.save())
        client.run_until_disconnected()

if __name__ == "__main__":
    main()
