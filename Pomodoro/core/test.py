from pomomodel import PomodoroModel
from pomocontroller import PomodoroController
from pomoview import PomodoroView
import sys

def print_func(msg):
    """Test print function"""

    # This is a VT100 terminal code.
    erase_line = '\x1b[2K'
    sys.stdout.write(erase_line + msg + '\r')
    sys.stdout.flush()

def test():
    p = PomodoroModel("test-pomodoro-count", 1)
    v = PomodoroView(p, print_func)
    c = PomodoroController(p, v)
    c.lifecycle()

test()
