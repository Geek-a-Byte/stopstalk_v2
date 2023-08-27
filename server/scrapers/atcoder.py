# import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests

username = "geekabyte"
profile_url=f'https://atcoder.jp/users/{username}'
url = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user_info?user={username}"

# Make a GET request to the user's profile page
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to fetch data from the Atcoder API")
    exit()

number=0
# Parse the response JSON
datum = response.json()['accepted_count']
if(datum>0):
  number=datum
print(f"{username} has solved {number} problems on Atcoder")
