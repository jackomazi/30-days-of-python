import requests

# url = 'http://www.gutenberg.org/files/1112/1112.txt'


url = 'https://api.thecatapi.com/v1/breeds'
#Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# -the min, max, mean, median, standard deviation of cats' weight in metric units.
# -the min, max, mean, median, standard deviation of cats' lifespan in years.
# -Create a frequency table of country and breed of cats

response = requests.get(url)  # opening a network and fetching a data
# print(response) # response object
# print(response.status_code)  # status code, success:200
cats = response.json()
#print(countries[:1])

weights = []

for cat in cats:
    weight = cat['weight']['metric']
    weights.append(weight)
print(weights)
max_weight = 0
min_weight = 1000
mean_weight = 0
std_weight = 0
for weight in weights:
    weight_range = weight.split(' - ')
    max_w = int(weight_range[1])
    min_w = int(weight_range[0])
    if max_w > max_weight:
        max_weight = max_w
    if min_w < min_weight:
        min_weight = min_w
    mean_weight += (max_w + min_w) / 2
    



mean_weight = mean_weight / len(weights)

print('Min weight:', min_weight)
print('Max weight:', max_weight)
print('Mean weight:', mean_weight)


