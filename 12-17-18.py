#Lists
item1 = ""
item2 = ""
item3 = ""

list_name = [item1, item2, item3]

print(list_name)

if len(list_name) < 1:
    print("Empty List!")
else:
    print("Non-empty list.")

item1 = input("Item 1: ")
item2 = input("Item 2: ")
item3 = input("Item 3: ")

list_name = [item1, item2, item3]

print(list_name)

if len(list_name) < 1:
    print("Empty List!")
else:
    print("Non-empty list.")

'''
print(list_name[0])
print(list_name[1])
print(list_name[2])

new_list = [5, "Superman", True]
print(new_list[0] + new_list[2])

new_list[2] = 100

print(new_list[0] + new_list[2])

#Append

letters = ['a', 'b', 'c']
letters.append('d')
print(len(letters))
print(letters)

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

print(suitcase[0:2])
print(suitcase[2:4])
print(suitcase[4:6])

print(suitcase[:2])
print(suitcase[2:])


suitcase_index = suitcase.index("passport")
suitcase.insert(suitcase_index, "Video Games")
print(suitcase)

start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
    square_list.append(number ** 2)

square_list.sort()

print(square_list)
'''
