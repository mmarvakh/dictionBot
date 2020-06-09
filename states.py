from aiogram.utils.helper import Helper, HelperMode, ListItem

class StatesOfPlan(Helper):
    mode = HelperMode.snake_case

    FIRST_PLAN = ListItem()
    SECOND_PLAN = ListItem()
    THIRD_PLAN = ListItem()