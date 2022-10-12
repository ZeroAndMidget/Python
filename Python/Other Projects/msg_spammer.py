import time
import pyautogui as pag

times = int(input("How many times? : "))
wait = int(input("How many seconds between each message? : "))
message = input("Whats the message? :")

print("Spamming in 5 . . . ")
time.sleep(1)
print("Spamming in 4 . . . ")
time.sleep(1)
print("Spamming in 3 . . . ")
time.sleep(1)
print("Spamming in 2 . . . ")
time.sleep(1)
print("Spamming in 1 . . . ")
time.sleep(1)

i = 1
while(i<=times):
    pag.write(message)
    time.sleep(wait)
    pag.press('Enter')
    i += 1