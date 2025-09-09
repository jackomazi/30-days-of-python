empty_list = []
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(list))

print(list[0], list[len(list)//2], list[-1]) # primo, medio, ultimo

mixed_data_types = [ 'Andrea', 23, 1.84]
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

print(len(it_companies))

print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1]) # primo, medio, ultimo

it_companies[0] = 'Meta'
it_companies.insert(len(it_companies)//2, 'Tesla')

print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)
joined = '#; '.join(it_companies)
print(joined)


print('Microsoft' in it_companies)

it_companies.sort()

it_companies.reverse()

print(it_companies[0:3]) # primi 3
print(it_companies[-3:]) # ultimi 3

print(it_companies[len(it_companies)//2])

it_companies.pop(0) # rimuovi primo
it_companies.pop(len(it_companies)//2) # rimuovi medio
it_companies.pop() # rimuovi ultimo
print(it_companies)
it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')



# EXERCISE level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
print(f"Min age: {min_age}, Max age: {max_age}")
median_age = (ages[len(ages)//2] + ages[(len(ages)-1)//2]) / 2
print(f"Median age: {median_age}")
average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")
range_of_ages = max_age - min_age
print(f"Range of ages: {range_of_ages}")
print(abs(min_age - average_age) , abs(max_age - average_age))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

print(countries[len(countries)//2])
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
if len(countries) % 2 == 0:
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else:
    first_half = countries[:len(countries)//2 + 1]
    second_half = countries[len(countries)//2 + 1:]

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = countries
print(ch, ru, us, scandic)

