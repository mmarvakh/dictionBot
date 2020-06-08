from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#ReplyKeyboard under main keyboard for quick typing commands /start and /help
button_plan = KeyboardButton("/current_plan")
button_plans = KeyboardButton("/plan")
button_help = KeyboardButton("/help")

reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
reply_keyboard.insert(button_plan).insert(button_plans).insert(button_help)

# Inline buttons for choosing plans
first_plan = InlineKeyboardButton("План №1", callback_data="first_plan")
second_plan = InlineKeyboardButton("План №2", callback_data="second_plan")
third_plan = InlineKeyboardButton("План №3", callback_data="third_plan")

# Create dictionary of plans
plans = {
    "first_plan" : "\"Укрепление мышц лица и преодоление неразвитости звучания(Базовый уровень, 7 дней)\"",
    "second_plan" : "\"Улучшение звучания вашего голоса(Средний уровень, 5 дней)\"",
    "third_plan" : "\"Самые сложные звукосочетания(Продвинутый уровень, 4 дня)\""
}

# Adding inline buttons of plans after message
inline_buttons_of_plans = InlineKeyboardMarkup().insert(first_plan).insert(second_plan).insert(third_plan)