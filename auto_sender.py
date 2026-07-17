#!/usr/bin/env python3
import sys
import asyncio
from telethon import TelegramClient, sessions
from telethon.errors import FloodWaitError

# Force logs to appear immediately in Render
sys.stdout.reconfigure(line_buffering=True)

print("🚀 Worker starting...", flush=True)

# ============================================================
# 🔐 YOUR CREDENTIALS (hardcoded)
# ============================================================
API_ID = 36705427
API_HASH = 'e69a36dc2b8c258d36d0d31c854d4aa7'
PHONE_NUMBER = '+447881257902'

# ⭐ NEW session string (exclusive to this Render worker)
SESSION_STRING = '1BJWap1sBuyUAH3Ml0mXJ3UystDiO4ogrcpDYf8qkauPK0nwJHff6ML9CQ91KnYsc6jFkZRji2YakZ6SzVWbIJRkz3GvfKbDb2DOL1dFmkSEE5WrOStnDmp2SkO6IBcNjsuPtfm4dGr0DuDFwsPOwAoE7szShP_9t5fVqKEp2PKJYrYzqTSNHtR8Q8fwGlfFnEExIqaOxBLd-Gen3hxPVi_ZnaSGx8AY3VvgSuglBLohTspclcfVE22wHHDN38RbHF-pEIRDTgy8WO-pwewv8TvenONxMw--CYtJijhcHkRikTK7CnDgEYmuZyd3utZZzqMhj_7kQ517fzTBnLkujkrbv2o9AHBw='

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
