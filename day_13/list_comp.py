numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

neg = [num for num in numbers if num<=0]
print(neg)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flatten = [num for rows in list_of_lists for row in rows for num in row]
print(flatten)