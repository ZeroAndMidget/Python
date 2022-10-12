#10/11/22

#Asking for a int input, 1 2 3 and 4 represents a animal
animal = int(input("Fish(1), Tarantula(2), Snake(3), Octopus(4) : "))

#Asking for yes or no inputs for these questions
question1 = input("Does it live in water? [Y/N] :")
question2 = input("Does it have arms or legs [Y/N] : ")
#if question1 is Y and question2 is Y then print octopus
if question1 == "Y" :
    if question2 == "Y" :
        print("Its a octopus and you chose",animal)
#if question1 is Y and question2 is N then print fish
if question1 == "Y" :
    if question2 == "N" :
        print("Its a fish and you chose",animal)
#if question 1 is N and question2 is Y then print tarantula
if question1 == "N" :
    if question2 == "Y" :
        print("Its a tarantula and you chose", animal)
#if question1 is N and question 2 is N then print snake
if question1 == "N" :
    if question2 == "N" :
        print("Its a snake and you chose", animal)


