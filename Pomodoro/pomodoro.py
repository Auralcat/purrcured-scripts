# TODO: Integrate the time module
#       Make it so you can append the pomodoro data to a view

import time
import sys

class PomodoroModel():
    """The Pomodoro object holds the data about the completed pomodoros and the
       methods to interact with it."""

    total_pomodoros = 0

    def __init__(self, duration=25):
        """Sets the duration of a pomodoro session and initializes
           the variables"""
        self.duration = duration
        self.mins = 0
        self.secs = 0

    def get_time(self):
        """Returns a string with the elapsed pomodoro time."""
        display_time = "{}:{}".format(str(self.mins).zfill(2),
                                      str(self.secs).zfill(2))

        return display_time

class PomodoroController():
    """Controls the model."""

    def __init__(self, model):
        self.model = model

    def start(self, msg="Beginning pomodoro... focus!"):
        """Begins counting the time."""
        print(msg)
        view = PomodoroView(self.model)
        while self.model.mins != self.model.duration:
            view.time()
            self.model.secs += 1
            if self.model.secs == 60:
                self.model.mins += 1
                self.model.secs = 0
            time.sleep(1)
        self.stop()

    def stop(self, msg="Pomodoro finished!"):
        """Adds a complete pomodoro to the count and opens
           the pomocount file."""
        print(msg)
        self.model.total_pomodoros += 1
        self.model.mins = 0
        self.model.secs = 0

    def interrupt(self):
        """Stops the pomodoro and returns to original state"""


class PomodoroView():
    """Holds the methods to view the data inside PomodoroModel instances."""

    def __init__(self, model):
        self.model = model

    def time(self):
        sys.stdout.write(self.model.get_time() + '\r')
        sys.stdout.flush()

def test():
    p = PomodoroModel(1)
    c = PomodoroController(p)
    c.start()

test()

