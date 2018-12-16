#input validation
#Never underestimate the power of human stupidity

test = "Batman"

print(test.lower())

print(test.isalpha())

print(test[0])
print(test[1])
print(test[2])
print(test[3])
print(test[4])

print(test[1:4]) #Slice position 1 up to position 4

print(test[:3]) #Slice from end

print(test.lower()[3:len(test)])
