from email import message
import random
from sys import get_coroutine_origin_tracking_depth
import time
import pyautogui as pag

word = "nigger"
		

user_for = word


x=1
while x<=10:
    message = "".join(random.sample(user_for, 6))
    time.sleep(1)
    pag.write("/all " + message)
    pag.press('Enter')
    x+=1

