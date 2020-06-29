from aiogram.utils.markdown import text, bold, italic
from emoji import emojize

start_message = emojize(text(bold("Здравствуйте, {name} :beaming_face_with_smiling_eyes:"),
               "Я буду рад помочь Вам с улучшением Вашей дикции для поднятия уровня речи на " + bold("новый уровень!"),
               bold("Для того, чтобы узнать о доступных программах тренировки, воспользуйтесь кнопкой ниже"), sep="\n\n"), use_aliases=True)

help_message = text(bold("Для просмотра интересующих Вас деталей тренировки, воспользуйтесь командами / кнопками ниже:"),
               bold("/plans - список планов тренировок"),
               bold("/current_plan - выбранный план тренировки"),
               bold("/days - выбранные дни тренировки"),
               bold("/reset - сбросить план тренировки, время, дни"), sep="\n\n")

from_user_invalid_message = "К сожалению, я не в состоянии такое обработать\n\n" + help_message

plans_message = text(bold("1. Укрепление мышц лица и преодоление неразвитости звучания") + " (Базовый уровень, 7 дней)\n",
               italic("Семидневная программа тренировки для укрепления мышц лица и преодоления неразвитости звучания Вашего голоса. Данная тренировка позволит убрать зажатость мышц лица, для того, чтобы придать вашему лицу пластичность и разбавить речь интересной мимикой.\n"),
               bold("2. Улучшение звучания вашего голоса") + " (Средний уровень, 5 дней)\n",
               italic("Пятидневная программа для тех, кто уже знаком с азами работы дикции и готов перейти на новый уровень звучания голоса. В этой тренировке будет отрабатываться звучание самых труднопроизносимых звуков, что позволит раз и навсегда избавиться от трудностей с произношением.\n"),
               bold("3. Самые сложные звукосочетания") + " (Продвинутый уровень, 4 дня)\n",
               italic("За эти 4 дня Вы научитесь оперировать своей речью на высшем уровне, изучив самые сложные звукосочетания, с которыми возникают проблемы даже у самых продвинутых ведущих.\n\n"),
               bold("Если Вы определились с планом тренировки, то выберите интересующий вариант по кнопкам ниже:"), sep="\n")

change_state_plan_message = text(bold("Был выбран план №{number}:\n"),
                    "{plan}\n",
                    bold("Первый этап пройден!\n"),
                    "Давайте приступим ко второму этапу - выбор дней занятий. Вы можете выбрать дни недели, по которым будут высылаться упражнения", sep="\n")

current_plan_message = text(bold("Текущий план тренировок:"),
                            "{current_plan}", sep="\n\n")

stop_choosing_message = text(bold("Дни тренировок были успешно выбраны!"),
                             "В указанные дни Вам будут высылаться задания",
                             bold("Выполняйте их тщательно, чтобы добиться нужного результата"),
                             "Успехов!", sep="\n\n")

MESSAGES = {
    'start' : start_message,
    'help' : help_message,
    'invalid' : from_user_invalid_message,
    'plans' : plans_message,
    'change_state_plan' : change_state_plan_message,
    'current_plan' : current_plan_message,
    'stop' : stop_choosing_message
}