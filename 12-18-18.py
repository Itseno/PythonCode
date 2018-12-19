#Dictionaries

population = { 'St. Louis': 308294, 'Ted': 105}

print(population['Ted'])
print(population['St. Louis'])

menu = {}

menu['Chicken Alfredo'] = 14.50


zoo_animals = {'Unicorn':'Candy House', 'Sloth':'Rainforest'}

del zoo_animals['Unicorn']
zoo_animals['Sloth'] = 'Panther'


for x in zoo_animals:
    print (x) #X is key not value

for x in zoo_animals:
    print(zoo_animals[x])

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone']
}

inventory['pouch'].remove('gemstone')

print(inventory)

input = open('13 - Alice.txt').read()


counts = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
