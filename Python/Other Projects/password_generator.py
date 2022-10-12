import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%^&*/\?"			

user_for = lower_case + upper_case + number +symbols

print ("=== Password Generator ===")
lenght_for_pass = int(input("Lenght of password (Must be less than 72): "))
password = "".join(random.sample(user_for, lenght_for_pass))
print ("Generated Password: " , password)
