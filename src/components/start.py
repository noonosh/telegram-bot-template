from telegram import Update
from telegram.ext import CallbackContext
from utils.text import text


def start(update: Update, context: CallbackContext):
    # This callback function just replies back with a greeting message from app.json texts
    update.effective_message.reply_text(text('start'),
                                        parse_mode='HTML')
