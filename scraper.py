import requests
from bs4 import BeautifulSoup
import csv

# URL of the news website to scrape
url = "https://timesofindia.indiatimes.com/2023/1/1/archivelist/year-2023,month-1,starttime-44927.cms"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the news headlines on the website
headlines = soup.select(".w_tle")

# Create a CSV file to store the headlines and their labels
with open("news_headlines.csv", "a", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Iterate over the headlines and save them in the CSV file
    for headline in headlines:
        writer.writerow([headline.text.strip(), "REAL"])
