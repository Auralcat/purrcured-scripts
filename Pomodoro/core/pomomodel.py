# The model holds the data for the programs. The idea here is to leave it as
# open as possible for new programs to use it.

"""
Module to hold the PomodoroModel class.
It takes the following parameters for the __init__() method:
- db_path -> Path to the pomodoro database (created by the shelf module)
- duration (default: 25 minutes) -> Duration of a pomodoro session
(excluding breaks and long breaks)
- break_duration -> Duration of a break after a pomodoro has been completed
- long_break_duration -> Duration of a long break, which is triggered by
completing 3 pomodoros (will be adjustable soon)

"""
import datetime
import shelve
import os
import subprocess
from collections import OrderedDict

class PomodoroModel():
    """The Pomodoro object holds the data about the completed pomodoros and the
       methods to interact with it."""

    total_pomodoros = 0
    break_count = 0
    home = os.environ.get("HOME")

    def __init__(self, db_path, duration=25, break_duration=5,
                 long_break_duration=30):
        """Sets the duration of a pomodoro session and initializes
           the variables"""
        self.duration = duration
        self.break_duration = break_duration
        self.long_break_duration = long_break_duration
        self.mins = 0
        self.secs = 0
        self.completed_tasks = OrderedDict()
        # Getting the current day:
        now = datetime.datetime.now()
        self.current_day = now.strftime("%d/%m/%Y")

        self.db_file = self.get_db(db_path)

    def get_db(self, db_path):
        """Passes the database object to be used with shelve."""
        # Fixing database path.
        # If it doesn't exist, it will be created.
        if not os.path.exists(os.path.join(self.home, db_path)):
            print("Creating database in %s" % (os.path.join(self.home, db_path)))
            new_db = shelve.open(os.path.join(self.home, db_path))
            new_db.close()

        # Tracking the total amount of pomodoros
        print("Opening shelf in %s" % db_path)
        dbfile = shelve.open(os.path.join(self.home, db_path))

        # If there's no instance of the current day in the shelf file,
        # we'll create one
        if self.current_day not in dbfile:
            dbfile[self.current_day] = 0

        return dbfile

    def update_db(self):
        """Updates the pomodoro count in the db"""
        self.db_file[self.current_day] += 1

    def get_time(self):
        """Returns a string with the elapsed pomodoro time."""
        display_time = "{}:{}".format(str(self.mins).zfill(2),
                                      str(self.secs).zfill(2))

        return display_time

    def get_pomocount_file(self, count_file_path):
        """Returns the path to the pomocount file.
           If the file doesn't exist, it will be created."""

        # Fixing pomocount path
        editor = os.environ.get("EDITOR")
        path = os.path.join(self.home, count_file_path)

        if not os.path.exists(path):
            text = ("# This is a new pomocount file." +
                    " You can track your work " +
                    "like so:\n\n# (number) pomodoros - Task executed\n\n")
            with open(path, 'w') as new_pomocount_file:
                new_pomocount_file.write(text)

        # Call the editor
        subprocess.call([editor, path])

