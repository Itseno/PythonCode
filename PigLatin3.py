#Remove all non alpha
#Input sentence Convert sentence into array, with each section a word.
import sys
loop = True
pyg = "ay"

alphabet = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm "
clusters_two = ["sh", "gl", "ch", "ph", "tr", "br", "fr", "bl", "gr", "st", "sl", "cl", "pl", "fl"]
clusters_three = ["str", "thr"]

def clean(input):
    clean = ""
    for character in input:
        if character in alphabet:
            clean += character
    return clean.lower()


def convert(word):
    if len(word) > 0 and word.isalpha():
        new_word = ''
        first = word[0]
        if first in ["a", "e", "i", "o", "u"] or len(word) < 3:
            new_word = word + pyg
            print(new_word, end=" ")
        elif word[0] + word[1] + word[2] in clusters_three:
            first_three = word[3:]
            new_word = first_three + word[:3] + pyg
            print(new_word, end=" ")
        elif word[0] + word[1] in clusters_two:
            first_two = word[2:]
            new_word = first_two + word[:2] + pyg
            print(new_word, end=" ")
        else:
            new_word = word + first + pyg
            new_word = new_word[1:]
            print(new_word, end=" ")

sentence = ""
while loop is True:
    sentence = input("Enter a sentence: ")
    if sentence is "exit" or "Exit":
        loop = False
        sys.exit()
    else:
        for word in sentence.split():
            print(convert(word), end=" ")


'''
def convert(word):
    first = word[0]
    if word is "exit":
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

def pigy():
    sentence = input("Enter a sentence: ")
    sentence = clean(sentence)
    sentence = sentence.split()
    new_sentence = convert(sentence)

pigy()
##############
while sentence != "exit":
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

#New stuff
pyg = "ay"

sentence = input("Enter a sentence: ")
for word in sentence.split():
    print(word)

alphabet = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuipasdfghjklzxcvbnm "
word = str(input("Enter a word: "))
for character in word:
    if character in alphabet:
        clean += character

print(clean)



x = ""
'''
