empty_tuple = ()

sisters = ('Jane', 'Mary', 'Kate')
brothers = ('John', 'Peter', 'Tom')
siblings = sisters + brothers
print(len(siblings))
family_members = siblings + ('Alice', 'Bob')
print(family_members)

# level 2
siblings, parents = family_members[:6], family_members[6:]
print(siblings)
print(parents)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('milk', 'meat', 'butter', 'yogurt')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_tp = list(food_stuff_tp)
print(food_stuff_tp[len(food_stuff_tp)//2])
print(food_stuff_tp[:3])
print(food_stuff_tp[-3:])


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
