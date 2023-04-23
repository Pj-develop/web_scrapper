import csv
import requests

# set up API parameters
apiKey = '21f42fa0c768459c94b070bab81e3f0d'

# set up CSV file
csv_file = open('news_articles.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['article', 'label'])  # column headers

# loop through all the news articles for the year 2023
for month in range(1, 13):
    for day in range(1, 32):
        url = f'https://newsapi.org/v2/everything?&apiKey={apiKey}&from=2023-{month:02d}-{day:02d}&to=2023-{month:02d}-{day:02d}'
        response = requests.get(url)
        articles = response.json().get('articles', [])

        # write each article to CSV file with label "REAL"
        for article in articles:
            print([article['content'], 'REAL'])
            csv_writer.writerow([article['content'], 'REAL'])
            csv_file.flush()

# close CSV file
csv_file.close()
