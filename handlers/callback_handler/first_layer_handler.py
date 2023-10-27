from aiogram import Dispatcher, dispatcher
from aiogram import types, dispatcher

from ..custom_config import choose_cb, bot
from ..custom_config import HOW_TO_GRADUATE, AET, ABITUR, GRANTS, DOCS, DISCOUNT, EP


back_button = types.inline_keyboard.InlineKeyboardButton(
        text='назад',
        callback_data=choose_cb.new(choose='back 1st'),
        )
async def how_to_graduate_info(query: types.CallbackQuery, callback_data: dict):
    button1 = types.inline_keyboard.InlineKeyboardButton(
            text='колледж', 
            callback_data=choose_cb.new(choose='colledge')
            )
    button2 = types.inline_keyboard.InlineKeyboardButton(
            text='бакалавриат', 
            callback_data=choose_cb.new(choose='bachelor')
            )
    button3 = types.inline_keyboard.InlineKeyboardButton(
            text='магистратура', 
            callback_data=choose_cb.new(choose='master')
            )
    button4 = types.inline_keyboard.InlineKeyboardButton(
            text='докторантура', 
            callback_data=choose_cb.new(choose='PHd')
            )
    inline_keys = [[button1, button2, button3],[button4],[back_button]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            HOW_TO_GRADUATE,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

async def AET_info(query: types.CallbackQuery, callback_data: dict):
    inline_keys = [[back_button]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            AET,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

async def abitur_info(query: types.CallbackQuery, callback_data: dict):
    button1 = types.inline_keyboard.InlineKeyboardButton(
            text='бакалавриат', 
            callback_data=choose_cb.new(choose='bachelor abitur')
            )
    button2 = types.inline_keyboard.InlineKeyboardButton(
            text='магистратура', 
            callback_data=choose_cb.new(choose='master abitur')
            )
    inline_keys = [[button1, button2],[back_button]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            ABITUR,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

async def grants_info(query: types.CallbackQuery, callback_data: dict):
    button1 = types.inline_keyboard.InlineKeyboardButton(
            text='бакалавриат', 
            callback_data=choose_cb.new(choose='bachelor grants')
            )
    button2 = types.inline_keyboard.InlineKeyboardButton(
            text='магистратура', 
            callback_data=choose_cb.new(choose='master grants')
            )
    inline_keys = [[button1, button2],[back_button]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            GRANTS,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

async def docs_info(query: types.CallbackQuery, callback_data: dict):
    inline_keys = [[back_button]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            DOCS,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

async def discount_info(query: types.CallbackQuery, callback_data: dict):
    button1 = types.inline_keyboard.InlineKeyboardButton(
            text='бакалавриат', 
            callback_data=choose_cb.new(choose='bachelor discount')
            )
    button2 = types.inline_keyboard.InlineKeyboardButton(
            text='магистратура', 
            callback_data=choose_cb.new(choose='master discount')
            )
    inline_keys = [[button1, button2],[back_button]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            DISCOUNT,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

async def ep_info(query: types.CallbackQuery, callback_data: dict):
    button1 = types.inline_keyboard.InlineKeyboardButton(
            text='бакалавриат', 
            callback_data=choose_cb.new(choose='bachelor ep')
            )
    button2 = types.inline_keyboard.InlineKeyboardButton(
            text='магистратура', 
            callback_data=choose_cb.new(choose='master ep')
            )
    inline_keys = [[button1, button2],[back_button]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            EP,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

def setup(dp: Dispatcher):
    dp.register_callback_query_handler(
            how_to_graduate_info, 
            choose_cb.filter(choose='how to graduate')
            )
    dp.register_callback_query_handler(
            AET_info, 
            choose_cb.filter(choose='AET')
            )
    dp.register_callback_query_handler(
            abitur_info, 
            choose_cb.filter(choose='abitur')
            )
    dp.register_callback_query_handler(
            grants_info, 
            choose_cb.filter(choose='grants')
            )
    dp.register_callback_query_handler(
            docs_info, 
            choose_cb.filter(choose='docs')
            )
    dp.register_callback_query_handler(
            discount_info, 
            choose_cb.filter(choose='discount')
            )
    dp.register_callback_query_handler(
            ep_info, 
            choose_cb.filter(choose='ep')
            )

