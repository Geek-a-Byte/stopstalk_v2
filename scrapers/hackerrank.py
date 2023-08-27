import requests
from bs4 import BeautifulSoup as bs
import lxml
import json

from dotenv import load_dotenv
import os

load_dotenv()

# Build the login payload
payload = {
'username': 'geek_a_byte32', #<-- your username
'remember':'1' 
}

#header string picked from chrome
headerString='''
{
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}
'''
d = json.loads(headerString)


url2=f"https://www.hackerrank.com/rest/hackers/{payload['username']}/badges"


# Try to get a page behind the login page
s = requests.Session()
r = s.get(url2, headers=d)


# # Check if login was successful, if so there have to be an element with the id menu_row2
soup = bs(r.text, 'lxml')

# Parse the response JSON
datum = r.json()['models']

total_count=0;
# Print the parsed data
for data in datum:
    # print(data['badge_name'],end=' ')
    # print(data['solved'])
    total_count+=data['solved']
print(f"{payload['username']} has solved {total_count} problems on Hackerrank")

