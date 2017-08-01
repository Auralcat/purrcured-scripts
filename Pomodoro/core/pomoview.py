# The view displays data to the user.

import sys

class PomodoroView():
    """Holds the methods to view the data inside PomodoroModel instances."""

    def __init__(self, model):
        self.model = model

    def time(self):
        display_time = "{}:{}".format(str(self.model.mins).zfill(2),
                                      str(self.model.secs).zfill(2))
        sys.stdout.write(display_time + '\r')
        sys.stdout.flush()
