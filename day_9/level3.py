person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    print(person['skills'][len(person['skills'])//2])

if 'skills' in person:
    if 'Python' in person['skills']:
        print('Ha python')


if len(person['skills']) == 2 and 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('He is a front end developer')

if person['is_marred'] == True:
    print('{} {} lives in {} and is married'.format(person['first_name'],person['last_name'],person['country']))