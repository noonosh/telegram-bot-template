from telegram import Update
from telegram.ext import ContextTypes
from utils.text import text


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # This callback function just replies back with a greeting message from app.json texts
    await update.effective_message.reply_text(text('start'),
                                              parse_mode='HTML')
