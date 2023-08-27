import requests
from bs4 import BeautifulSoup
import pandas as pd

# https://uhunt.onlinejudge.org/api/uname2uid/dheeranazia
username="dheeranazia"
user_id = "1044787"
url = f"https://uhunt.onlinejudge.org/api/subs-user/{user_id}"
profile_url=f'https://uhunt.onlinejudge.org/id/{user_id}'

# Make a GET request to the user's profile page
response = requests.get(url)
# print(response.status_code)
# Check if the request was successful
if response.status_code != 200:
    print("Failed to fetch data from the UVA API")
    exit()


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Parse the response JSON
datum = response.json()['subs']

# print(datum)

empty_set = set()
       
for data in datum:
  if data[2]==90:
     empty_set.add(data[1])

uva=len(empty_set)
print(f"{username} has solved {uva} problems on UVA")
