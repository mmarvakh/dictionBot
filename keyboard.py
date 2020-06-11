from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#ReplyKeyboard under main keyboard for quick typing commands /start and /help
button_plan = KeyboardButton("/current_plan")
button_plans = KeyboardButton("/plan")
button_help = KeyboardButton("/help")

reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
reply_keyboard.insert(button_plan).insert(button_plans).insert(button_help)

# Inline buttons for choosing plans
first_plan = InlineKeyboardButton("План №1", callback_data="plan_1")
second_plan = InlineKeyboardButton("План №2", callback_data="plan_2")
third_plan = InlineKeyboardButton("План №3", callback_data="plan_3")

# Create dictionary of plans
plans = {
    "first_plan" : "\"Укрепление мышц лица и преодоление неразвитости звучания (Базовый уровень, 7 дней)\"",
    "second_plan" : "\"Улучшение звучания вашего голоса (Средний уровень, 5 дней)\"",
    "third_plan" : "\"Самые сложные звукосочетания (Продвинутый уровень, 4 дня)\""
}

# Adding inline buttons of plans after message
reply_buttons_of_plans = InlineKeyboardMarkup(resize_keyboard=True).insert(first_plan).insert(second_plan).insert(third_plan)

# Buttons for choosing day of the week
monday = InlineKeyboardButton("[Пн]", callback_data="day_0")
tuesday = InlineKeyboardButton("[Вт]", callback_data="day_1")
wednesday = InlineKeyboardButton("[Ср]", callback_data="day_2")
thursday = InlineKeyboardButton("[Чт]", callback_data="day_3")
friday = InlineKeyboardButton("[Пт]", callback_data="day_4")
saturday = InlineKeyboardButton("[Сб]", callback_data="day_5")
sunday = InlineKeyboardButton("[Вс]", callback_data="day_6")
stop_choosing = InlineKeyboardButton("Закончить выбор", callback_data="day_stop")


# Adding inline buttons of days of the week after choosing
inline_buttons_of_days = InlineKeyboardMarkup(row_width=7).insert(monday).insert(tuesday).insert(wednesday).insert(thursday).insert(friday).insert(saturday).insert(sunday).row(stop_choosing)