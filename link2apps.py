import webbrowser
import time
import subprocess
import pyautogui 

# Slack
time.sleep(1)
subprocess.Popen('C:\\Users\\VDA Labs 3\\AppData\\Local\\slack\\app-4.26.2\\slack.exe')
time.sleep(1)
pyautogui.keyDown("win")
pyautogui.press("up")
pyautogui.keyUp("win")
time.sleep(1)

# File Explorer
time.sleep(1)
pyautogui.keyDown("win")
pyautogui.press("E")
pyautogui.keyUp("win")
time.sleep(1)
pyautogui.keyDown("win")
pyautogui.press("up")
pyautogui.keyUp("win")
time.sleep(1)

# Settings
time.sleep(1)
pyautogui.keyDown("win")
pyautogui.press("i")
pyautogui.keyUp("win")
time.sleep(1)
pyautogui.keyDown("win")
pyautogui.press("up")
pyautogui.keyUp("win")
time.sleep(1)

# Powershell
time.sleep(1)
pyautogui.keyDown("win")
pyautogui.press("1")
pyautogui.keyUp("win")
time.sleep(1)
pyautogui.keyDown("win")
pyautogui.press("up")
pyautogui.keyUp("win")
time.sleep(1)