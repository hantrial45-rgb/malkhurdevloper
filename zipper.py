# import os
# import zipfile
# from telegram import Update
# from telegram.ext import ContextTypes
# from io import BytesIO

# from telethon import TelegramClient
# from telethon.sessions import StringSession
# from telethon.errors import (
#     SessionPasswordNeededError,
#     FloodWaitError,
#     AuthKeyError,
#     PhoneCodeInvalidError,
#     UserDeactivatedBanError,
#     UserDeactivatedError,
#     UserMigrateError,
# )

# from handlers.account import BLOCKED_USER_IDS
# from config import API_ID, API_HASH


# async def is_valid_session(session_path: str) -> bool:
#     try:
#         client = TelegramClient(session_path, API_ID, API_HASH)
#         await client.connect()
#         if not await client.is_user_authorized():
#             await client.disconnect()
#             return False
#         await client.disconnect()
#         return True
#     except (AuthKeyError, PhoneCodeInvalidError, UserDeactivatedBanError,
#             UserDeactivatedError, FloodWaitError, UserMigrateError):
#         return False
#     except Exception:
#         return False


# async def download_sessions(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id

#     # 🚫 Silently ignore users not in admin list
#     if user_id not in BLOCKED_USER_IDS:
#         return

#     # ✅ Proceed for allowed users
#     if len(context.args) == 0:
#         await update.message.reply_text("Please provide a country code. Example: /download_sessions +880")
#         return

#     country_code = context.args[0].lower()
#     session_dir = f"sessions/{country_code}"

#     if not os.path.exists(session_dir):
#         await update.message.reply_text(f"No session folder found for: {country_code}")
#         return

#     zip_buffer = BytesIO()
#     valid_count = 0

#     with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
#         for root, _, files in os.walk(session_dir):
#             for file in files:
#                 file_path = os.path.join(root, file)

#                 # Check validity
#                 if await is_valid_session(file_path):
#                     arcname = os.path.relpath(file_path, session_dir)
#                     zipf.write(file_path, arcname)
#                     valid_count += 1

#     if valid_count == 0:
#         await update.message.reply_text("❌ No valid sessions found to download.")
#         return

#     zip_buffer.seek(0)
#     await update.message.reply_document(
#         document=zip_buffer,
#         filename=f"{country_code}_valid_sessions.zip",
#         caption=f"✅ {valid_count} valid {country_code.upper()} sessions"
#     )

# my production code


import os
import zipfile
import json
from telegram import Update
from telegram.ext import ContextTypes
from io import BytesIO

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import (
    SessionPasswordNeededError,
    FloodWaitError,
    AuthKeyError,
    PhoneCodeInvalidError,
    UserDeactivatedBanError,
    UserDeactivatedError,
    UserMigrateError,
)

from handlers.account import BLOCKED_USER_IDS
from config import API_ID, API_HASH


async def is_valid_session(session_path: str) -> bool:
    """
    Checks if a Telegram session is valid by connecting to it.
    """
    try:
        client = TelegramClient(session_path, API_ID, API_HASH)
        await client.connect()
        if not await client.is_user_authorized():
            await client.disconnect()
            return False
        await client.disconnect()
        return True
    except (AuthKeyError, PhoneCodeInvalidError, UserDeactivatedBanError,
            UserDeactivatedError, FloodWaitError, UserMigrateError):
        return False
    except Exception:
        return False


async def download_sessions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Downloads all valid sessions for a given country code, including their
    corresponding JSON files, and sends them as a single ZIP file.
    """
    user_id = update.effective_user.id

    # 🚫 Silently ignore users not in admin list
    if user_id not in BLOCKED_USER_IDS:
        return

    # ✅ Proceed for allowed users
    if len(context.args) == 0:
        await update.message.reply_text("Please provide a country code. Example: /download_sessions +880")
        return

    country_code = context.args[0].lower()
    session_dir = f"sessions/{country_code}"

    if not os.path.exists(session_dir):
        await update.message.reply_text(f"No session folder found for: {country_code}")
        return

    zip_buffer = BytesIO()
    valid_count = 0

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(session_dir):
            for file in files:
                if file.endswith('.session'):
                    session_path = os.path.join(root, file)
                    json_path = os.path.join(
                        root, f"{file.replace('.session', '.json')}")

                    # Check validity of the .session file
                    if await is_valid_session(session_path):
                        # Add the .session file to the zip
                        arcname = os.path.relpath(session_path, session_dir)
                        zipf.write(session_path, arcname)
                        valid_count += 1

                        # If a corresponding .json file exists, add it as well
                        if os.path.exists(json_path):
                            json_arcname = os.path.relpath(
                                json_path, session_dir)
                            zipf.write(json_path, json_arcname)

    if valid_count == 0:
        await update.message.reply_text("❌ No valid sessions found to download.")
        return

    zip_buffer.seek(0)
    await update.message.reply_document(
        document=zip_buffer,
        filename=f"{country_code}_valid_sessions.zip",
        caption=f"✅ {valid_count} valid {country_code.upper()} sessions  (including their JSON files) "
    )
