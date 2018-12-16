# 10 line story, with 3 variables, one a number one a string.
import sys
x = int(input("Enter your age:"))

if x < 13 or x > 100:
    print("Please make sure your age,is between 13 and 100.")
    sys.exit()

y = input("Enter your name:")
print("Hello " + y + ". Let's play a game!")
z = str(input("Give me an animal:"))
if z == "pig" or z == "cow":
    print("I see you chose " + z + ", one of my favorite animals!")
a = str(input("Give me a verb ending in -ing:"))
if a == "running" and y != "Ian":
    print("Lol, you are a bad runner!")
elif a == "walking":
    print("Yeah I bet you prefer walking.")

b = input("Are you ready for your story?")
if b == "yes":
    print("Great!")
elif b == "no":
    print("Ok, bye.")
    sys.exit()
else:
    print("Well, here's your story anyway.")

print("Once upon a time, a brave knight named, " + y + " entered into a strange land.")
print("This land was filled with all kinds of animals, most notably the evil " + z + " .")
print(y + " fought the " + z + " and claimed it as his own.")
print("From then on " + y + " became renowned for his military tactic of " + a + " .")
