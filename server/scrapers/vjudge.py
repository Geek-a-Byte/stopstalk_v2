import requests

username_1 = "dheeranazia"
username_2="geek_a_byte"

url_1 = f"https://vjudge.net/user/solveDetail/{username_1}"
url_2 = f"https://vjudge.net/user/solveDetail/{username_2}"

# Make a GET request to the user's profile page
response1 = requests.get(url_1)
response2 = requests.get(url_2)

# Check if the request was successful
if response1.status_code != 200:
    print("Failed to fetch data from the Vjudge API")
    exit()
if response2.status_code != 200:
    print("Failed to fetch data from the Vjudge API")
    exit()

number1=0
number2=0
# Parse the response JSON
datum = response1.json()['acRecords']
datum2= response2.json()['acRecords']


keysList1 = [x for x in list(datum.keys()) ]
keysList2 = [x for x in list(datum2.keys()) ]


oj = ['SPOJ', 'UVA', 'CodeForces',  'Aizu', 'LightOJ', 'CodeChef', 'AtCoder', 'HackerRank', 'CSES','Toph', 'Gym']

for item in keysList1: 
  if item not in oj:
    #  print(item)
     number1+=len(datum[item])

for item in keysList2: 
  if item not in oj:
    #  print(item)
     number2+=len(datum2[item])

