# TODO: Integrate the time module
#       Make it so you can append the pomodoro data to a view

import time
import sys

class Pomodoro():
    """The Pomodoro object holds the data about the completed pomodoros and the
       methods to interact with it."""

    total_pomodoros = 0

    def __init__(self, display_func, duration=25):
        """Sets the duration of a pomodoro session and initializes
           the variables"""
        self.duration = duration
        self.mins = 0
        self.secs = 0
        self.display_func = display_func()

        self.start()
        self.stop()

    def start(self, msg="Beginning pomodoro... focus!"):
        """Begins counting the time."""
        print(msg)

        while self.mins != self.duration:
            self.display_func()
            self.secs += 1
            if self.secs == 60:
                self.mins += 1
                self.secs = 0
            time.sleep(1)

    def stop(self, msg="Pomodoro finished!"):
        """Adds a complete pomodoro to the count and opens
           the pomocount file."""
        print(msg)
        self.total_pomodoros += 1
        self.mins = 0
        self.secs = 0

    def interrupt(self):
        """Stops the pomodoro and returns to original state"""

    def get_time(self):
        """Returns a string with the elapsed pomodoro time."""
        display_time = "{}:{}".format(str(self.mins).zfill(2),
                                      str(self.secs).zfill(2))

        return display_time

def display(reading):
    """External function to display the elapsed time"""
    sys.stdout.write(reading + '\r')
    sys.stdout.flush()

def test():
    p = Pomodoro(1, display)

test()
