import pandas
import requests
from bs4 import BeautifulSoup

ANSWERS_CSV = 'answers.csv'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


def get_html(url):
    response = requests.get(url, headers=HEADERS)
    return response


def get_scores(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('td', class_='resScaleVal')
    scores = []
    for item in items:
        scores.append(item.text)
    return scores


dataframe = pandas.read_csv(ANSWERS_CSV, delimiter=',')
answer_urls = dataframe.values[:, 2]

dataframe['O'] = -1
dataframe['C'] = -1
dataframe['E'] = -1
dataframe['A'] = -1
dataframe['N'] = -1
for i in range(len(answer_urls)):
    html = get_html(answer_urls[i])
    scores = get_scores(html.text)
    dataframe['O'][i] = scores[4]
    dataframe['C'][i] = scores[2]
    dataframe['E'][i] = scores[0]
    dataframe['A'][i] = scores[1]
    dataframe['N'][i] = scores[3]

dataframe.to_csv(ANSWERS_CSV, index=False)
