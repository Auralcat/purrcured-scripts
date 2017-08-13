from pomomodel import PomodoroModel
from pomocontroller import PomodoroController
from pomoview import PomodoroView
import sys

def print_func(msg):
    """Test print function"""
    sys.stdout.write(msg + '\r')
    sys.stdout.flush()

def test():
    p = PomodoroModel("Python Scripts/test-pomodoro-count", 1)
    v = PomodoroView(p, print_func)
    c = PomodoroController(p, v)
    c.lifecycle()

test()
