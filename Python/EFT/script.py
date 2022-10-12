import pyautogui
import time
import os
from sty import fg, bg, ef, rs
#pyautogui.mouseInfo() SHOWS COORDS

clear = lambda: os.system('cls')
clear()

print (fg.blue + "[" + fg.li_blue + "1" + fg.blue + "] " + fg.li_blue + "How many keycards would you like to purchase?" + fg.rs)
amount = float (input(fg.blue + "[" + fg.li_blue + "2" + fg.blue + "] "+ fg.li_blue + "Please Select: " + fg.rs))

clear = lambda: os.system('cls')
clear()

print (bg.blue + "    " + fg.li_blue + "Resoultion" "    " + fg.rs + bg.rs)
print (fg.blue + "[" + fg.li_blue + "1" + fg.blue + "] " + fg.li_blue + "1920x1080 " + fg.rs)
print (fg.blue + "[" + fg.li_blue + "2" + fg.blue + "]" + fg.li_blue + " 2560x1440 " + fg.rs)
selection = int(input(fg.blue + "[" + fg.li_blue + "3" + fg.blue + "]" + fg.li_blue + " Please Select:  " + fg.rs))
clear = lambda: os.system('cls')
clear()

i = 1
while(i<=amount):
    cooldown = int("3650") #2 Hours and 30 Minutes
    purchased = (fg.blue + bg.da_blue + "[" + fg.li_blue + "Purchase" + fg.blue + "]" + bg.rs + fg.li_blue + " Successful " + fg.rs + bg.rs)
    time.sleep(5)
    if selection == 1 :
        pyautogui.moveTo(958, 182)
    elif selection == 2 :
        pyautogui.moveTo(1258, 235)
    pyautogui.click(button='Left') 
    print(purchased)
    time.sleep(cooldown)
    pyautogui.click(button='Left')
    i+=1