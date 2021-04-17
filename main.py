from telegram import *
from telegram.ext import *
import logging
from config import *


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# This is called callback. It is derived from the Handler
def start(update, context):
    update.message.reply_text('Hello, World!')


def main():
    updater = Updater(token=API_TOKEN)
    dispatcher = updater.dispatcher
    
    # Initialize Handler for getting into the conversation with the user
    conversation = ConversationHandler(
        entry_points=[],
        states={},
        fallbacks=[]
    )
    
    # Handlers catch the updates and pass them into callbacks (this handler below sends the user's update into start callback)
    # Callbacks also can be named as functions
    dispatcher.add_handler(CommandHandler('start', start))
    
    # Updater constantly checks for 'news' from Telegram server
    # By default updater is set to run every 5 seconds
    updater.start_polling()
    updater.idle()
