#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""Implementation of the core module for tmux"""

import core
import subprocess

if __name__ == '__main__':
        model = core.pomomodel.PomodoroModel("Python Scripts/test-pomodoro-count",
            1)
    controller = core.pomocontroller.PomodoroController(model)
    controller.lifecycle()
    #subprocess.call("curl -L git.io/unix".split())
