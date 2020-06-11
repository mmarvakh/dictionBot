from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.types.message import ContentType
from aiogram.types import ParseMode, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from messages import MESSAGES
import keyboard as kb
from config import *
from states import StateOfPlan

bot = Bot(token=TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('plan'), state='*')
async def process_callback_plans(callback_query: types.CallbackQuery):
    state = dp.current_state(user=callback_query.from_user.id)

    global chosen_days

    chosen_days = []

    number = int(callback_query.data[-1])

    async def answer_to_choosing(number):
        await bot.answer_callback_query(callback_query.id, text="")
        await state.set_state(StateOfPlan.all()[number - 1])
        await bot.send_message(callback_query.from_user.id, MESSAGES['change_state_plan'].format(number=number, plan=str(kb.plans[await state.get_state()])), parse_mode=ParseMode.MARKDOWN, reply_markup=kb.inline_buttons_of_days)

    await answer_to_choosing(number)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('day'), state='*')
async def process_callback_days(callback_query: types.CallbackQuery):

    day_number = ''

    if callback_query.data[4].isdigit():
        day_number = int(callback_query.data[4])

        if not day_number in chosen_days:
            chosen_days.append(day_number)
        else:
            await bot.answer_callback_query(callback_query.id, text="Этот день уже выбран")
            return

        await bot.answer_callback_query(callback_query.id, text='Добавлено')
        return
    else:
        await bot.answer_callback_query(callback_query.id, text='')
        await bot.send_message(callback_query.from_user.id, "Для занятий были выбраны следующие дни недели: {days}! Ожидайте в указанное время сообщение с упражнениями по Вашему плану. Успехов!".format(days=chosen_days))
        return


@dp.message_handler(state='*', commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(MESSAGES['start'].format(name=message.from_user.full_name), parse_mode=ParseMode.MARKDOWN, reply=False)


@dp.message_handler(state='*', commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(MESSAGES['help'], parse_mode=ParseMode.MARKDOWN, reply=False)


@dp.message_handler(state='*', commands=['about'])
async def process_facts_command(message: types.Message):
    await message.reply(MESSAGES['about'], parse_mode=ParseMode.MARKDOWN, reply=False)


@dp.message_handler(state='*', commands=['plans'])
async def process_plans_command(message: types.Message):
    await message.reply(MESSAGES['plans'], parse_mode=ParseMode.MARKDOWN, reply_markup=kb.reply_buttons_of_plans, reply=False)


@dp.message_handler(state='*', commands=['current_plan'])
async def process_current_command(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    if not await state.get_state():
        await message.reply("Вы пока не выбрали ни одного плана тренировки", reply=False)
        return
    await message.reply(MESSAGES['current_plan'].format(current_plan=kb.plans[await state.get_state()]), parse_mode=ParseMode.MARKDOWN, reply=False)


@dp.message_handler(state='*', commands=['change_plan'])
async def process_change_command(message: types.Message):
    state = dp.current_state(user=message.from_user.id)

    await state.reset_state()

    await message.reply(MESSAGES['plans'], parse_mode=ParseMode.MARKDOWN, reply_markup=kb.reply_buttons_of_plans, reply=False)


@dp.message_handler(state='*', content_types=types.ContentTypes.ANY)
async def other_messages(message: types.Message):
    await bot.send_message(message.from_user.id, MESSAGES['invalid'], parse_mode=ParseMode.MARKDOWN)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)