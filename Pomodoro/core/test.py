from pomomodel import PomodoroModel
from pomocontroller import PomodoroController

def test():
    p = PomodoroModel("Python Scripts/test-pomodoro-count", 1)
    c = PomodoroController(p)
    c.lifecycle()

test()
