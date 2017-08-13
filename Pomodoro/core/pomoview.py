# The view displays data to the user.

class PomodoroView():
    """Holds the methods to view the data inside PomodoroModel instances."""

    def __init__(self, model, print_func):
        """Initialization parameters: PomodoroModel object and a print func"""
        self.model = model
        self.print_func = print_func

    def time(self):
        """Returns a string containing the current time in the pomodoro"""
        display_time = "{}:{}".format(str(self.model.mins).zfill(2),
                                      str(self.model.secs).zfill(2))

        return display_time

    def display_time(self):
        """Shows the time using the function received in __init__"""
        self.print_func(self.time())
