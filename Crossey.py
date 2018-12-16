#Remove all non alpha
#Input sentence Convert sentence into array, with each section a word.
import sys
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
        if first in ['a', 'e', 'i', 'o', 'u'] or len(word) < 3:
            new_word = word + pyg
        elif word[0] + word[1] + word[2] in clusters_three:
            first_three = word[3:]
            new_word = first_three + word[:3] + pyg
        elif word[0] + word[1] in clusters_two:
            first_two = word[2:]
            new_word = first_two + word[:2] + pyg
        else:
            new_word = word + first + pyg
            new_word = new_word[1:]
        return(new_word)
    else:
        return ''
print("Welcome to the Pig Latin Translator, enter a sentence to be translated, or type exit to quit!")
loop = 5
while loop == 5:
    sentence = input("Enter a sentence: ")
    sentence = clean(sentence)
    if sentence == "exit":
        print("Exiting...")
        sys.exit()
    else:
        for word in sentence.split():
            print(convert(word), end=" ")
        print("")
