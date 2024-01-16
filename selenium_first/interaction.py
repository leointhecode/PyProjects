import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/lenny/development/chromedriver"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

start_time = time.time()
seconds = 120


cookie = driver.find_element(by=By.ID, value='cookie')
store = driver.find_element(by=By.ID, value='store')
money = driver.find_element(by=By.ID, value='money')


def upgrade():
    products = store.find_elements(by=By.TAG_NAME, value='div')
    cost = 0

    for n in products[:-1][::-1]:

        try:
            for i in n.text.split():

                cost = int(i.replace(",", ""))
        except ValueError:
            pass
        except selenium.common.exceptions.StaleElementReferenceException:
            driver.implicitly_wait(10)

        try:
            if int(money.text.replace(",", "")) > cost + 1000:
                n.click()

        except selenium.common.exceptions.StaleElementReferenceException:
            driver.implicitly_wait(10)


while True:
    cookie.click()

    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time > seconds:
        upgrade()
