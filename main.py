import logging
from aiogram import Dispatcher, executor

from handlers.custom_config import bot
from handlers.callback_handler import first_layer_handler, second_layer_handler
from handlers import message_handler


logging.basicConfig(level=logging.INFO)

dp = Dispatcher(bot)

if __name__ == "__main__":
    message_handler.setup(dp)
    first_layer_handler.setup(dp)
    second_layer_handler.setup(dp)
    executor.start_polling(dp, skip_updates=True)    

