#!/home/pdajgs/python_labs/py3.7/bin/python3

import time, subprocess

def alarme(timeLeft):
    while timeLeft > 0:
        print(timeLeft, end=' - ')
        time.sleep(1)
        timeLeft -= 1
    subprocess.Popen(['/usr/bin/rhythmbox', 'alarm.wav'])

alarme(10)
