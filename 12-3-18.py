#12-3-18 Notes
age = int(input("Age?"))
if age >= 0:
    print("Not necessarily a time traveller.")
else:
    print("You are a time traveller.")

height = int(input("How tall are you?"))

if height < 256:
    print("Too short for this ride")
else:
    print("Welcome aboard")

if ( True ):
    print("Always prints true.")

# < <= > >= == !=

if 0 < age < 21:
    print("Kid")
else:
    print("Adult")

print("good" in "this is a great example")
print("good" not in "this is a great example")

for x in range(6):
    print(x)
for x in range(2, 6):
    print(x)
for x in range(2, 30, 3):
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally Finished")

#Create a program
