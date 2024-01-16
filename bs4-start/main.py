from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.rottentomatoes.com/top/bestofrt/")
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all(name='a', class_='unstyled articleLink')

names = [name.getText().replace('\n', '').replace("  ", '') for name in titles][43:-2]

indexed_names = [[names.index(name) + 1, name] for name in names]

final_list = [f"{str(name[0])}. {name[1]}" for name in indexed_names]

with open('movies.text', 'w') as file:
    for name in final_list:
        file.write(f"{name}\n")
