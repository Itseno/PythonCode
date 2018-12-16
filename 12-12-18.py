#Remove all non alpha
#Input sentence Convert sentence into array, with each section a word.

alphabet = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm "

def clean(input):
    clean = ""
    for character in input:
        if character in alphabet:
            clean += character
    return clean.lower()

sentence = input("enter se")
sentence = clean(sentence)
print(sentence)

"""
import sys
pyg = "ay"

def yolo(argument):
    #do someting
    return "Blah"

print(yolo(arg))

sentence = input("Enter a sentence: ")
for word in sentence.split():
    print(word)

date_in = '12/12/18'
date_arr = date_in.split('/'):
print(date_arr)

alphabet = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuipasdfghjklzxcvbnm "
word = str(input("Enter a word: "))
for character in word:
    if character in alphabet:
        clean += character

print(clean)

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
        elif first in ["a", "e", "i", "o", "u"] or len(word) < 3:
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
"""
