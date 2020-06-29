from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Inline buttons for choosing plans
first_plan = InlineKeyboardButton("План №1", callback_data="plan_1")
second_plan = InlineKeyboardButton("План №2", callback_data="plan_2")
third_plan = InlineKeyboardButton("План №3", callback_data="plan_3")

# Create dictionary of plans
plans = {
    "1" : "\"Укрепление мышц лица и преодоление неразвитости звучания (Базовый уровень, 7 дней)\"",
    "2" : "\"Улучшение звучания вашего голоса (Средний уровень, 5 дней)\"",
    "3" : "\"Самые сложные звукосочетания (Продвинутый уровень, 4 дня)\""
}

# Adding inline buttons of plans after message
reply_buttons_of_plans = InlineKeyboardMarkup(resize_keyboard=True).insert(first_plan).insert(second_plan).insert(third_plan)

# Buttons for choosing day of the week
monday = InlineKeyboardButton("Пн", callback_data="day_0")
tuesday = InlineKeyboardButton("Вт", callback_data="day_1")
wednesday = InlineKeyboardButton("Ср", callback_data="day_2")
thursday = InlineKeyboardButton("Чт", callback_data="day_3")
friday = InlineKeyboardButton("Пт", callback_data="day_4")
saturday = InlineKeyboardButton("Сб", callback_data="day_5")
sunday = InlineKeyboardButton("Вс", callback_data="day_6")
stop_choosing = InlineKeyboardButton("Закончить выбор", callback_data="day_stop")


# Adding inline buttons of days of the week after choosing
inline_buttons_of_days = InlineKeyboardMarkup(row_width=7).insert(monday).insert(tuesday).insert(wednesday).insert(thursday).insert(friday).insert(saturday).insert(sunday).row(stop_choosing)

# Buttons for choosing time
six_clock = InlineKeyboardButton("6:00", callback_data="time_6:00")
seven_clock = InlineKeyboardButton("7:00", callback_data="time_7:00")
eight_clock = InlineKeyboardButton("8:00", callback_data="time_8:00")
nine_clock = InlineKeyboardButton("9:00", callback_data="time_9:00")
ten_clock = InlineKeyboardButton("10:00", callback_data="time_10:00")
eleven_clock = InlineKeyboardButton("11:00", callback_data="time_11:00")
twelve_clock = InlineKeyboardButton("12:00", callback_data="time_12:00")
thirteen_clock = InlineKeyboardButton("13:00", callback_data="time_13:00")
fourteen_clock = InlineKeyboardButton("14:00", callback_data="time_14:00")
fifteen_clock = InlineKeyboardButton("15:00", callback_data="time_15:00")
sixteen_clock = InlineKeyboardButton("16:00", callback_data="time_16:00")
seventeen_clock = InlineKeyboardButton("17:00", callback_data="time_17:00")
eighteen_clock = InlineKeyboardButton("18:00", callback_data="time_18:00")
nineteen_clock = InlineKeyboardButton("19:00", callback_data="time_19:00")
twenty_clock = InlineKeyboardButton("20:00", callback_data="time_20:00")
twentyOne_clock = InlineKeyboardButton("21:00", callback_data="time_21:00")

# Adding inline buttons of time
inline_buttons_of_time = InlineKeyboardMarkup(row_width=4).insert(six_clock).insert(seven_clock).insert(eight_clock).insert(nine_clock).insert(ten_clock).insert(eleven_clock).insert(twelve_clock).\
                                                insert(thirteen_clock).insert(fourteen_clock).insert(fifteen_clock).insert(sixteen_clock).insert(seventeen_clock).insert(eighteen_clock).insert(nineteen_clock)\
                                                .insert(twenty_clock).insert(twentyOne_clock)

help_btn = InlineKeyboardButton("Начать работу", callback_data='help')

inline_start_btn = InlineKeyboardMarkup(resize_keyboard=True).row(help_btn)

plans_btn = InlineKeyboardButton("Доступные планы", callback_data='plans')
current_plan_btn = InlineKeyboardButton("Выбранный план", callback_data='current_plan')
days_btn = InlineKeyboardButton("Выбранные дни", callback_data='days')
change_btn = InlineKeyboardButton("Сменить план", callback_data='change_plan')

inline_info = InlineKeyboardMarkup(row_width=2).insert(plans_btn).insert(current_plan_btn).insert(days_btn).insert(change_btn)