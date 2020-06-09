from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#ReplyKeyboard under main keyboard for quick typing commands /start and /help
button_plan = KeyboardButton("/current_plan")
button_plans = KeyboardButton("/plan")
button_help = KeyboardButton("/help")

reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
reply_keyboard.insert(button_plan).insert(button_plans).insert(button_help)

# Inline buttons for choosing plans
first_plan = KeyboardButton("/plan 1")
second_plan = KeyboardButton("/plan 2")
third_plan = KeyboardButton("/plan 3")

# Create dictionary of plans
plans = {
    "first_plan" : "\"Укрепление мышц лица и преодоление неразвитости звучания(Базовый уровень, 7 дней)\"",
    "second_plan" : "\"Улучшение звучания вашего голоса(Средний уровень, 5 дней)\"",
    "third_plan" : "\"Самые сложные звукосочетания(Продвинутый уровень, 4 дня)\""
}

# Adding inline buttons of plans after message
reply_buttons_of_plans = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).insert(first_plan).insert(second_plan).insert(third_plan)

# Buttons for choosing day of the week
monday = InlineKeyboardButton("Понедельник", callback_data="monday")
tuesday = InlineKeyboardButton("Вторник", callback_data="tuesday")
wednesday = InlineKeyboardButton("Среда", callback_data="wednesday")
thursday = InlineKeyboardButton("Четверг", callback_data="thursday")
friday = InlineKeyboardButton("Пятница", callback_data="friday")
saturday = InlineKeyboardButton("Суббота", callback_data="saturday")
sunday = InlineKeyboardButton("Воскресенье", callback_data="sunday")
stop_choosing = InlineKeyboardButton("Закончить выбор", callback_data="stop")


# Adding inline buttons of days of the week after choosing
inline_buttons_of_days = InlineKeyboardMarkup().insert(monday).insert(tuesday).insert(wednesday).insert(thursday).insert(friday).insert(saturday).insert(sunday).row(stop_choosing)