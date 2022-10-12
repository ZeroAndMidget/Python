print ("=== C/F Converter ===")
print ("[1] C ==> F")
print ("[2] F ==> C")
print ("[3] EXIT")
converter = float(input("What would you like to convert? "))
if converter == 1 :
    c = float(input("Celsius: ")) 
    f = (c * 1.8) + 32
    print (">> Fahrenheit: " ,  f)
elif converter == 2 :
    f = float(input("Fahrenheit: ")) 
    c = (f - 32) * 5/9
    print (">> Celsius: " ,  c)
else :
    print ("Error . . .")