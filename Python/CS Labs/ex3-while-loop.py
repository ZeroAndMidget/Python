#10/11/22

#the starting number is 5
sum = 5

#while 1 creates a infinite loop since there is nothing change 1
while 1:
#asking for a user input
    add = input("Enter number to add, otherwise press q to quit:")
#if input is "q" then break
    if add == "q" : break
#if its not "q" then turn the input into a int
    add = int(add)
#sum is the starting number + the numbers that is being inputed
    sum = sum + add
#print out the subtotal
    print("Your subtotal is : ", sum)
    
#if "q" is pressed then it will print out the grand total
print("Your Grand Total is : ",sum)