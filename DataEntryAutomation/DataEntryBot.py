import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class DataBot:
    def __init__(self, driver_path: str):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def submit_to_form(self, form: str, data: list):
        while True:
            for n in range(len(data)):

                self.driver.get(form)
                time.sleep(1)

                question1 = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]'
                                                                        '/div/div/div[2]/div/div[1]/div/div[1]/input')
                question1.clear()
                question1.send_keys(data[n][0])
                time.sleep(1)

                question2 = self.driver.find_element(by=By.XPATH,
                                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]'
                                                           '/div/div/div[2]/div/div[1]/div/div[1]/input')
                question2.clear()
                question2.send_keys(data[n][1])
                time.sleep(1)

                question3 = self.driver.find_element(by=By.XPATH,
                                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]'
                                                           '/div/div/div[2]/div/div[1]/div/div[1]/input')
                question3.clear()
                question3.send_keys(data[n][2])
                time.sleep(1)

                send = self.driver.find_element(by=By.XPATH,
                                                value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
                send.click()

                if n == range(len(data)):
                    break
                else:
                    time.sleep(1)
                    not_stop = self.driver.find_element(by=By.XPATH,
                                                        value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
                    not_stop.click()
