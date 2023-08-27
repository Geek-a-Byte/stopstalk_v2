import sys
import requests
import re
from bs4 import BeautifulSoup as BS


username='dheeranazia'
url = 'https://www.codechef.com/users/' + username
page = requests.get(url)
soap = BS(page.text , 'html.parser')

ratings = soap.find_all('section', class_ = 'rating-data-section problems-solved')

rat = ratings[0]
h51,h52=rat.find_all('h5')
# print(h51)

number=0
if h51 is not None:
    # Extract the number of solved problems from the div text
    solved_count = h51.text.strip()
    # Extract the first number using regular expressions
    number = re.findall(r'\d+', solved_count)[0]
    print(f"{username} has solved {number} problems on CC")
else:
    print("Could not find the number of solved problems on the user's profile page")

