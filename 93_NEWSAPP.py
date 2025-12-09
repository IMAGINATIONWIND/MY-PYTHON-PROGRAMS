import requests
import time

api_key = "pub_33812c10eb5445278565e6cb1c77be80"

def querys():
    print("query selection")
    time.sleep(1)
    print('''                           ''')
    a = ["politics",
         "business",
         "technology",
         "sports",
         "entertainment",
         "crime",
         "health"]
    print("press 0 for politics, 1 for business, 2 for technology, 3 for sports, 4 for entertainment, 5 for crime, and 6 for health. \n")
    time.sleep(5)
    b = int(input("-->"))
    return a[b]
query = querys()
print("-----------------QUERY SELECTED SUCCESSFILLY-----------------")

def langs():
    print("language selection")
    time.sleep(1)
    print('''                           ''')
    a =[    
    "en",
    "hi",
    "es",
    "fr",
    "de",
    "ja",
    "ko"
        ]
    print("Press 0 for English, 1 for Hindi, 2 for Spanish, 3 for French, 4 for German, 5 for Japanese, and 6 for Korean. \n")
    time.sleep(5)
    b = int(input("-->"))
    return a[b]
language = langs()
print("-----------------LANGUAGE SELECTED SUCCESSFILLY-----------------")

url = f"https://newsdata.io/api/1/latest?apikey={api_key}&q={query}&language={language}"

response = requests.get(url)
data = response.json()

for item in data["results"]:
   print(item["title"])
   print(item['description'])
   print(item['creator'])
   print(item["language"])
   print(item['category'])
   print(item['pubDate'])
   print(item['source_name'])
   print("\n","-" * 50)