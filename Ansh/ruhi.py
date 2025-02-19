fro pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot settings
API_ID = "14050586"
API_HASH = "42a60d9c657b106370c79bb0a8ac560c"
BOT_TOKEN = "7704975537:AAHMJaooLtGkzwUpwKkQyxOoc_HstCJk1bU"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Start command
@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    # Welcome image file path or URL
    welcome_image_url = "https://envs.sh/9ul.jpg"  # Replace with your image URL or local file path

    # Inline buttons
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("👤 Owner", url="https://t.me/YourUsername"),
                InlineKeyboardButton("🛠 Support", url="https://t.me/SupportGroupLink")
            ],
            [
                InlineKeyboardButton("❓ Problem", url="https://t.me/YourHelpBot")
            ]
        ]
    )

    # Send welcome message with image and buttons
    await client.send_photo(
        chat_id=message.chat.id,
        photo=welcome_image_url,
        caption="👋 **Welcome to the Bot!**\n\nUse the buttons below for support or to contact the owner.",
        reply_markup=keyboard
    )

# Run the bot
app.run()