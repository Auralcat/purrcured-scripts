# TODO: Integrate the time module

import sys
import datetime
import shelve
import os
import time

class PomodoroModel():
    """The Pomodoro object holds the data about the completed pomodoros and the
       methods to interact with it."""

    total_pomodoros = 0
    break_count = 0

    def __init__(self, duration=25, break_duration=5,
                 long_break_duration=30):
        """Sets the duration of a pomodoro session and initializes
           the variables"""
        self.duration = duration
        self.break_duration = break_duration
        self.long_break_duration = long_break_duration
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

    def get_pomocount_file(self):
        """Returns the pomocount file if there is one."""

        # Fixing pomocount path
        home = os.environ.get("HOME")
        return os.path.join(home, "pomodorocount2017")

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
        dbfile = shelve.open(self.model.db_path)
        # If there's no instance of the current day in the shelf file,
        # we'll create one
        if current_day not in self.model.total_pomodoros:
            dbfile[current_day] = 0
        current_pomocount = self.model.total_pomodoros[current_day]
        dbfile.close()

        print("Pomodoros completed today: " + str(current_pomocount))

    def start_timer(self, duration):
        """Begins counting the time."""
        self.open_db()
        print(msg)
        view = PomodoroView(self.model)
        while self.model.mins != duration:
            view.time()
            self.model.secs += 1
            if self.model.secs == 60:
                self.model.mins += 1
                self.model.secs = 0
            time.sleep(1)

    def stop(self, msg="Pomodoro finished!"):
        """Adds a complete pomodoro to the count and opens
           the pomocount file."""
        print(msg)
        self.reset()

    def reset(self):
        """Returns the model's mins and secs value to 0"""
        self.model.mins = 0
        self.model.secs = 0

    def interrupt(self, msg="Pomodoro has been interrupted."):
        """Stops the pomodoro and returns to original state"""
        print('\r' + msg)
        self.reset()

    def break(self, msg="Break time! Get some rest <3"):
        """Sets a <break> duration timer so the user gets a rest"""
        self.start_time(self.break_duration)
        self.break_count += 1
        self.stop()

    def long_break(self, msg="Long break time! Maybe it's a good idea to do
                   some other activity, then resume this one!")
        """Sets a <long_break> duration timer"""
        self.break_count = 0
        self.start_time(self.long_break_duration)
        self.stop()

    def lifecycle(self, msg="Beginning pomodoro... focus!"):
        """Standardizes a pomodoro lifecycle."""
        self.open_db()
        print(msg)

        try:
            self.start_timer()
        except KeyboardInterrupt:
            self.interrupt()
        except:
            print("Uh-oh! An error has occurred!")

        self.model.total_pomodoros += 1
        self.stop()

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
    c.lifecycle()

test()

