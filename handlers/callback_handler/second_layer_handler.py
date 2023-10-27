from aiogram import Dispatcher, dispatcher
from aiogram import types, dispatcher

from ..custom_config import choose_cb, bot
from ..custom_config import BACHELOR_ABITUR, BACHELOR_DISCOUNT, BACHELOR_EP, BACHELOR_GRANTS, MAGA_ABITUR, MAGA_DISCOUNT, MAGA_EP, MAGA_GRANTS, MASTER, PHD, WELLCOME_TEXT, COLLEDGE, BACHELOR

async def to_main(query: types.CallbackQuery, callback_data: dict):
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
    await bot.edit_message_text(
            WELLCOME_TEXT,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup,
            disable_web_page_preview=True
            )

back_button = types.inline_keyboard.InlineKeyboardButton(
        text='назад',
        callback_data=choose_cb.new(choose='how to graduate'),
        )

async def colledge_info(query: types.CallbackQuery, callback_data: dict):
    inline_keys = [[back_button]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            COLLEDGE,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

async def bachlor_info(query: types.CallbackQuery, callback_data: dict):
    button1 = types.inline_keyboard.InlineKeyboardButton(
            text='образовательные программы', 
            callback_data=choose_cb.new(choose='ep')
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
    inline_keys = [
            [button1, button2, button3], 
            [button4, button5],
            [back_button]
            ]
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            BACHELOR,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

async def master_info(query: types.CallbackQuery, callback_data: dict):
    inline_keys = [[back_button]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            MASTER,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

async def PHD_info(query: types.CallbackQuery, callback_data: dict):
    inline_keys = [[back_button]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            PHD,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

back_button1 = types.inline_keyboard.InlineKeyboardButton(
        text='назад',
        callback_data=choose_cb.new(choose='abitur'),
        )

async def bachelor_abitur_info(query: types.CallbackQuery, callback_data: dict):
    inline_keys = [[back_button1]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            BACHELOR_ABITUR,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

async def maga_abitur_info(query: types.CallbackQuery, callback_data: dict):
    inline_keys = [[back_button1]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            MAGA_ABITUR,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

back_button2 = types.inline_keyboard.InlineKeyboardButton(
        text='назад',
        callback_data=choose_cb.new(choose='grants'),
        )

async def bachelor_grants_info(query: types.CallbackQuery, callback_data: dict):
    inline_keys = [[back_button2]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            BACHELOR_GRANTS,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

async def maga_grants_info(query: types.CallbackQuery, callback_data: dict):
    inline_keys = [[back_button2]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            MAGA_GRANTS,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

back_button3 = types.inline_keyboard.InlineKeyboardButton(
        text='назад',
        callback_data=choose_cb.new(choose='discount'),
        )

async def bachelor_discount_info(query: types.CallbackQuery, callback_data: dict):
    inline_keys = [[back_button3]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            BACHELOR_DISCOUNT,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

async def maga_discount_info(query: types.CallbackQuery, callback_data: dict):
    inline_keys = [[back_button3]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            MAGA_DISCOUNT,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

back_button4 = types.inline_keyboard.InlineKeyboardButton(
        text='назад',
        callback_data=choose_cb.new(choose='ep'),
        )

async def bachelor_ep_info(query: types.CallbackQuery, callback_data: dict):
    inline_keys = [[back_button4]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            BACHELOR_EP,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

async def maga_ep_info(query: types.CallbackQuery, callback_data: dict):
    inline_keys = [[back_button4]] 
    reply_markup = types.inline_keyboard.InlineKeyboardMarkup(
            inline_keyboard=inline_keys
            )
    await bot.edit_message_text(
            MAGA_EP,
            query.from_user.id,
            query.message.message_id,
            reply_markup=reply_markup
            )

def setup(dp: Dispatcher):
    dp.register_callback_query_handler(
            to_main, 
            choose_cb.filter(choose='back 1st')
            )
    dp.register_callback_query_handler(
            colledge_info, 
            choose_cb.filter(choose='colledge')
            )
    dp.register_callback_query_handler(
            bachlor_info, 
            choose_cb.filter(choose='bachelor')
            )
    dp.register_callback_query_handler(
            master_info, 
            choose_cb.filter(choose='master')
            )
    dp.register_callback_query_handler(
            PHD_info, 
            choose_cb.filter(choose='PHd')
            )
    dp.register_callback_query_handler(
            bachelor_abitur_info, 
            choose_cb.filter(choose='bachelor abitur')
            )
    dp.register_callback_query_handler(
            maga_abitur_info, 
            choose_cb.filter(choose='master abitur')
            )
    dp.register_callback_query_handler(
            bachelor_grants_info, 
            choose_cb.filter(choose='bachelor grants')
            )
    dp.register_callback_query_handler(
            maga_grants_info, 
            choose_cb.filter(choose='master grants')
            )
    dp.register_callback_query_handler(
            bachelor_discount_info, 
            choose_cb.filter(choose='bachelor discount')
            )
    dp.register_callback_query_handler(
            maga_discount_info, 
            choose_cb.filter(choose='master discount')
            )
    dp.register_callback_query_handler(
            bachelor_ep_info, 
            choose_cb.filter(choose='bachelor ep')
            )
    dp.register_callback_query_handler(
            maga_ep_info, 
            choose_cb.filter(choose='master ep')
            )

