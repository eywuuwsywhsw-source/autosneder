#!/usr/bin/env python3
import sys
import asyncio
from telethon import TelegramClient, sessions
from telethon.errors import FloodWaitError

# Force Python to flush prints immediately (so Render logs show them)
# This works on Python 3.7+
sys.stdout.reconfigure(line_buffering=True)

print("🚀 Worker starting...", flush=True)

# ============================================================
# 🔐 YOUR CREDENTIALS (hardcoded)
# ============================================================
API_ID = 36705427
API_HASH = 'e69a36dc2b8c258d36d0d31c854d4aa7'
PHONE_NUMBER = '+447881257902'

# ⭐ The session string you generated earlier
SESSION_STRING = '1BJWap1sBu7Bl_IExUg758pVPDKo93Na5AfJyb7y7I0-i2a8oSTEAbWKf9YmUNQMaUHk7UtW72V2CZiVJAxfUpp-s01qfXEXYf8C82DFtdxo5ahX-W3RgtDveSMlJbloF99Ytjig7z4gBe2xl-uW3U8ltwoOVkhVTOZoX_QUnS4B_cNt-zUXBbefo_PtstyjwVd11eX8QkxedV6wg3oAvZ1szJrtyw8rYy7F021yufK1iQHnsfnTHqXxhd_YNrTgiklX6Is3_QjfQHJz8e6lxN7doI2sqk7C9fgc6Js-UVxZlu5MugqfqsTbeQUiujQuiOOAIxel8pz6H34PuTgWUFjYRexHK1SA='

INVITE_LINK = 'https://t.me/+XwxJN7zdcetiNDRl'
DELAY_SECONDS = 60   # 1 minute
# ============================================================

MESSAGE_TEMPLATE = """• UPI QR Generate(0.7$)
• Chat Gpt Plus 1Month On Mail($2.5)
• Netflix 1 Month on Mail (2.5$)

━━━━━━━━━
• Selling Chat Gpt Plus Method (8$)
• Selling Netflix 30days Trial Method (10$)
✅ Escrow Accepted
📩 DM to Buy @GPT_Providers"""

print("✅ Variables loaded", flush=True)


async def main():
    print("🔐 Connecting to Telegram...", flush=True)

    # Use StringSession – NO database file is created
    client = TelegramClient(sessions.StringSession(SESSION_STRING), API_ID, API_HASH)
    await client.start(phone=PHONE_NUMBER)

    print("✅ Logged in successfully!", flush=True)

    # Find the group
    print(f"📢 Fetching group: {INVITE_LINK}", flush=True)
    try:
        chat = await client.get_entity(INVITE_LINK)
        print(f"✅ Target chat: {chat.title}", flush=True)
    except Exception as e:
        print(f"❌ Error finding chat: {e}", flush=True)
        return

    counter = 1
    print(f"🚀 Starting send loop (every {DELAY_SECONDS} seconds). Press Ctrl+C to stop.", flush=True)

    while True:
        try:
            full_msg = f"{MESSAGE_TEMPLATE}\n\n#{counter}"
            await client.send_message(chat, full_msg)
            print(f"✅ Sent message #{counter}", flush=True)
            counter += 1
            await asyncio.sleep(DELAY_SECONDS)
        except FloodWaitError as e:
            print(f"⏳ Flood wait: {e.seconds} seconds. Sleeping...", flush=True)
            await asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}", flush=True)
            await asyncio.sleep(10)


if __name__ == '__main__':
    print("🏃 Running main()...", flush=True)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Stopped by user.", flush=True)
    except Exception as e:
        print(f"💥 Fatal error: {e}", flush=True)
        sys.exit(1)
