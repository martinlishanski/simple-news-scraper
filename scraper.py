import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Целеви сайт (в случая BBC News, тъй като е стандарт за примери)
URL = "https://www.bbc.com/news"

def scrape_headlines():
    print(f"Fetching headlines from {URL}...")
    
    try:
        response = requests.get(URL)
        # Проверяваме дали заявката е успешна
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Намираме заглавията (H2 елементи обикновено съдържат новините)
        headlines = soup.find_all('h2')
        
        saved_data = []
        for item in headlines:
            title = item.get_text(strip=True)
            if title:
                saved_data.append([title, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

        # Записваме резултатите в CSV файл
        with open('headlines.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Headline", "Timestamp"])
            writer.writerows(saved_data)
            
        print(f"Successfully saved {len(saved_data)} headlines to headlines.csv")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_headlines()
