import requests
from bs4 import BeautifulSoup


class ExtractData:
    def __init__(self, url: str):
        self.response = requests.get(url=url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

    def get_data(self):
        names = self.soup.find_all(name='div', class_='entry-title')
        data1 = [name.getText().replace('  ', '').replace('\t', '').replace('\n', '') for name in names]

        links = self.soup.find_all(name='a', class_='entry-vote')
        data2 = [link['href'] for link in links]

        tops = self.soup.find_all(name='div', class_='arrow-number')
        data3 = [variable.getText().replace('  ', '').replace('\t', '').replace('\n', '') for variable in tops]

        data = []
        for _ in range(len(names)):
            data.append([data1[_], data2[_], data3[_]])

        return data
