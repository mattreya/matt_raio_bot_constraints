
import asyncio
from slash_commands import run_duckduckgo

def search_dark_reading(query):
    """
    Searches for articles from darkreading.com using the ddg command.
    """
    return asyncio.run(run_duckduckgo(f"site:darkreading.com {query}"))

if __name__ == "__main__":
    articles = search_dark_reading("latest news")
    print(articles)
