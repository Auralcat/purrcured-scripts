#!/bin/bash

# Needs an open terminal window to display the info.

# Opens the pomodoro count file.
pomocount()
{
    vim ~/pomodorocount2017
}

# Message if the user hits <C-c>. That's pressing the CTRL
# and lowercase c keys together.
pomostop()
{
    echo -e "\nPomodoro stopped before completion."
    tmux rename-window "Pomodoro"
    exit 1
}

notify_start='notify-send --urgency=low --expire-time=5000'
notify_end='notify-send --urgency=low --expire-time=5000 -i face-smile-big'

# Displays start message as a popup notification in the desktop
$notify_start "Begin!" "Starting pomodoro..."
echo "Press CTRL+C to stop counting."
echo -e

# Getting ready to catch <C-c> input
trap pomostop SIGINT

# Changing window title in tmux
tmux rename-window "Focus!"

# Default time: 25 minutes
python3 ~/"Python Scripts"/stopwatch.py

# Another title change:
tmux rename-window "Done! ^-^"

# Displays end message as a popup notification in the desktop
$notify_end "Pomodoro finished!" "Opening pomodorocount..."

# Plays a sound clip for when the user doesn't see the notification.
# Requires mpv installed!
mpv "$HOME/purrcured-scripts/Pomodoro/sound/SchoolBell.ogg"

sleep 5s

pomocount

# Back to the original title
tmux rename-window "Pomodoro"
