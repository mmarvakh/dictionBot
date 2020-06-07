from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, CallbackQuery

from keyboard import *

from config import *

bot = Bot(token=TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Здравствуйте, " + message.from_user.full_name + "!\n" +
                           "Мы рады помочь Вам с улушением вашей дикции для поднятия уровня вашей речи на новый уровень!\n" +
                           "Для того, чтобы узнать о доступных программах тренировки, воспользуйтесь командой /help")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text(bold("Для просмотра интересующих Вас деталей тренировки, воспользуйтесь командами ниже:"),
               bold("/plans - список планов тренировок"),
               bold("/about - фундаментальные аспекты техники речи(основы)"),
               bold("/plan - выбранный план тренировки"),
               bold("/days - выбранные дни тренировки"),
               sep="\n\n")
    await bot.send_message(message.from_user.id, msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['about'])
async def process_facts_command(message: types.Message):
    msg = text(bold("1. Речевое дыхание"),
               italic("Поставленное речевое дыхание, является фундаментом красивой речи. Это один из самых важных элементов в постановке голоса и речи. От того, как дышит человек, т.е как он умеет пользоваться своим дыханием, зависит красота и сила его голоса, мелодичность речи. Красивое звучание голоса невозможно без правильно поставленного дыхания! Именно с постановки дыхания, мы начинаем работу над речью. Голос перестанет «садиться» и уставать даже после длительного общения, он приобретет силу и полетность.\n"),
               bold("2. Дикция"),
               italic("Это четкость произнесения звуков и слов, определяющих разборчивость речи. Четкая дикция, делает речь красивой, легко восприимчивой и значимой. Человек с хорошей дикцией воспринимается деловым, энергичным и властным. А собеседник с плохой дикцией, производит впечатление, вялого и неуверенного в себе человека. На наших занятиях мы уделяем особое внимание работе над дикцией и проводим множество разноплановых тренировок дикции.\n"),
               bold("3. Артикуляция"),
               italic("Без правильно настроенной работы артикуляционного аппарата, невозможно добиться хорошей дикции. Дикция, находится в прямой зависимости от артикуляции. Хорошая дикция зависит от степени тренированности органов артикуляционного аппарата. Тренировка артикуляционного аппарата, в том числе, артикуляционная гимнастика важный аспект в работе над постановкой речи.\n"),
               bold("4. Тембр голоса"),
               italic("Красота и богатство тембра голоса, во многом, зависит от резонаторов. Работа с резонаторами, расширяет диапазон звучания голоса. Это также, важный аспект, которому мы уделяем не мало внимания, в нашей программе по постановке речи."),
               sep="\n")

    await bot.send_message(message.from_user.id, msg, parse_mode=ParseMode.MARKDOWN)


@dp.callback_query_handler()
async def process_callback_first_plan(callback_query: types.CallbackQuery):
    for plan in buttons_for_plans:
        if callback_query.data == plan:
            msg = text(bold("Был выбран план:\n"),
                    f"{buttons_for_plans[plan]}\n",
                    bold("Первый этап выполнен!\n"),
                    "Давайте приступим ко второму - выбор дней занятий. Вы можете выбрать дни недели, по которым будут высылаться упражнения",
                    sep="\n")
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['plans'])
async def process_plans_command(message: types.Message):
    msg = text(bold("1. Укрепление мышц лица и преодоление неразвитости звучания") + " (Базовый уровень, 7 дней)\n",
               italic("Семидневная программа тренировки для укрепления мышц лица и преодоления неразвитости звучания Вашего голоса. Данная тренировка позволит убрать зажатость мышц лица, для того, чтобы придать вашему лицу пластичность и разбавить речь интересной мимикой.\n"),
               bold("2. Улучшение звучания вашего голоса") + " (Средний уровень, 5 дней)\n",
               italic("Пятидневная программа для тех, кто уже знаком с азами работы дикции и готов перейти на новый уровень звучания голоса. В этой тренировке будет отрабатываться звучание самых труднопроизносимых звуков, что позволит раз и навсегда избавиться от трудностей с произношением.\n"),
               bold("3. Самые сложные звукосочетания") + " (Продвинутый уровень, 4 дня)\n",
               italic("За эти 4 дня Вы научитесь оперировать своей речью на высшем уровне, изучив самые сложные звукосочетания, с которыми возникают проблемы даже у самых продвинутых ведущих.\n\n"),
               bold("Если Вы определились с планом тренировки, то выберите интересующий вариант по кнопкам ниже:"),
               sep="\n")
    await bot.send_message(message.from_user.id, msg, parse_mode=ParseMode.MARKDOWN, reply_markup=inline_buttons_of_plans)


if __name__ == '__main__':
    executor.start_polling(dp)