import os
from telethon import TelegramClient
from dotenv import load_dotenv
import xml.etree.ElementTree as ET
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

# --- 3. RSS fájl létrehozása ---
def create_rss(messages):
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = f"Telegram feed: {CHANNEL_USERNAME}"
    ET.SubElement(channel, "link").text = f"https://t.me/{CHANNEL_USERNAME}"
    ET.SubElement(channel, "description").text = "Generated from Telegram using Telethon"

    for msg in messages:
        if not msg.message:
            continue
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = msg.message[:50] + ("..." if len(msg.message) > 50 else "")
        ET.SubElement(item, "link").text = f"https://t.me/{CHANNEL_USERNAME}/{msg.id}"
        ET.SubElement(item, "description").text = msg.message
        ET.SubElement(item, "pubDate").text = msg.date.strftime('%a, %d %b %Y %H:%M:%S GMT')

    tree = ET.ElementTree(rss)
    tree.write("rss_feed.xml", encoding="utf-8", xml_declaration=True)

# --- 4. GitHub Pages feltöltés ---
def upload_to_github():
    # When running in GitHub Actions, this will be handled by the workflow
    # So we'll just print a message
    print("RSS feed generated successfully. GitHub Actions will handle the upload.")

# --- 5. Fő folyamat ---
async def main():
    await client.start()
    messages = await client.get_messages(CHANNEL_USERNAME, limit=50)
    create_rss(messages)
    upload_to_github()
    print("RSS feed frissítve és feltöltve a GitHub Pages-re.")

with client:
    client.loop.run_until_complete(main())
