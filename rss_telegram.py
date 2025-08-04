import os
from telethon import TelegramClient
from dotenv import load_dotenv
import json
from datetime import datetime
import subprocess

# Teszt komment - Source Control gombokkal!

# --- 1. Betöltjük a .env fájlt ---
load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

# --- 2. Telethon kliens ---
client = TelegramClient('rss_session', API_ID, API_HASH)

# --- 3. JSON feed létrehozása ---
def create_rss(messages):
    # Create JSON feed structure (compatible with JSON Feed spec)
    feed = {
        "version": "https://jsonfeed.org/version/1.1",
        "title": f"Telegram feed: {CHANNEL_USERNAME}",
        "home_page_url": f"https://t.me/{CHANNEL_USERNAME}",
        "feed_url": f"https://plaszeb.github.io/telegram-rss-feed/rss_feed.json",
        "description": "Generated from Telegram using Telethon",
        "author": {
            "name": f"@{CHANNEL_USERNAME}"
        },
        "items": []
    }

    for msg in messages:
        if not msg.message:
            continue
        
        item = {
            "id": f"https://t.me/{CHANNEL_USERNAME}/{msg.id}",
            "url": f"https://t.me/{CHANNEL_USERNAME}/{msg.id}",
            "title": msg.message[:50] + ("..." if len(msg.message) > 50 else ""),
            "content_text": msg.message,
            "date_published": msg.date.isoformat() + "Z"
        }
        feed["items"].append(item)

    # Write JSON file
    with open("rss_feed.json", "w", encoding="utf-8") as f:
        json.dump(feed, f, ensure_ascii=False, indent=2)

# --- 4. GitHub Pages feltöltés ---
def upload_to_github():
    # When running in GitHub Actions, this will be handled by the workflow
    # So we'll just print a message
    print("JSON feed generated successfully. GitHub Actions will handle the upload.")

# --- 5. Fő folyamat ---
async def main():
    await client.start()
    messages = await client.get_messages(CHANNEL_USERNAME, limit=50)
    create_rss(messages)
    upload_to_github()
    print("JSON feed frissítve és feltöltve a GitHub Pages-re.")

with client:
    client.loop.run_until_complete(main())
