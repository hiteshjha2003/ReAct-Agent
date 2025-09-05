import requests
import os 
from dotenv import load_dotenv

load_dotenv()
SERP_API_KEY = os.getenv("SERP_API_KEY")


def search_google(query:str) -> str:
    url = "https://serpapi.com/search"
    params = {
        "q":query,
        "api_key":SERP_API_KEY,
        "num":10
    }
    response = requests.get(url , params=params)
    response.raise_for_status()
    results = response.json()

    snippets = []
    for result in results.get("organic_results",[]):
        title = result.get("title")
        link = result.get("link")
        snippet = result.get("snippet")
        snippets.append(f"{title}\n{snippet}\n{link}\n")
    return "\n----\n".join(snippets) if snippets else "No Results found"