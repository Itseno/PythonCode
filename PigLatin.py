import sys
pig = "ay"

clusters_two = ["sh", "gl", "ch", "ph", "tr", "br", "fr", "bl", "gr", "st", "sl", "cl", "pl", "fl"]
clusters_three = ["str", "thr"]

x = str(input("Input a word!"))

if x.isalpha() is False:
    print("I don't understand what you put in, try again!")
    sys.exit()

one = x[0].lower()
rest = x[1:len(x)].lower()

print(rest + one + pig)
