import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Bot:
    def __init__(self, driver_path: str):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        start = self.driver.find_element(by=By.XPATH,
                                         value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start.click()
        
        time.sleep(20)
        up_info = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div'
                                                 '/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        up_info.click()

        time.sleep(20)

        down_info = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                                                   'div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        down_info.click()

        self.up = float(up_info.text)
        self.down = float(down_info.text)

        self.driver.quit()

        return [self.up, self.down]

    def tweet_provider(self, data: list, twitter_mail: str, password: str):
        up_data = data[0]
        down_data = data[1]
        message = f'@Telmex\n ' \
                  f'mi internet tiene {down_data}mbs de descarga y {up_data}mbs de subida, cuando pago por 100mbs.'

        self.driver.get('https://twitter.com/login')

        time.sleep(2)

        mail = self.driver.find_element(by=By.TAG_NAME,
                                        value='input')
        mail.send_keys(twitter_mail)

        time.sleep(2)

        next_button = self.driver.find_element(by=By.XPATH,
                                               value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]'
                                                     '/div/div/div[2]/div[2]/div[1]/div/div/div[6]')
        next_button.click()

        time.sleep(2)

        password_check = self.driver.find_elements(by=By.TAG_NAME,
                                                   value='input')
        password_check[-1].send_keys(password)

        log_in = self.driver.find_element(by=By.XPATH,
                                          value='//*[@id="layers"]/div/div/div/div/div/div/div[2]'
                                                '/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]')

        log_in.click()

        try:

            time.sleep(2)

            username_check = self.driver.find_element(by=By.TAG_NAME, value='input')
            username_check.clear()

            username_check.send_keys('lenny_touch')

            check_button = self.driver.find_element(by=By.XPATH,
                                                    value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]'
                                                          '/div/div/div[2]/div[2]/div[2]/div/div[1]')
            check_button.click()

            time.sleep(2)

            password_check = self.driver.find_elements(by=By.TAG_NAME,
                                                       value='input')
            password_check[-1].send_keys(password)

            log_in = self.driver.find_element(by=By.XPATH,
                                              value='//*[@id="layers"]/div/div/div/div/div/div/div[2]'
                                                    '/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]')

            log_in.click()

        except selenium.common.exceptions.InvalidArgumentException:
            pass

        time.sleep(5)

        tweet = self.driver.find_element(by=By.XPATH, value='//a[@data-testid="SideNav_NewTweet_Button"]')
        tweet.click()

        time.sleep(2)

        text = self.driver.find_element(by=By.XPATH, value='//div[@role="textbox"]')
        text.send_keys(message)

        send = self.driver.find_element(by=By.XPATH, value='//div[@data-testid="tweetButton"]')
        send.click()

        self.driver.quit()

    def quit_all(self):
        self.driver.quit()
