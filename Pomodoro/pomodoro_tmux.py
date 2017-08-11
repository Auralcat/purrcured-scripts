#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""Implementation of the core module for tmux"""

from core import pomoview, pomocontroller, pomomodel
#import subprocess

if __name__ == '__main__':
    model = pomomodel.PomodoroModel(1)
    controller = pomocontroller.PomodoroController(model)
    controller.lifecycle()
    #subprocess.call("curl -L git.io/unix".split())
