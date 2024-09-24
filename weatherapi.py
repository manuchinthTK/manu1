import requests
import os
from dotenv import load_dotenv
load_dotenv()

password = os.getenv('PASS2')

def get_weather(city,  units):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={password}&units={units}"
    request = requests.get(url)
    content = request.json()
    print(content)

get_weather("Kannur", "standard")
