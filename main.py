import requests
import os

# Get the API key from the environment variable
API_KEY = os.environ.get('e544a9cda75646aab4ac34dab997c6ed')

# Get the news from the API
def get_news():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey=e544a9cda75646aab4ac34dab997c6ed'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# Print the news

def print_news():
    news = get_news()
    for article in news['articles']:
        print(article['title'])

if __name__ == '__main__':
    print_news()
    
