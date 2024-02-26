#!/home/pdajgs/python_labs/py3.7/bin/python3

import threading, time

print('Start of program')

def takeANap():
    time.sleep(5)
    print('Wake up!')

theadObj = threading.Thread(target=takeANap)
theadObj.start()

print('End of program.')