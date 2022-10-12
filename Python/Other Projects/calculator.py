print ("=== Calculator ===")
print ("[1] Add")
print ("[2] Subtract")
print ("[3] Multiply")
print ("[4] Divide")
print ("[5] EXIT")
selection = float (input("Select an option: "))
if selection == 1 : 
    num1 = float (input("First number: "))
    num2 = float (input("Second number: "))
    print (">> Answer: " , num1 + num2)
elif selection == 2 :
    num1 = float (input("First number: "))
    num2 = float (input("Second number: "))
    print (">> Answer: " , num1 - num2)
elif selection == 3 :
    num1 = float (input("First number: "))
    num2 = float (input("Second number: "))
    print (">> Answer: " , num1 * num2)
elif selection == 4 :
    num1 = float (input("First number: "))
    num2 = float (input("Second number: "))
    print (">> Answer: " , num1 / num2)
elif selection == 5 :
    print (">> Exiting . . .")
    exit()
else :
    print ("Error . . .")