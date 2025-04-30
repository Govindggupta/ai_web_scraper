import aiohttp
from bs4 import BeautifulSoup
import asyncio
import nest_asyncio

# Apply nest_asyncio to handle asyncio run issues in Python 3.12 (Windows)
nest_asyncio.apply()

async def scrape_website(website):
    print("Starting website scraping...")
    
    try:
        # Set a user agent to identify our requests
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(website) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    return soup.prettify()
                else:
                    print(f"Error: Received status code {response.status}")
                    return None
    
    except Exception as e:
        print(f"Error: {e}")
        return None
    
if __name__ == "__main__":
    asyncio.run(scrape_website("https://x.com/3g_g0vind"))