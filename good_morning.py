import webbrowser
import time
import subprocess
import pyautogui 

# below is a template for creating a new entry.
# name 
# time.sleep(3)
# webbrowser.open('', new=2)

print('INITIATING STARTUP SEQUENCE...')
# mail
time.sleep(3)
webbrowser.open('https://mail.google.com/mail/u/0/#inbox', new=1)

# calendar
time.sleep(3)
webbrowser.open('https://calendar.google.com/calendar/u/0/r?tab=rc&pli=1', new=2)

# Shane's Primary File
time.sleep(3)
webbrowser.open('https://docs.google.com/spreadsheets/d/1VlNqJ1qSAVcSN5PTzdf8cwXmkFU7cb5RlGmpG5HjwQg/edit#gid=1731413837', new=2)

# Try Hack Me Dashboard
# time.sleep(3)
# webbrowser.open('https://tryhackme.com/dashboard', new=2)

# Palo Alto Beacon 
# time.sleep(3)
# webbrowser.open('https://beacon.paloaltonetworks.com/student/catalog', new=2)

# Google
time.sleep(3)
webbrowser.open('https://www.google.com/', new=2)

# SNYPR Cheat Sheet
time.sleep(3)
webbrowser.open('https://docs.google.com/spreadsheets/d/1Q427RonQa9CfSdTs-w8MtiKhBP3K7_oSqJpK0yIPznc/edit#gid=1654361937', new=2)

# SNYPR
time.sleep(3)
webbrowser.open('https://a1t5plmnha.securonix.net/Snypr/', new=2)

# Virus Total
time.sleep(3)
webbrowser.open('https://www.virustotal.com/gui/home/upload', new=2)

# Nessus
time.sleep(3)
webbrowser.open('https://127.0.0.1:8834/#/', new=2)

# Rumble
time.sleep(3)
webbrowser.open('https://console.rumble.run/', new=2)

# Import link to apps
time.sleep(3)
import link2apps
time.sleep(3)

# Import link to documents
time.sleep(3)
import link2dox
time.sleep(3)

time.sleep(1)
print('...STARTUP SEQUENCE COMPLETE')
time.sleep(1)
print('-end of transmission-')