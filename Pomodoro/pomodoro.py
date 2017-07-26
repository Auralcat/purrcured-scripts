# TODO: Integrate the time module

import sys
import datetime
import shelve
import os

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
        self.db_path = self.get_db()

    def get_db(self):
        """Passes the database object to be used with shelve."""
        # Fixing database path
        home = os.environ.get("HOME")
        return os.path.join(home, "Python Scripts", "total-pomodoro-count")

    def get_time(self):
        """Returns a string with the elapsed pomodoro time."""
        display_time = "{}:{}".format(str(self.mins).zfill(2),
                                      str(self.secs).zfill(2))

        return display_time

class PomodoroController():
    """Controls the model."""

    def __init__(self, model):
        self.model = model

    def open_db(self):
        """Opens the database from the model"""

        # Getting the current day:
        now = datetime.datetime.now()
        current_day = now.strftime("%d/%m/%Y")

        # Tracking the total amount of pomodoros
        print("Opening shelf in %s" % self.model.db_path)
        with shelve.open(self.model.db_path, 'c') as dbfile:
            # If there's no instance of the current day in the shelf file,
            # we'll create one
            if current_day not in total_pomodoros:
                dbfile[current_day] = 0
            current_pomocount = total_pomodoros[current_day]

        print("Pomodoros completed today: " + str(current_pomocount))

    def start(self, msg="Beginning pomodoro... focus!"):
        """Begins counting the time."""
        self.open_db()
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
        self.reset()

    def reset(self, msg="Pomodoro interrupted."):
        """Returns the model's mins and secs value to 0"""
        self.model.mins = 0
        self.model.secs = 0

    def interrupt(self):
        """Stops the pomodoro and returns to original state"""


class PomodoroView():
    """Holds the methods to view the data inside PomodoroModel instances."""

    def __init__(self, model):
        self.model = model

    def time(self):
        display_time = "{}:{}".format(str(self.model.mins).zfill(2),
                                      str(self.model.secs).zfill(2))
        sys.stdout.write(display_time + '\r')
        sys.stdout.flush()

def test():
    p = PomodoroModel(1)
    c = PomodoroController(p)
    c.start()

test()

