import time
from random import random

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Bot:
    def __init__(self, driver_path: str):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self, ig_mail: str, ig_password: str):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        mail = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        mail.send_keys(ig_mail)

        time.sleep(2)
        password = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(ig_password)

        time.sleep(2)

        login = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        time.sleep(5)

    def find_followers(self, account: str):
        search = self.driver.find_element(by=By.XPATH,
                                          value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(account)

        time.sleep(2)

        results = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="react-root"]/section/nav/div[2]/'
                                                 'div/div/div[2]/div[3]/div/div[2]/div/div/a')
        results.click()
        time.sleep(2)

        followers = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)

        modal = self.driver.find_element(by=By.XPATH, value='//div[@Class="isgrP"]')
        for i in range(100):
            self.follow()
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        targets = self.driver.find_elements(by=By.TAG_NAME, value='button')

        for target in targets:
            time.sleep(1)
            if target.text == 'Follow':
                self.driver.execute_script("arguments[0].click();", target)
            else:
                pass
