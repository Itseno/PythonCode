# abstraction, later in this code we will use something from the non-standard
# Python libraries, so we need to import this
import operator

# get how many the user wants to display the count of
top_count = int(input( "How many do you want to display? " ))
while top_count < 1:
  top_count = int(input( "How many do you want to display? " ))

# borrowed from another project, good thing we made it a function
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
def clean( input ):
  clean = ''
  for character in input:
    if character in alphabet:
      clean += character
  return clean.lower()

userInput = input("Name of the file to be scanned:")
if userInput = 1:
    userInput = "carols.txt"
common = input("Name of the file of common words:")
if common == 1:
    common = "common.txt"

# initialize some variables and load in our text file
counts = {}
input = clean(open(userInput).read())
common = clean(open(common).read())
# step through our text, counting each word and putting it into our dictionary
# if the word hasn't been added, we set it to 0 before counting
for word in input.split():
    if word in common:
        counts[word] = 0
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

# abstraction, we won't cover how this works but it does
# this line will change our dictionary into a list ordered by the value
# of each item (which is our count), we added "reverse" to start at the top
# and order decending
counts = sorted( counts.items(), key=operator.itemgetter(1), reverse=True )

# get only the top number of results based on the user input from before
top = counts[:top_count]

# output a nice "top board" of counts
count = 1
for item in top:
  print( "#" + str(count) + "\t\t" + item[0] + "\t\t" + str(item[1]) )
  count += 1
