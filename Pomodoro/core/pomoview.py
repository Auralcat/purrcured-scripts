# The view displays data to the user.

class PomodoroView():
    """Holds the methods to view the data inside PomodoroModel instances."""

    def __init__(self, model, print_func):
        """Initialization parameters: PomodoroModel object and a print func"""
        self.model = model
        self.print_func = print_func

    def display(self, text):
        """Shows the message using the function received in __init__"""
        self.print_func(text)
