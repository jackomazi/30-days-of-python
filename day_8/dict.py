dog = dict()
dog = {
    'name': 'Bosco',
    'color': 'brown',
    'breed': 'Labrador',
    'legs': 4,
    'age': 5
}

student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript', 'HTML'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

print(len(student))

print(type(student['skills']))
student['skills'].append('CSS')
print(student.keys())

print(student.values())

print(student.items())

del student['marital_status']

del student