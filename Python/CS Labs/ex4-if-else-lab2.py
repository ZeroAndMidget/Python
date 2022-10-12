#9/27/22

#printing what shapes there are
print ("Triangle")
print ("Square")
print ("Pentagon")
print ("Octogon")
#getting a input from user
user_choice = input("Choose a shape: ")

#asking questions and getting a Y/N input
question1 = input("Does it have 3 sides? [Y/N] : ")
question2 = input("Does it have 4 sides? [Y/N] : ")
question3 = input("Does it have 5 sides? [Y/N] : ")
question4 = input("Does it have 6 sides? [Y/N] : ")
#if question1 is Y then print its a triangle
if question1 == "Y" : 
    print ("Its a triangle and you choose", user_choice)
#if not Y then print nothing
else:
    print ()
#if question2 is Y then print its a Square
if question2 == "Y" : 
    print ("Its a Square and you choose", user_choice)
#if not Y then print nothing
else: 
    print ()
#if question3 is Y then print its a Pentagon
if question3 == "Y" : 
    print ("Its a Pentagon and you choose", user_choice)
#if not Y then print nothing
else: 
    print ()
#if question4 is Y then print its a Octogon
if question4 == "Y" : 
    print ("Its a Octogon and you choose", user_choice)
#if not Y then print nothing
else: 
    print ()
