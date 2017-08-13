#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""Implementation of the core module for tmux"""

from core import *
import os
from re import sub
import sys
import subprocess

def print_func(msg):
    """Prints the time inside the terminal window"""
    sys.stdout.write(msg + '\r')
    sys.stdout.flush()

def change_tmux_window_title(text):
    """Changes the title of the window to the desired text"""
    # The idea here is to show the time through the window title
    # And other messages when needed.
    command = "tmux rename-window " + text
    subprocess.call(command.split())

if __name__ == '__main__':
    # Save current window title
    db_path = os.path.join(os.environ.get("HOME"), "test.pomodb")
    model = pomomodel.PomodoroModel(db_path)
    view = pomoview.PomodoroView(model, change_tmux_window_title)
    controller = pomocontroller.PomodoroController(model, view)

    # Wrapping the process: get current title, execute, back to normal
    get_title_cmd = "tmux display-message -p '#W'"

    # Command returns quoted string, gotta get rid of that with sub()
    initial_title = subprocess.check_output(
        get_title_cmd.split()).decode("utf-8")
    sanitize = sub(r"'", '', initial_title)
    # Main pomodoro method
    controller.lifecycle()
    subprocess.call(('tmux rename-window ' + sanitize).split())
