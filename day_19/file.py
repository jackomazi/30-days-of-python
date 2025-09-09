import os
import json
# Write a function which count number of lines and number of words in a text.
def count_lines_and_words(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
    return num_lines, num_words


n, w = count_lines_and_words('./day_19/obama_speech.txt')
print(f'Number of lines: {n}, Number of words: {w}')
n, w = count_lines_and_words('./day_19/michelle_obama_speech.txt')
print(f'Number of lines: {n}, Number of words: {w}')
n, w = count_lines_and_words('./day_19/donald_speech.txt')
print(f'Number of lines: {n}, Number of words: {w}')
n, w = count_lines_and_words('./day_19/melina_trump_speech.txt')
print(f'Number of lines: {n}, Number of words: {w}')

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_languages(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)
    language_count = {}
    for country in countries:
        for languages in country.get("languages"):
            language_count[languages] = language_count.get(languages, 0) + 1
    language_count = sorted(language_count.items(), key=lambda item: item[1], reverse=True)[:n]
    
    return [(count, language) for language, count in language_count]

language_count = most_spoken_languages(filename='./day_19/countries_data.json', n=10)
print(language_count)

# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        countries = json.load(f)
    population_count = {}
    for country in countries:
        population_count[country.get("name")] = country.get("population")
    population_count = sorted(population_count.items(), key=lambda item: item[1], reverse=True)[:n]
    return population_count

print(most_populated_countries(filename='./day_19/countries_data.json', n=3))

# Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
def find_most_frequent_words(file_path, n):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        word_count = {}
        for word in words:
            word = word.strip('.,!?;"()[]{}')  # Remove punctuation
            word_count[word] = word_count.get(word, 0) + 1
        most_frequent = sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:n]
    return most_frequent

print(find_most_frequent_words('./day_19/obama_speech.txt', 10))
print(find_most_frequent_words('./day_19/michelle_obama_speech.txt', 10))
print(find_most_frequent_words('./day_19/donald_speech.txt', 10))
print(find_most_frequent_words('./day_19/melina_trump_speech.txt', 10))

