from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from messages import MESSAGES
import keyboard as kb
from config import *
from states import StatesOfPlan

bot = Bot(token=TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
dp = Dispatcher(bot, storage=MemoryStorage())


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
    await message.reply(MESSAGES['plans'], parse_mode=ParseMode.MARKDOWN, reply_markup=kb.reply_buttons_of_plans, reply=False)


@dp.message_handler(state='*', commands=['plan'])
async def process_setstate_command(message: types.Message):
    argument = message.get_args()
    state = dp.current_state(user=message.from_user.id)

    if not argument:
        await state.reset_state()
        return await message.reply("Ошибка, не был передан номер плана тренировки", reply=False)

    if (not argument.isdigit()) or (int(argument) < 1 or int(argument) > 3):
        return await message.reply(MESSAGES['invalid'], parse_mode=ParseMode.MARKDOWN, reply=False)

    await state.set_state(StatesOfPlan.all()[int(argument)-1])
    await message.reply(MESSAGES['change_state_plan'].format(number=argument, plan=str(kb.plans[await state.get_state()])), parse_mode=ParseMode.MARKDOWN, reply=False)


@dp.message_handler(state='*', commands=['current_plan'])
async def process_current_command(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    if not await state.get_state():
        return await message.reply("Вы пока не выбрали ни одного плана тренировки", reply=False)
    await message.reply(MESSAGES['current_plan'].format(current_plan=kb.plans[await state.get_state()]), parse_mode=ParseMode.MARKDOWN, reply=False)


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def other_messages(message: types.Message):
    await bot.send_message(message.from_user.id, MESSAGES['invalid'], parse_mode=ParseMode.MARKDOWN)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)