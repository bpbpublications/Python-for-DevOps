# Script: 028_scrape_website.py

# Importing the necessary modules for web scraping
import requests
from bs4 import BeautifulSoup

# Sending a GET request to the website to retrieve its content
response = requests.get('https://example.com')

# Parsing the HTML content of the response using BeautifulSoup and 'lxml' parser
# You can also use 'html.parser' if lxml is not available
soup = BeautifulSoup(response.content, 'lxml')  # or 'html.parser'

# Finding all h1 tags on the page
titles = soup.find_all('h1')  # Finds all h1 tags

# Iterating through the found h1 tags and printing their text content
for title in titles:
    print(title.text)  # Prints the text in each h1 tag

# Finding all div tags with the class 'article'
articles = soup.find_all('div', class_='article')  # Finds all divs with class 'article'

# Optionally, save the extracted data to a file or database
# Saving data to a text file (you can adapt it for a database)
with open('scraped_articles.txt', 'w') as file:
    for article in articles:
        file.write(article.text.strip() + '\n')

print("Data saved to scraped_articles.txt")
