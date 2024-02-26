#!/home/pdajgs/python_labs/py3.7/bin/python3

import pyautogui, time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

time.sleep(5)
pyautogui.click()
distance = 200

while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2) # move para direita
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2) # move para baixo
    pyautogui.dragRel(-distance, 0, duration=0.2) # move para esquerda
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2) # move para cima
print('Done!')