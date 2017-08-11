# The model holds the data for the programs. The idea here is to leave it as
# open as possible for new programs to use it.

import datetime
import shelve
import os

class PomodoroModel():
    """The Pomodoro object holds the data about the completed pomodoros and the
       methods to interact with it."""

    total_pomodoros = 0
    break_count = 0

    def __init__(self, db_path, duration=25, break_duration=5,
                 long_break_duration=30):
        """Sets the duration of a pomodoro session and initializes
           the variables"""
        self.duration = duration
        self.break_duration = break_duration
        self.long_break_duration = long_break_duration
        self.mins = 0
        self.secs = 0

        # Getting the current day:
        now = datetime.datetime.now()
        self.current_day = now.strftime("%d/%m/%Y")

        self.db_file = self.get_db(db_path)

    def get_db(self, db_path):
        """Passes the database object to be used with shelve."""
        # Fixing database path.
        # If it doesn't exist, it will be created.
        home = os.environ.get("HOME")
        if not os.path.exists(os.path.join(home, db_path)):
            new_db = shelve.open(os.path.join(home, db_path))
            new_db.close()

        # Tracking the total amount of pomodoros
        print("Opening shelf in %s" % db_path)
        dbfile = shelve.open(os.path.join(home, db_path))

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

    def open_pomocount_file(self, count_file_path):
        """Returns the pomocount file if there is one."""

        # Fixing pomocount path
        home = os.environ.get("HOME")
        editor = os.environ.get("EDITOR")
        path = os.path.join(home, count_file_path)

        # If there's no file in the destination, we'll create a sample one
        if not os.path.exists(path):
            text = ("# This is a new pomocount file." +
                    " You can track your work " +
                    "like so:\n\n# (number) pomodoros - Task executed\n\n")
            with open(path, 'w') as new_pomocount_file:
                new_pomocount_file.write(text)

        # Call the editor
        os.system(" ".join([editor, path]))
