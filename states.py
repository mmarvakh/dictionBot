from aiogram.utils.helper import Helper, HelperMode, ListItem

class States(Helper):
    mode = HelperMode.snake_case

    CURRENT_PLAN_STATE = ListItem()

    CURRENT_DAY_1 = ListItem()
    CURRENT_DAY_2 = ListItem()
    CURRENT_DAY_3 = ListItem()
    CURRENT_DAY_4 = ListItem()
    CURRENT_DAY_5 = ListItem()
    CURRENT_DAY_6 = ListItem()
    CURRENT_DAY_7 = ListItem()