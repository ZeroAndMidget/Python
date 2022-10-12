#9/27/22

import random

#asking for a input from user, after that the computer generates a random number from 1-3
user_choice = (input("Enter your choice of Rock(R), Paper(P), or Scissors(S) : "))
comp_choice = random.randint(1,3)

#Choice 1 = rock, if comp generates 1 then its rock, if 2 then its paper, if 3 its scissors
if user_choice == "R" :
    if comp_choice == 1 :
        print("You chose rock. The computer chose rock. You tied.")
    
    elif comp_choice == 2 :
        print("You chose rock. The computer chose paper. You lose.")
        
    elif comp_choice == 3 :
        print("You chose rock. The computer chose scissors. You win.")
#Choice 2 = paper, if comp generates 1 then its rock, if 2 then its paper, if 3 its scissors
elif user_choice == "P" :
    if comp_choice == 1 :
        print("You chose paper. The computer chose rock. You win.")
    
    elif comp_choice == 2 :
        print("You chose paper. The computer chose paper. You tied.")
        
    elif comp_choice == 3 :
        print("You chose paper. The computer chose scissors. You lose.")
#Choice 3 = scissors, if comp generates 1 then its rock, if 2 then its paper, if 3 its scissors
elif user_choice == "S" :
    if comp_choice == 1 :
        print("You chose scissors. The computer chose rock. You lose.")
    
    elif comp_choice == 2 :
        print("You chose scissors. The computer chose paper. You win.")
        
    elif comp_choice == 3 :
        print("You chose scissors. The computer chose scissors. You tied.")