import os 
import requests
import json 
import dotenv
import socket 

dotenv.load_dotenv() 

api_key = os.environ.get('API_KEY')
# query   = input("Enter a pokemon name\n")
query = 'blastoise'
limit = 1
offset = 0
rating = 'G'

url = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={query}&limit={int(limit)}&offset={int(offset)}&rating={rating.upper()}&lang=en"

response = requests.get(url)
data = response.json() 


img_url = data['data'][0]['images']['fixed_height']['url']


print(img_url)