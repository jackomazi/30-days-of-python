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


print("="*50)

# Extract all incoming email addresses as a list from the email_exchange_big.txt file.

with open('./day_19/email_exchanges_big.txt') as f:
    lines = f.read().splitlines()
    email_addresses = []
    for line in lines:
        # check if line starts with 'From: '
        if line.startswith('From: '):
            print(line.split(' '))
            email = line.split(' ')[1]
            email_addresses.append(email)

    #print(email_addresses)
print("="*50)

# Write a python application that checks similarity between two texts. 
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
# For instance check the similarity between the transcripts of Michelle's and Melina's speech. 
# You may need a couple of functions, 
# function to clean the text(clean_text), 
# function to remove support words(remove_support_words) and 
# finally to check the similarity(check_text_similarity). 
# List of stop words are in the data directory

import stop_words
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text) # rimuove caratteri che non sono lettere o spazi [^] è la negazione
    return text

def remove_stop_words(text):
    # stop words are in a python file stop_words.py
    stop_words_list = stop_words.stop_words
    words = text.split()
    words = [word for word in words if word not in stop_words_list]
    return ' '.join(words)

def similarity(file1, file2):
    with open(file1, 'r') as f:
        file1 = f.read(50)
        
    with open(file2,'r') as f:
        file2 = f.read(50)
    file1 = clean_text(file1)
    file2 = clean_text(file2)
    file1 = remove_stop_words(file1)
    file2 = remove_stop_words(file2)
    docs = [file1, file2]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(docs)

    sim = cosine_similarity(tfidf[0], tfidf[1])
    
    return sim[0][0]


# print(similarity('./day_19/michelle_obama_speech.txt','./day_19/melina_trump_speech.txt'))

print("="*50)

# Find the 10 most repeated words in the romeo_and_juliet.txt
print(find_most_frequent_words('./day_19/romeo_and_juliet.txt',10))

print("="*50)

# Read the hacker news csv file and find out: 
# a) Count the number of lines containing python or Python 
# b) Count the number lines containing JavaScript, javascript or Javascript 
# c) Count the number lines containing Java and not JavaScript
import csv
with open('./day_19/hacker_news.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    python_count = 0
    js_count = 0
    java_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if re.search('python|Python', " ".join(row)) != None:
                python_count += 1
            if re.search('JavaScript|javascript|Javascript', " ".join(row)) != None:
                js_count += 1
            if re.search('Java', " ".join(row)) != None and re.search('Javascript', " ".join(row)) == None:
                java_count += 1
            line_count += 1

    print(f'Number of lines:  {line_count}')
    print(f"Number of python/Python lines: {python_count}")
    print(f"Number of JavaScript/javascript/Javascript lines: {js_count}")
    print(f"Number of Java and not Javascript lines: {java_count}")