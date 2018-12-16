import sys
pyg = "ay"

clusters_two = ["sh", "gl", "ch", "ph", "tr", "br", "fr", "bl", "gr", "st", "sl", "cl", "pl", "fl"]
clusters_three = ["str", "thr"]

x = ""

while x != "exit":
    x = str(input("Input a word!"))
    if len(x) > 0 and x.isalpha():
        new_word = ""
        word = x.lower()
        first = word[0]
        if x is "exit":
            sys.exit()
        elif first in ["a", "e", "i", "o", "u"]:
            new_word = word + pyg
            print(new_word)
        elif word[0] + word[1] + word[2] in clusters_three:
            first_three = word[3:]
            new_word = first_three + word[:3] + pyg
            print(new_word)
        elif word[0] + word[1] in clusters_two:
            first_two = word[2:]
            new_word = first_two + word[:2] + pyg
            print(new_word)
        else:
            new_word = word + first + pyg
            new_word = new_word[1:]
            print(new_word)
    else:
        print("Empty")
