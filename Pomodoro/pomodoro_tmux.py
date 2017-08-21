#!/usr/bin/python3 # -*- encode: utf-8 -*-
"""Implementation of the core module for tmux"""

from core import *
import os
import re
import sys
import subprocess

def change_tmux_window_title(text):
    """Changes the title of the window to the desired text"""
    # The idea here is to show the time through the window title
    # And other messages when needed.
    command = "tmux rename-window " + text
    subprocess.call(command.split())

def print_func(msg):
    """Prints the time inside the terminal window"""
    # I want the time to be tracked in the window name and
    # The longer messages to be displayed inside the window

    # First we need a regex for the time format:
    time_format = re.compile(r'\d+:\d+')
    # Now we use that regex to match the time string
    if re.match(time_format, msg):
        change_tmux_window_title(msg)
    else:
        # You can format the print function however you want here:
        print(msg)

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

if __name__ == '__main__':
    # Save current window title
    db_path = os.path.join(os.environ.get("HOME"), "test.pomodb")
    try:
        sanitized_args = [int(sys.argv[i]) for i in range(1, len(sys.argv))]
        duration, break_duration, long_break_duration = sanitized_args
    except:
        print("Something went wrong! Using default values...")
        duration, break_duration, long_break_duration = (25, 5, 15)

    model = pomomodel.PomodoroModel(db_path, duration, break_duration,
            long_break_duration)
    view = pomoview.PomodoroView(model, print_func)
    controller = pomocontroller.PomodoroController(input, model, view)

    # Wrapping the process: get current title, execute, back to normal
    get_title_cmd = "tmux display-message -p '#W'"

    # Command returns quoted string, gotta get rid of that with sub()
    initial_title = subprocess.check_output(
        get_title_cmd.split()).decode("utf-8")
    sanitize = re.sub(r"'", '', initial_title)
    # Main pomodoro method
    controller.lifecycle()
    subprocess.call(('tmux rename-window ' + sanitize).split())
