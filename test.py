import requests

# Taking the url of the api
url = "https://api.imgflip.com/get_memes"

# Getting the response from the api
response = requests.get(url)

# Taking the response and converting it into a JSON format
jsonated_response = response.json()

print(jsonated_response)

print("------------------------------")

for i in range(100):
    print(jsonated_response['data']['memes'][i]['url'])
