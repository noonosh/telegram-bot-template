import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 <b>Hello and welcome!</b>\n\n"
        "📩 <b>Send a message to contact admin anonymously.</b>",
        parse_mode="HTML"
    )

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text
    if user and text:
        msg = f"📩 From @{user.username or 'no username'} (ID: {user.id}):\n\n{text}"
        await context.bot.send_message(chat_id=ADMIN_ID, text=msg)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))
    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
