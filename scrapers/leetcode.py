
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

#username
lc_user = "nazia32"
api_endpoint = f"https://leetcode.com/graphql"

def extract_json(dict):
  user=dict['user']
  opName=dict['opName']
  Query=dict['Query']
  data={
  "operationName": opName,
  "variables": {"username":user},
  "query": Query
  }
  header={
      "Referer":f"https://leetcode.com/{user}",
      'Content-type':'application/json'
  
  }
  s=requests.session()
  s.get("https://leetcode.com/")
  header["x-csrftoken"] = s.cookies["csrftoken"]
  r = s.post("https://leetcode.com/graphql",json=data,headers=header)
  return json.loads(r.text)

query = '''
query skillStats($username: String!) {
    matchedUser(username: $username) {
    submitStats {
      acSubmissionNum {
        difficulty
        count
      }
    }
      tagProblemCounts {
        advanced {
          tagName
          problemsSolved
        }
        intermediate {
          tagName
          problemsSolved
        }
        fundamental {
          tagName
          problemsSolved
        }
      }
    }
  }
'''
json_data1=extract_json({"user":lc_user,"opName":"skillStats","Query":query})

try:
  df_data1 = json_data1['data']['matchedUser']['tagProblemCounts']['intermediate']
  df_data2=json_data1['data']['matchedUser']['tagProblemCounts']['fundamental']
  df_data3=json_data1['data']['matchedUser']['tagProblemCounts']['advanced']
  df_data4=json_data1['data']['matchedUser']['submitStats']['acSubmissionNum']
  df_intermediate= pd.DataFrame(df_data1)
  df_fundamental= pd.DataFrame(df_data2)
  df_advanced= pd.DataFrame(df_data3)
  df_total = pd.DataFrame(df_data4)
  leetcode = df_total.iloc[0]['count']
  print(f"{lc_user} has solved {leetcode} problems on Leetcode")
except:
  print("The user does not exist!")