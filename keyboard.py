from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Inline buttons for choosing plans
button_of_first_plan = InlineKeyboardButton("План №1", callback_data="first_plan")
button_of_second_plan = InlineKeyboardButton("План №2", callback_data="second_plan")
button_of_third_plan = InlineKeyboardButton('План №3', callback_data="third_plan")

# Adding inline buttons of plans after message
inline_buttons_of_plans = InlineKeyboardMarkup().insert(button_of_first_plan).insert(button_of_second_plan).insert(button_of_third_plan)