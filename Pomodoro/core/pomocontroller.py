# The controller is responsible for changing the vars inside the model and
# relaying the data to the view

import time

class PomodoroController():
    """Controls the model."""

    def __init__(self, model, view):
        """Parameters: PomodoroModel object and a PomodoroView object"""
        self.model = model
        self.view = view

    def start_timer(self, duration):
        """Begins counting the time."""

        while self.model.mins != duration:
            self.view.display(self.model.get_time())
            self.model.secs += 1
            if self.model.secs == 60:
                self.model.mins += 1
                self.model.secs = 0
            time.sleep(1)

    def stop(self, msg="Pomodoro finished!"):
        """Adds a complete pomodoro to the count and updates
           the pomocount file."""
        print(msg)
        self.model.update_db()
        self.log_pomodoros()
        self.reset()

    def reset(self):
        """Returns the model's mins and secs value to 0"""
        self.model.mins = 0
        self.model.secs = 0

    def interrupt(self, msg="Pomodoro has been interrupted."):
        """Stops the pomodoro and returns to original state"""
        self.view.display(msg)
        self.reset()

    def start_break(self, msg="Break time! Get some rest <3"):
        """Sets a <break> duration timer so the user gets a rest"""
        self.view.display(msg)
        self.start_timer(self.model.break_duration)
        self.model.break_count += 1
        self.reset()

    def long_break(self, msg="Long break time! Maybe it's a good idea to do \
                   some other activity, then resume this one!"):
        """Sets a <long_break> duration timer"""
        self.view.display(msg)
        self.model.break_count = 0
        self.start_timer(self.model.long_break_duration)
        self.reset()

    def lifecycle(self, msg="Beginning pomodoro... focus!"):
        """Standardizes a pomodoro lifecycle."""
        current_pomocount = self.model.db_file[self.model.current_day]
        prompt = "Pomodoros completed today: "
        self.view.display(prompt + str(current_pomocount))
        self.view.display(msg)

        interrupted = False
        while not interrupted:
            try:
                self.start_timer(self.model.duration)
                self.model.update_db()
                self.stop()
                # Implementing breaks
                if self.model.break_count < 3:
                    self.start_break()
                else:
                    self.long_break()

            except KeyboardInterrupt:
                self.interrupt()
                break

    def log_pomodoros(self):
        """Writes the task and pomodoros done into the log file"""

        path = self.model.get_pomocount_file("samplepomocount.txt")
        self.view.display("Opening pomocount file in %s" % path)
        log_format = "%d pomodoros - %s\n"

        # With this we'll need to get a generic input function
        # BTW, the implementation of a pre-defined input depends on the
        # platform you're working in
        self.view.display("Last completed task: %s" % self.model.previous_task)
        task = input("Task completed: ")
        if task not in self.model.completed_tasks:
            self.model.completed_tasks[task] = 1
        else:
            self.model.completed_tasks[task] += 1

        with open(path, 'w') as log_file:
            for task, pomos in self.model.completed_tasks.items():
                self.view.display("Logging task: %s" % task)
                log_file.write(log_format % (pomos, task))

