import requests
import re
from bs4 import BeautifulSoup

# Set the username
judge_id = '314812BQ'

# Extract the numeric part using regular expressions
numeric_part_list = re.findall('\d+', judge_id)

# Convert the list of numeric digits to a string
id = ''.join(numeric_part_list)

# Print the numeric part as a string
# print(id)

# Make the API request
url = f'https://timus.online/author.aspx?id={id}'
# print(url)
response = requests.get(url)

# Parse the response
soup = BeautifulSoup(response.content, 'html.parser')

t1,t2,t3,t4 = soup.find_all('td', {'class': 'author_stats_value'})
number=0
if t2 is not None:
    # Extract the number of solved problems from the div text
    solved_count = t2.text.strip()
    # Extract the first number using regular expressions
    number = re.findall(r'\d+', solved_count)[0]
    print(f"{id} has solved {number} problems on Timus")
else:
    print("Could not find the number of solved problems on the user's profile page")
