# The controller is responsible for changing the vars inside the model and
# relaying the data to the view

import time
from pomoview import PomodoroView

class PomodoroController():
    """Controls the model."""

    def __init__(self, model):
        self.model = model

    def start_timer(self, duration):
        """Begins counting the time."""
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
        self.model.update_db()
        self.model.open_pomocount_file("samplepomocount.txt")
        self.reset()

    def reset(self):
        """Returns the model's mins and secs value to 0"""
        self.model.mins = 0
        self.model.secs = 0

    def interrupt(self, msg="Pomodoro has been interrupted."):
        """Stops the pomodoro and returns to original state"""
        print('\r' + msg)
        self.reset()

    def start_break(self, msg="Break time! Get some rest <3"):
        """Sets a <break> duration timer so the user gets a rest"""
        self.start_timer(self.model.break_duration)
        self.model.break_count += 1
        self.reset()

    def long_break(self, msg="Long break time! Maybe it's a good idea to do \
                   some other activity, then resume this one!"):
        """Sets a <long_break> duration timer"""
        self.model.break_count = 0
        self.start_timer(self.model.long_break_duration)
        self.reset()

    def lifecycle(self, msg="Beginning pomodoro... focus!"):
        """Standardizes a pomodoro lifecycle."""
        current_pomocount = self.model.db_file[self.model.current_day]
        print("Pomodoros completed today: " + str(current_pomocount))

        print(msg)
        interrupted = False
        while not interrupted:
            try:
                self.start_timer(self.model.duration)
                self.model.update_db()
                self.model.open_pomocount_file("samplepomocount.txt")

                # Implementing breaks
                if self.model.break_count < 3:
                    self.start_break()
                else:
                    self.long_break()

            except KeyboardInterrupt:
                self.interrupt()
                interrupted = True

