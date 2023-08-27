import requests
from bs4 import BeautifulSoup
import pandas as pd

username = "geekabyte"
url = f"https://toph.co/u/{username}/"

# Make a GET request to the user's profile page
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to fetch data from the TOPH API")
    exit()


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# print(soup)
div1, div2, div3 = soup.find("div", {"class": "numbers"}).find_all('div',{'class':'value'})



# Check if the div element was found
toph=0
if div2 is not None:
    # Extract the number of solved problems from the div text
    toph = div2.text.strip()
    print(f"{username} has solved {toph} problems on Toph")
else:
    print("Could not find the number of solved problems on the user's profile page")
