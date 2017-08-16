#!/usr/bin/python3
# -*- encode: utf-8 -*-

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

# You can define the input function from outside the core module.
# In this case, we'll get the variables we need from sys.argv.
def pass_vars(args):
    """Sample input function"""
    # You NEED to cast all the input vars to ints!
    size = len(args)
    duration, break_dur, long_break_dur = [int(args[i]) for i in range(1, size)]
    print("Duration: %s\n Break duration: %s\nLong Break Duration: %s" %
            (duration, break_dur, long_break_dur))
    return duration, break_dur, long_break_dur

def change_tmux_window_title(text):
    """Changes the title of the window to the desired text"""
    # The idea here is to show the time through the window title
    # And other messages when needed.
    command = "tmux rename-window " + text
    subprocess.call(command.split())

if __name__ == '__main__':
    # Save current window title
    db_path = os.path.join(os.environ.get("HOME"), "test.pomodb")
    duration, break_duration, long_break_duration = pass_vars(sys.argv)
    model = pomomodel.PomodoroModel(db_path, duration, break_duration,
            long_break_duration)
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
