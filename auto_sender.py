#!/usr/bin/env python3
import sys
import asyncio
from telethon import TelegramClient, sessions
from telethon.errors import FloodWaitError

sys.stdout.reconfigure(line_buffering=True)
print("🚀 Worker starting...", flush=True)

# ============================================================
API_ID = 36705427
API_HASH = 'e69a36dc2b8c258d36d0d31c854d4aa7'
PHONE_NUMBER = '+447881257902'

# ✅ Your new session string (exclusive to this Render worker)
SESSION_STRING = '1BJWap1sBu6vMhkoMLYSKRtnf0ZALQZzw0RTq8ea_LCtGldQ79H6cNxNXdzKNI57_noGzT8Y-ci5VbcbzAQP75VhUq1W2Gp8tiL3CootytrX4m84r0D0iEyJZlukRhN9ks5_xQMRpQhkVW3qEK-N-CdUNYeuiQB534HWoDyo9LcNh4A-Uvti1qf-lPvRUrzKw2jN0etwkchNK_ww1NfKVNfdLkPvNRa__uK3SxTdbHvEkwbXv_HXk1u-HvadgdM746AxfuqMWXV46Iil3QGrfhQ1b-V2Sg0h64t7WwocyRbJwd0PN96-Oymu5-nObfsha5w8grQTHF290cfh8uEEEos9u0_JPg94='

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
    client = TelegramClient(sessions.StringSession(SESSION_STRING), API_ID, API_HASH)
    await client.start(phone=PHONE_NUMBER)
    print("✅ Logged in successfully!", flush=True)

    try:
        chat = await client.get_entity(INVITE_LINK)
        print(f"✅ Target chat: {chat.title}", flush=True)
    except Exception as e:
        print(f"❌ Error finding chat: {e}", flush=True)
        return

    counter = 1
    print(f"🚀 Starting send loop (every {DELAY_SECONDS}s). Press Ctrl+C to stop.", flush=True)

    while True:
        try:
            full_msg = f"{MESSAGE_TEMPLATE}\n\n#{counter}"
            await client.send_message(chat, full_msg)
            print(f"✅ Sent message #{counter}", flush=True)
            counter += 1
            await asyncio.sleep(DELAY_SECONDS)
        except FloodWaitError as e:
            print(f"⏳ Flood wait: {e.seconds}s", flush=True)
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
