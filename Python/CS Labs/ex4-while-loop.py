#10/11/22

#i = 1 and while i is less than 6, it will keep looping
i = 1
while i<6:
#whatever i is it will multiply "#" and then print
    print ("#" * i)
#i += 1 adds 1 to i
    i += 1


print("---------------------")

#asking input for number of row
row = input('Enter number of rows : ')
#turning row into a int since it didnt ask for a int input on top
row = int(row)


for i in range(1,row+1):
    for x in range(1,i+1):
        print("#",end="")
    print("")