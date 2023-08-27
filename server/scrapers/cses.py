import requests
from bs4 import BeautifulSoup
import pandas as pd

cses_username = "77547"
cses_url = f"https://cses.fi/user/{cses_username}/"
# Make a GET request to the user's profile page
cses_response = requests.get(cses_url)
# Check if the request was successful
if cses_response.status_code != 200:
    print("Failed to fetch data from the CSES API")
    exit()
    
# Parse the HTML content using BeautifulSoup
cses_soup = BeautifulSoup(cses_response.content, "html.parser")
# init so that if a user doesn't solve any problem it shows 0
cses = 0

# cses
table = cses_soup.find_all('table')
df1 = pd.read_html(str(table))[1]
df2 = pd.read_html(str(table))[2]
# print(df1)
# print(df2)

df = pd.DataFrame(df1)
cses = df.iloc[0]['solved tasks']
print(f"{cses_username} has solved {cses} problems on cses")
