#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""Implementation of the core module for tmux"""

from core import *
import os
import sys

def print_func(msg):
    """Function to be passed to the view object"""
    sys.stdout.write(msg + '\r')
    sys.stdout.flush()

if __name__ == '__main__':
    db_path = os.path.join(os.environ.get("HOME"), "test.pomodb")
    model = pomomodel.PomodoroModel(db_path)
    view = pomoview.PomodoroView(model, print_func)
    controller = pomocontroller.PomodoroController(model, view)
    controller.lifecycle()
