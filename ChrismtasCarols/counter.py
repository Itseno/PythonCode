import operator

top_count = int(input("How many do you want to display? "))
while top_count < 1:
    top_count = int(input("How many do you want to display? "))

file = str(input('Where is carols file? '))
if len(file) < 1:
    file = "carols.txt"
common = str(input('Where is common file? '))
if len(common) < 1:
    common = "common.txt"

alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM "

def clean(input):
    clean = ""
    for character in input:
        if character in alphabet:
            clean += character
    return clean.lower()

counts = {}

carol = clean(open(file).read())

common = clean(open(common).read())

for word in carol.split():
    if word not in common:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
