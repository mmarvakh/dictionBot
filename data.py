# -*- coding: utf-8 -*-

from vedis import Vedis
from config import DATA_BASE
from states import StateOfPlan

def get_current_state(user_id):
    with Vedis(DATA_BASE) as db:
        try:
            return db[user_id].decode()
        except KeyError:
            return StateOfPlan.START.value

def set_state(user_id, value):
    with Vedis(DATA_BASE) as db:
        try:
            db[user_id] = value
            return True
        except:
            return False