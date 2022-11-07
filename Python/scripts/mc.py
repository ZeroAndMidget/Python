import pyautogui as pag
import time

time.sleep(5)

x = 1
while 1:
    pag.mouseDown(button = "left")
    time.sleep(420)
    pag.mouseUp(button = "left")
    pag.press('Enter')
    pag.write("/fix all") 
    pag.press('Enter')
x+=1