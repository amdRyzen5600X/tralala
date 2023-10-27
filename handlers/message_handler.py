from aiogram import Dispatcher, dispatcher
from aiogram import types, dispatcher

from .custom_config import choose_cb, WELLCOME_TEXT


async def start_message(msg: types.Message, state: dispatcher.FSMContext):
    button1 = types.inline_keyboard.InlineKeyboardButton(
            text='как \nпоступить', 
            callback_data=choose_cb.new(choose='how to graduate')
            )
    button2 = types.inline_keyboard.InlineKeyboardButton(
            text='AET', 
            callback_data=choose_cb.new(choose='AET')
            )
    button3 = types.inline_keyboard.InlineKeyboardButton(
            text='abitur', 
            callback_data=choose_cb.new(choose='abitur')
            )
    button4 = types.inline_keyboard.InlineKeyboardButton(
            text='гранты', 
            callback_data=choose_cb.new(choose='grants')
            )
    button5 = types.inline_keyboard.InlineKeyboardButton(
            text='документы', 
            callback_data=choose_cb.new(choose='docs')
            )
    button6 = types.inline_keyboard.InlineKeyboardButton(
            text='образовательные программы', 
            callback_data=choose_cb.new(choose='ep')
            )
    button7 = types.inline_keyboard.InlineKeyboardButton(
            text='скидки', 
            callback_data=choose_cb.new(choose='discount')
            )
    inline_keys = [
            [button1, button2, button3], 
            [button4, button5, button7],
            [button6]
            ]
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await msg.answer(
            WELLCOME_TEXT, 
            reply_markup=reply_markup,
            disable_web_page_preview=True
            )

def setup(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start', 'help'])

