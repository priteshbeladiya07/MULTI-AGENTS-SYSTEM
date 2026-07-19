from langchain.tools import tool
import requests
from langchain_mistralai import ChatMistralAI
from bs4 import BeautifulSoup
from tavily import TavilyClient
from dotenv import load_dotenv
load_dotenv()
import os
from rich import print

tavily = TavilyClient(api_key = os.getenv("TAVILY_API_KEY"))
#tool 1
@tool
def web_search(query:str)->str:
    """search the web for recent and reliable information on topic,Return title,urls and snippets."""
    results = tavily.search(query=query,max_results=5)
    out = []
    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL:{r['url']}\nSnippet : {r['content'][:300]}\n"
        )
    return "\n----\n".join(out)

#tool 2
@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
