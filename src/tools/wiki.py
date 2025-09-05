import requests

def search_wikipedia(query:str) -> str:
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
    response = requests.get(url)

    if response.status_code == 404:
        return "No Article found"
    
    data = response.json()
    return f"{data.get('title')}\n\n{data.get('extract')}"
