#Rong Cong Yu

#A
# three variables are being assigned a str
animal_1 = "A Red Fox"
animal_2 = "chased a Blue mouse"
meadow = "across a Green meadow"

# print out each variable to test it
print(animal_1)
print(animal_2)
print(meadow)

print()
print("------------------------")

#B
# the results variable concatenates the three variables from part A
results = animal_1 + " " + animal_2 + " " + meadow

# print out the variable results as a sentence
print(results)

print()
print("------------------------")

#C
# the .lower() method makes every character from the results variable lower case
print(results.lower())
# print out original and lower case method to compare
print(results)

print()
print("------------------------")

#D
# the .upper() method will print out the full string in all UPPER case characters
print(results.upper())
# print out original and upper case method to compare
print(results)

print()
print("------------------------")

#E
# access character at index 19
print(results[19])

print()
print("------------------------")

#F
# created a new variable that contains a list of the three variables in the results variable
# results_list is assigned to index 1 which is animal_2 in the list
# access the word 'Blue' between index[9:14]
results_list = [animal_1, animal_2, meadow]
results_list = results_list[1]
print(results_list[9:14])

print()
print("------------------------")

#G
results_list = [animal_1, animal_2, meadow]
print(len(results_list[0]) + len(results_list[1]) + len(results_list[2]))

print()
print("------------------------")

