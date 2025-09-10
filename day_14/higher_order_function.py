from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def upper_case(txt):
    return txt.upper()
def square(num):
    return num ** 2

upper_countries = map(upper_case, countries)
print(list(upper_countries))

squared_nums = map(square, numbers)
print(list(squared_nums))

names = map(upper_case, names)
print(list(names))

# Use filter to filter out countries containing 'land'.
def contain_land(txt):
    if 'land' in txt:
        return False
    return True

filtered_countries = filter(contain_land, countries)
print(list(countries))
print(list(filtered_countries))

# Use filter to filter out countries having exactly six characters.
def six_chars(txt):
    if len(txt) == 6:
        return False
    return True
filtered_countries = filter(six_chars, countries)
print(list(countries))
print(list(filtered_countries))

# Use filter to filter out countries containing six letters and more in the country list.
def six_chars_or_more(txt):
    if len(txt) >= 6:
        return False
    return True
filtered_countries = filter(six_chars_or_more, countries)
print(list(countries))
print(list(filtered_countries))

# Use filter to filter out countries starting with an 'E'
def starts_with_e(txt):
    if txt.startswith('E'):
        return False
    return True
filtered_countries = filter(starts_with_e, countries)
print(list(countries))
print(list(filtered_countries))

# Use reduce to sum all the numbers in the numbers list.
def add(x, y):
    return x + y

sum = reduce(add, numbers)

print(sum)

# Use reduce to concatenate all the countries and to produce this sentence: 
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def add_strings(x, y):
    return x + ', ' + y

sentence = reduce(add_strings, countries)
sentence += ' are north European countries'
print(sentence)

# Declare a function called categorize_countries that returns a list of countries 
# with some common pattern (you can find the countries list in this repository as 
# countries.js(eg 'land', 'ia', 'island', 'stan')).
import countries as C
def categorize_countries(txt, pattern):
    if pattern in txt:
        return True
    return False
pattern = "stan"
countrie_pattern = filter(lambda country: categorize_countries(country, pattern), C.countries)
print(list(countrie_pattern))

# Create a function returning a dictionary, where keys stand for starting letters of countries 
# and values are the number of country names starting with that letter.

def start_with_letter(txt, first_letter):
    if txt.startswith(first_letter):
        return True
    return False

def create_dict(countries_list):
    letters_countries = {}
    for country in countries_list:
        letter = country[0]
        if letter not in letters_countries:
            countries_grouped = filter(lambda country: start_with_letter(country, letter), countries_list)
            letters_countries[letter] = len(list(countries_grouped))
    return letters_countries

letters_countries = create_dict(C.countries)
print(letters_countries)

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

