import operator

alphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM "

def clean(input):
    clean = ""
    for character in input:
        if character in alphabet:
            clean += character
    return clean.lower()

countCarols = {}
countCommon = {}

carols = input("Where is the carols file?")
common = input("Where is the common file?")

top_count = int(input("How many do you want to display?"))
while top_count < 1:
    top_count = int(input("How many do you want to display?"))

inputCarols = clean(open(carols).read())
inputCommon = clean(open(common).read())

for word in inputCarols.split():
    if word not in countCarols:
        countCarols[word] = 0
    countCarols[word] += 1

for word in inputCommon.split():
    if word not in countCommon:
        countCommon[word] = 0
    countCommon[word] += 1

countCarols = sorted(countCarols.items(), key=operator.itemgetter(1), reverse=True)
countCommon = sorted(countCommon.items(), key=operator.itemgetter(1), reverse=True)

topCarols = countCarols[:top_count]
topCommon = countCommon[:top_count]

count = 1
for item in topCarols:
    print("#" + str(count) + "\t\t" + item[0] + "\t\t" + str(item[1]))
    count += 1

twocount = 1
for item in topCommon:
    print("#" + str(count) + "\t\t" + item[0] + "\t\t" + str(item[1]))
    twocount += 1
