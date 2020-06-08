from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from messages import MESSAGES

from keyboard import *

from config import *

bot = Bot(token=TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.callback_query_handler(lambda call: call.data == "stop")
async def process_callback_stop(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, MESSAGES['stop'], parse_mode=ParseMode.MARKDOWN)


@dp.callback_query_handler(lambda call: True)
async def process_callback_plans(callback_query: types.CallbackQuery):
    for index, plan in enumerate(plans, 1):
        if callback_query.data == plan:
            current_state = dp.current_state(user=callback_query.from_user.id)
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, MESSAGES['change_state_plan'].format(number=index, plan=plans[plan]), parse_mode=ParseMode.MARKDOWN, reply_markup=inline_buttons_of_days)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(MESSAGES['start'].format(name=message.from_user.full_name), parse_mode=ParseMode.MARKDOWN, reply=False)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(MESSAGES['help'], parse_mode=ParseMode.MARKDOWN, reply=False)


@dp.message_handler(commands=['about'])
async def process_facts_command(message: types.Message):
    await message.reply(MESSAGES['about'], parse_mode=ParseMode.MARKDOWN, reply=False)


@dp.message_handler(commands=['plans'])
async def process_plans_command(message: types.Message):
    await message.reply(MESSAGES['plans'], parse_mode=ParseMode.MARKDOWN, reply_markup=inline_buttons_of_plans, reply=False)





@dp.message_handler()
async def process_invalid_command(message: types.Message):
    await message.reply(MESSAGES['invalid'], parse_mode=ParseMode.MARKDOWN,reply=False)


if __name__ == '__main__':
    executor.start_polling(dp)