from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/lenny/development/chromedriver"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get('https://www.python.org/')

menu = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

dates = menu.find_elements(by=By.TAG_NAME, value='time')
titles = menu.find_elements(by=By.TAG_NAME, value='a')

dates_data = [date.text for date in dates]
titles_data = [title.text for title in titles]

schedule = {}

for n in range(len(titles_data)):
    schedule[n] = {
        'time': dates_data[n],
        'event': titles_data[n]
    }

print(schedule)

driver.close()
