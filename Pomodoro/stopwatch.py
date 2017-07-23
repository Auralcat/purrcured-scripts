#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""This is a module for tracking time on the terminal."""

import time
import os
import sys
import shelve
import datetime

# Getting the current day:
now = datetime.datetime.now()
current_day = now.strftime("%d/%m/%Y")

# Checking where the database is:
pwd = os.getcwd()
print("Checking for database in {}".format(pwd))

# Tracking the total amount of pomodoros:
total_pomodoros = shelve.open('total-pomodoro-count')

# If there's no instance of the current day in the shelf file, we'll create one
if current_day not in total_pomodoros:
    total_pomodoros[current_day] = 0

current_pomocount = total_pomodoros[current_day]
print("Pomodoros completed today: " + str(current_pomocount))
mins, secs = 0, 0

# Here's where you set the amount of minutes you want it to count:
while mins != 1:
    secs += 1
    if secs == 60:
        mins += 1
        secs = 0
    display_time = "{}:{}".format(str(mins).zfill(2),
                                  str(secs).zfill(2))
    sys.stdout.write(display_time+'\r')
    sys.stdout.flush()
    time.sleep(1)

print(display_time)

# Once the pomodoro is finished, we add it to the count.
current_pomocount += 1
total_pomodoros[current_day] = current_pomocount
total_pomodoros.close()
