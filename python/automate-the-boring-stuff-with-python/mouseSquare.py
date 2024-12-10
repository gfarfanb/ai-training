import pyautogui

for i in range(5):
    pyautogui.moveTo(100, 0, duration=0.25)  # right
    pyautogui.moveTo(0, 100, duration=0.25)  # down
    pyautogui.moveTo(-100, 0, duration=0.25) # left
    pyautogui.moveTo(0, -100, duration=0.25) # up
