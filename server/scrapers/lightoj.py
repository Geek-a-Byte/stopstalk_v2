import requests
from bs4 import BeautifulSoup
import pandas as pd

#username
loj_username = "geek-a-byte"
loj_url = f"https://lightoj.com/user/{loj_username}/"



# Make a GET request to the user's profile page
loj_response = requests.get(loj_url)


# Check if the request was successful
if loj_response.status_code != 200:
    print("Failed to fetch data from the CSES API")
    exit()

# Parse the HTML content using BeautifulSoup
loj_soup = BeautifulSoup(loj_response.content, "html.parser")


# loj
span1, span2 = loj_soup.find("div", {"class": "like-count mr-4"}).find_all('span')

# Check if the span element was found
if span1 is not None:
    # Extract the number of solved problems from the div text
    loj = span1.text.strip()
    print(f"{loj_username} has solved {loj} problems on LightOJ")
else:
    print("Could not find the number of solved problems on the user's profile page")