import operator

print("Welcome to the word counter! This program takes a carols file and a common file, and lists the top words present in the carols file, excluding words appreaing in the common file. If you would like to use the carols and common files, just type the number 1, when prompted for their location!")

top_count = int(input( "How many top counts do you want? " ))
while top_count < 1:
  top_count = int(input( "Please enter at least 1: " ))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
def clean( input ):
  clean = ''
  for character in input:
    if character in alphabet:
      clean += character
  return clean.lower()

userInput = input("Where is the file that is being scanned? (Type 1 if you want to use the preset files.) ")
if userInput == 1:
userInput = input("Where is the file that is being scanned? (Type 1 if you want to use the preset files.) " )
if len(userInput) < 1:
    userInput = "carols.txt"
commonFile = input("Where is the file that has all the common words? (Type 1 if you want to use the preset files.) ")
if commonFile == 1:
    commonFile = "common.txt"
common = input("Where is the file that has all the common words? (Type 1 if you want to use the preset files.)" )
if len(common) < 1:
    common = "common.txt"

count = {}
input = clean(open(userInput).read())
commonFile = clean(open(commonFile).read())
# step through our text, counting each word and putting it into our dictionary
# if the word hasn't been added, we set it to 0 before counting
for word in input.split():
    if word in commonFile:
        count[word] = 0
    if word not in count:
        count[word] = 0
    count[word] += 1

count = sorted( count.items(), key=operator.itemgetter(1), reverse=True )

top = count[:top_count]

count = 1
for item in top:
  print( "#" + str(count) + "\t\t" + item[0] + "\t\t" + str(item[1]) )
  count += 1
