#9/27/22

import random

#asking for a input from user, after that the computer generates a random number from 1-10
user_choice1 = int (input("Choose a number : "))
comp_choice = random.randint(1,10)


#First try, if number is higher than comp choice, then print lower.
#if number is lower than comp choice then print higher
if user_choice1 > comp_choice :
    print ("Lower")
if user_choice1 < comp_choice :
    print ("Higher")
#Second try, same thing as first try
user_choice2 = int (input("Choose a number : "))
if user_choice2 > comp_choice :
    print ("Lower")
if user_choice2 < comp_choice :
    print ("Higher")
#Third try, same thing as first try
user_choice3 = int (input("Choose a number : "))
if user_choice3 > comp_choice :
    print ("Lower")
if user_choice3 < comp_choice :
    print ("Higher")
#Fourth try last try, if number is == to comp choice then print you won, if not then print you lost and the comp choice
user_choice4 = int (input("Choose a number : "))
if user_choice4 > comp_choice :
    print ("Lower")
if user_choice4 < comp_choice :
    print ("Higher")
elif user_choice4 == comp_choice : 
    print ("You Won")
else:
    print ("You lost, the number was", comp_choice)

  
