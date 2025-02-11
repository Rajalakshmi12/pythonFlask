# Content Curation for StreamFlix Streaming - created by '23ds3000149@ds.study.iitm.ac.in'

# id, title, year, rating --> into a json format, rating between 2 and 7
import requests
import json
from bs4 import BeautifulSoup
import re

# API call to get the response from the site
min_rating = 2
max_rating = 7
url = f"https://www.imdb.com/search/title/?user_rating={min_rating},{max_rating}"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)


if response.status_code == 200:
    final_summary = []

    data = response.content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the div 'ipc-metadata-list-summary-item'
        # Loop through to find div of [a] with class 'ipc-lockup-overlay ipc-focusable'
        # Loop through to find h3 with 'ipc-title__text' --> TITLE
        # Loop through to find span with class 'sc-d5ea4b9d-7 URyjV dli-title-metadata-item' --> YEAR
        # Loop through to find span with class 'ipc-rating-star--rating' --> RATING
        
    movies = soup.find_all('div', attrs = {'class':'ipc-metadata-list-summary-item__c'})
    
    for movie in movies:
        movie_summary = {}
                
        # ID
        id_href = movie.find('a', attrs={'class':'ipc-lockup-overlay ipc-focusable'}).get('href')
        match = re.search(r"tt(\d+)", id_href)
        movie_summary["id"] = 'tt'+match.group(1)
        
        # TITLE
        title = movie.find('h3', attrs={'class': 'ipc-title__text'}).get_text(strip=True)
        _, _, m_title = title.partition(" ")  # Splits at the first space, partition is useful
        encoded_title = title.encode('utf-8').decode('utf-8')
        movie_summary["title"] = encoded_title
        print(title)

        # YEAR
        year = movie.find('span', attrs={'class': 'sc-d5ea4b9d-7 URyjV dli-title-metadata-item'}).get_text(strip=True)
        movie_summary["year"] = year # Get only first 4 digits
        
        
        # RATING
        rating = movie.find('span', attrs = {'class':'ipc-rating-star--rating'}).get_text(strip=True)
        movie_summary["rating"] = rating

        # Final array that stores all the objects  
        final_summary.append(movie_summary)
    print(json.dumps(final_summary, indent=2, ensure_ascii=False)) # Important to get rid of decoded characters

        #print(f"Title: {title}, Rating: {rating}, Link: {link}")
    

    # [
        #{ "id": "tt1234567", "title": "Movie 1", "year": "2021", "rating": "5.8" },
        #{ "id": "tt7654321", "title": "Movie 2", "year": "2019", "rating": "6.2" }
    # ]