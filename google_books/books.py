import requests 
import json

result = requests.get ("https://www.googleapis.com/books/v1/volumes?q=quilting")

print (result.status_code)
print (result.headers["content-Type"])

book = result.json()

print (book["totalItems"])

items = book["items"]

print (items[1].keys())

encoded = json.dumps(items)
decoded = json.loads(encoded)

print(decoded[1]["volumeInfo"]["title"]) 