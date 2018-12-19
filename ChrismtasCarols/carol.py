import operator

top_count = int(input("How many do you want to display?"))
while top_count < 1:
    top_count = int(input("How many do you want to display?"))

alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM "

def clean(input):
    clean = ""
    for character in input:
        if character in alphabet:
            clean += character
    return clean.lower()

counts = {}
input = clean(open('13-Alice.txt').read())

for word in input.split():
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

counts = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)

top = counts[:top_count]

count = 1
for item in top:
    print("#" + str(count) + "\t\t" + item[0] + "\t\t" + str(item[1]))
    count += 1
