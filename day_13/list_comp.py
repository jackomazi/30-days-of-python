numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

neg = [num for num in numbers if num<=0]
print(neg)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flatten = [num for rows in list_of_lists for row in rows for num in row]
print(flatten)


powers = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(0, 11)]
print(powers)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]


print([[i[0].upper(),i[0][0:3].upper(), i[1].upper()] for country in countries for i in country])

# to dictionary
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([{'country': i[0], 'city': i[1]} for country in countries for i in country])

# to concat
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print([i[0] + ' ' + i[1] for name in names for i in name])

# Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else 'undefined'
y_intercept = lambda m, x, y: y - m * x
print(slope(1, 2, 3, 4))  # Output: 1.0
print(y_intercept(1, 2, 3))  # Output: 1