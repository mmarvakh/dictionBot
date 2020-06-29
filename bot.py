from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.types.message import ContentType
from aiogram.types import ParseMode, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from models import *

import sqlalchemy

import redis

from messages import MESSAGES
import keyboard as kb
from config import *
from states import StateOfUser

bot = Bot(token=TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
dp = Dispatcher(bot, storage=MemoryStorage())

r = redis.Redis(db=0)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=ENGINE)
session = Session()

global chosen_days, indexes_of_chosen, time_sending, days

chosen_days = []

indexes_of_chosen = []

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]


@dp.callback_query_handler(lambda c: c.data and c.data == 'help', state='*')
async def process_help_command(callback_query: types.CallbackQuery):

    await bot.answer_callback_query(callback_query.id, text='')

    await bot.send_message(callback_query.from_user.id, MESSAGES['help'], parse_mode=ParseMode.MARKDOWN, reply_markup=kb.inline_info)


@dp.callback_query_handler(lambda c: c.data and c.data == 'plans', state='*')
async def process_plans_command(callback_query: types.CallbackQuery):

    await bot.answer_callback_query(callback_query.id, text='')

    await bot.send_message(callback_query.from_user.id, MESSAGES['plans'], parse_mode=ParseMode.MARKDOWN, reply_markup=kb.reply_buttons_of_plans)


@dp.callback_query_handler(lambda c: c.data and c.data == 'current_plan', state='*')
async def process_current_command(callback_query: types.CallbackQuery):

    state = dp.current_state(user=callback_query.from_user.id)

    await bot.answer_callback_query(callback_query.id, text='')

    if await state.get_state() != StateOfUser.USER:

        await bot.send_message(callback_query.from_user.id, "Вы пока не выбрали ни одного плана тренировки")
        return

    await bot.send_message(callback_query.from_user.id, MESSAGES['current_plan'].format(current_plan=kb.plans[await state.get_state()]), parse_mode=ParseMode.MARKDOWN)


@dp.callback_query_handler(lambda c: c.data and c.data == 'change_plan', state='*')
async def process_change_command(callback_query: types.CallbackQuery):

    state = dp.current_state(user=callback_query.from_user.id)

    await state.reset_state()

    await bot.answer_callback_query(callback_query.id, text='')

    await bot.send_message(callback_query.from_user.id, MESSAGES['plans'], parse_mode=ParseMode.MARKDOWN, reply_markup=kb.reply_buttons_of_plans)


@dp.callback_query_handler(lambda c: c.data and c.data == 'days', state='*')
async def process_days_command(callback_query: types.CallbackQuery):

    await bot.answer_callback_query(callback_query.id, text='')

    if len(chosen_days) > 0:

        await bot.send_message(callback_query.from_user.id, "Выбранные дни тренировок:\n\n"
                            "{days}".format(days=sorted(chosen_days)))

    else:
        await bot.send_message(callback_query.from_user.id, "Вы пока не выбрали план / дни тренировок.\n\n"
                            "Чтобы приступить к выбору, воспользуйтесь командой /plans")


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('plan'), state='*')
async def process_callback_plans(callback_query: types.CallbackQuery):

    global current_plan_number

    time_sending = ''

    chosen_days.clear()

    indexes_of_chosen.clear()

    new_keyboard = kb.inline_buttons_of_days

    number = int(callback_query.data[-1])

    current_plan_number = number

    async def answer_to_choosing(number):
        await bot.answer_callback_query(callback_query.id, text="")
        await bot.send_message(callback_query.from_user.id, MESSAGES['change_state_plan'].format(number=number, plan=str(kb.plans[str(number)])), parse_mode=ParseMode.MARKDOWN, reply_markup=kb.inline_buttons_of_days)

    await answer_to_choosing(number)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('day'), state='*')
async def process_callback_days(callback_query: types.CallbackQuery):

    global message_id, days_str

    days_str = ''

    new_keyboard = kb.inline_buttons_of_days

    message_id = callback_query.message.message_id

    if callback_query.data[4].isdigit():

        day_number = int(callback_query.data[4])

        if not day_number in indexes_of_chosen:

            chosen_days.append(days[day_number])

            indexes_of_chosen.append(day_number)

        else:

            await bot.answer_callback_query(callback_query.id, text='День убран из расписания')

            chosen_days.remove(days[day_number])

            indexes_of_chosen.remove(day_number)

            for day in new_keyboard:

                for text in day[1][0]:

                    if text['callback_data'] == callback_query.data:

                        new_keyboard['inline_keyboard'][0][int(callback_query.data[4])]['text'] = new_keyboard['inline_keyboard'][0][int(callback_query.data[4])]['text'][:-1]

            await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=message_id, reply_markup=new_keyboard)

            return

        await bot.answer_callback_query(callback_query.id, text='День выбран')

        for day in new_keyboard:

            for text in day[1][0]:

                if text['callback_data'] == callback_query.data:

                    new_keyboard['inline_keyboard'][0][int(callback_query.data[4])]['text'] += '✅'

        await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id, message_id=message_id, reply_markup=new_keyboard)

    else:

        await bot.answer_callback_query(callback_query.id, text='')

        if len(chosen_days) != 0:

            for day in chosen_days:

                days_str += day + ', '

            await bot.send_message(callback_query.from_user.id, "Для занятий были выбраны следующие дни недели:\n{days}\n\n"
                                                                "Выберите удобное для Вас время занятий (В это время я буду высылать Вам упражнения, пройти их Вы можете в любое удобное время))".format(days=days_str[:-2]), reply_markup=kb.inline_buttons_of_time)

        else:

            await bot.send_message(callback_query.from_user.id, "Вы не выбрали ни одного дня. Пожалуйста, выберите дни занятий по кнопкам выше")


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('time'), state='*')
async def process_callback_time(callback_query: types.CallbackQuery):

    try:
        user = Users(id=callback_query.from_user.id, user_login=callback_query.from_user.username,
                     chosen_time=callback_query.data[5:], chosen_days=days_str[:-2],
                     chosen_plan=current_plan_number)

        r.set(callback_query.from_user.id, "USER")

        session.add(user)
        session.commit()

    except:
        print("Ошибка")

    time_sending = callback_query.data[5:].split(":")[0]

    await bot.answer_callback_query(callback_query.id, text="Время установлено")

    await bot.send_message(callback_query.from_user.id, "Выбранное время занятий: {time}\n\n"
                                                        "В указанные дни и время я буду высылать Вам упражнения для развития Вашей дикции. Успехов!".format(time=callback_query.data[5:]))

    await dp.current_state(user=callback_query.from_user.id).set_state(StateOfUser.USER)

    #r.set(str(callback_query.from_user.id), str(dp.current_state(user=callback_query.from_user.id).get_state()))

    #exercises = session.query(Exercises).filter_by(plan_number=current_plan_number).first()

    #await bot.send_message(callback_query.from_user.id, exercises.exercise_text)


@dp.message_handler(state='*', commands=['start'])
async def process_start_command(message: types.Message):

    global u

    state = dp.current_state(user=message.from_user.id)

    await state.set_state(StateOfUser.NEW_USER)

    if r.get(message.from_user.id) == b"USER":

        print(0)

    else:
        print(r.get(message.from_user.id))


    await message.reply(MESSAGES['start'].format(name=message.from_user.full_name), parse_mode=ParseMode.MARKDOWN, reply=False, reply_markup=kb.inline_start_btn)


@dp.message_handler(state='*', commands=['plans'])
async def process_plans_command(message: types.Message):

    await message.reply(MESSAGES['plans'], parse_mode=ParseMode.MARKDOWN, reply_markup=kb.reply_buttons_of_plans, reply=False)


@dp.message_handler(state='*', commands=['current_plan'])
async def process_current_command(message: types.Message):

    state = dp.current_state(user=message.from_user.id)

    if r.get(message.from_user.id) != b"USER":

        await message.reply("Вы пока не выбрали ни одного плана тренировки", reply=False)
        return

    await message.reply(MESSAGES['current_plan'].format(current_plan=kb.plans[str(current_plan_number)]), parse_mode=ParseMode.MARKDOWN, reply=False)


@dp.message_handler(state='*', commands=['reset'])
async def process_change_command(message: types.Message):

    state = dp.current_state(user=message.from_user.id)

    await state.reset_state()

    await state.set_state(StateOfUser.NEW_USER)

    try:
        user = session.query(Users).filter_by(id=message.from_user.id).delete()

        session.commit()

    except:
        print("Ошибка2")

    await message.reply(MESSAGES['plans'], parse_mode=ParseMode.MARKDOWN, reply_markup=kb.reply_buttons_of_plans, reply=False)


@dp.message_handler(state='*', commands=['days'])
async def process_days_command(message: types.Message):

    if len(chosen_days) > 0:

        await message.reply("Выбранные дни тренировок:\n\n"
                            "{days}".format(days=sorted(chosen_days), reply=False))

    else:
        await message.reply("Вы пока не выбрали план / дни тренировок.\n\n"
                            "Чтобы приступить к выбору, воспользуйтесь командой /plans", reply=False)


@dp.message_handler(state='*', content_types=types.ContentTypes.ANY)
async def other_messages(message: types.Message):

    await bot.send_message(message.from_user.id, MESSAGES['invalid'], parse_mode=ParseMode.MARKDOWN, reply_markup=kb.inline_info)


async def shutdown(dispatcher: Dispatcher):

    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)