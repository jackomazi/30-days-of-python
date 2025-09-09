import re

# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = re.findall(r'\b\w+\b', paragraph, re.I)
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
print(word_freq)

#The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
regex_pattern = r'-?\d+'
points = re.findall(regex_pattern, text)
print(points)
sorted_points = sorted([int(point) for point in points])
distance = sorted_points[-1] - sorted_points[0]
print(distance)

# Write a pattern which identifies if a string is a valid python variable

def is_valid_variable(var):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    if re.match(pattern, var):
        return True
    return False

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

# Clean the following text. After cleaning, count three most frequent words in the string.
def most_frequent_words(text):
    words = re.findall(r'\b\w+\b', text, re.I)
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = re.sub(r'[%$@&#;!?]', '', sentence)
print(cleaned_text)
word_freq = most_frequent_words(cleaned_text)
print(word_freq)
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
print(sorted_word_freq[:3])
