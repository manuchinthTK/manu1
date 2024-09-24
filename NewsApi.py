import requests
import os
from dotenv import load_dotenv
load_dotenv()

password = os.getenv('PASS1')

def get_weather():
    url = f"https://newsdata.io/api/1/latest?apikey={password}&q=pizza"
    request = requests.get(url)
    content = request.json()
    print(content)

get_weather()