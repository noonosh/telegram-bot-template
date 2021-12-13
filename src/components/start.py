from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    update.effective_message.reply_text("This is a reply for start command!")
