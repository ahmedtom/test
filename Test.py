from pyrogram import Client, filters
import os

BOT_USERNAME = os.getenv("Tomyy_0bot")
API_ID = 9157919
API_HASH = "b90c282e584222babde5f68b5b63ee3b"
BOT_TOKEN = os.getenv("5921031219:AAHgPZysStwEE6APKt9W2oOaDfsDDtLi9mE")

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    bot_username=BOT_USERNAME
)

@app.on_message(filters.group & filters.text & filters.command("change") & filters.user("me"))
def change_group_name(client, message):
    new_name = message.text.split("/change ", 1)[1]
    chat_id = message.chat.id
    client.set_chat_title(chat_id, new_name)

@app.on_message(filters.channel & filters.text & filters.command("change") & filters.user("me"))
def change_channel_name(client, message):
    new_name = message.text.split("/change ", 1)[1]
    chat_id = message.chat.id
    client.edit_channel(channel_id=chat_id, title=new_name)

@app.on_message(filters.private & filters.text & ~filters.command)
def echo(client, message):
    message.reply_text(message.text)

app.run()


