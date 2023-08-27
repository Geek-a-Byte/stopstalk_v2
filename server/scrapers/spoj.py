import requests
from bs4 import BeautifulSoup

# Set the username
username = 'dheeranazia'

# Make the API request
url = f'https://www.spoj.com/users/{username}/'
response = requests.get(url)

# Parse the response
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('div', {'class': 'col-md-6 text-center valign-center'})
dd1, dd2 = table.find_all('dd')
# print(dd1)

spoj=0
if dd1 is not None:
    # Extract the number of solved problems from the div text
    spoj = dd1.text.strip()
    print(f"{username} has solved {spoj} problems on Spoj")
else:
    print("Could not find the number of solved problems on the user's profile page")