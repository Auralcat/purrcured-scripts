"""Pomodoro core library

The idea for this module is to be able to implement the Pomodoro Technique in
any medium desired (that supports Python scripting).

Basic usage:

    from core import pomoview, pomocontroller, pomomodel

    model = pomomodel.PomodoroModel(db_path, duration,
                                    break_duration, long_break_duration)
    controller = pomocontroller.PomodoroController(model)
    controller.lifecycle()

TODO:

    - Make a place for a generic print function to be added"""


__title__ = 'pomodoro'
__version__ = '0.5'
__author__ = 'Auralcat'
__license__ = 'Public Domain'

from . import pomomodel
from . import pomoview
from . import pomocontroller
