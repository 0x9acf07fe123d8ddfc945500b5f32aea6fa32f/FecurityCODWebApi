import requests
from bs4 import BeautifulSoup

def get_guide(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    else:
        return "Error: Unable to fetch the guide."

urls = [
    "https://fecurity.cloud/guide/",  # System Requirements
    "https://www.fecurity.cloud/guide/launch.html",  # Preparing for Launch
    "https://fecurity.cloud/guide/launch.html",  # Launch
    "https://fecurity.cloud/guide/params.html",  # Launch Options
    "https://fecurity.cloud/guide/codspoofer.html"  # How to Spoof COD
]

for url in urls:
    print(get_guide(url))
    print("\n" + "="*80 + "\n") 
