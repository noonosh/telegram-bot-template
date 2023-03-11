import os
import dotenv
import logging
from telegram.ext import Application, CommandHandler, ConversationHandler
from src.components import start


dotenv.load_dotenv()

# Set Debug to False when in production!
DEBUG = os.environ.get('DEBUG', True)


logging.basicConfig(
    filename='logs.log' if not DEBUG else None,
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG if DEBUG else logging.INFO
)

logger = logging.getLogger(__name__)


def main():
    application = Application.builder().token(os.environ.get('BOT_TOKEN')).build()

    main_conversation = ConversationHandler(
        entry_points=[
            CommandHandler('start', start.start)
        ],
        states={},
        fallbacks=[]
    )

    application.add_handler(main_conversation)

    application.run_polling()
