#10/11/22

import time
import random

#prints a message and waits and prints next message
print("Hey")
time.sleep(0.5)
print("how")
time.sleep(1.0)
print("are")
time.sleep(1.0)
print("you")
time.sleep(1.0)
print("my")
time.sleep(1.0)
print("friend")

print("---------------------")

#i = 1, the code will loop everytime and add 1 to i until i = 10
i = 1
while(i<=10):
    print(i)
    i += 1

print("---------------------")

#i = 1, the code will loop everytime and add 1 to i until i = 10 and will print on the same line with "-" in between each number
i = 1
while(i<=10):
    print(i, end=" - ")
    i += 1

print("---------------------")

#i = 1, the code will loop everytime and add 1 to i until i = 5 and everytime it loops, it will wait 0.5 before printing i
i = 1
while(i<=5):
    time.sleep(0.5)
    print(i)
    i += 1

print("---------------------")

#i = 10 and it will loop till it gets to i = 20, everytime it loops it will print i and then add 2 to i
i = 10
while(i<=20):
    print(i)
    i += 2

print("---------------------")

#i = 20 and it will loop until i = 0, eveytime it loops, it will print i and minus 3 from i
i = 20
while(i>=0):
    print(i)
    i -= 3

print("---------------------")

#i = 1 and will loop until i = 10, everytime it loops it will generate a random number from 0-100 and will print the 10 generated numbers in one line
i = 1
while(i<=10):
    ten_numbers = random.randint(0, 100)
    print (ten_numbers, end = "")
    i += 1

print("---------------------")

#asking for a user input thats a int
number = int(input("Enter a value bigger than 100: "))

#loop ends if the number is bigger than 100 otherwise it will run forever
while number <= 100: 

    print("Enter a number greater than 100")

    number = int(input("Enter a value bigger than 100: "))
#if number is greater than 100, print "Thank you"
print("Thank you")

