import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

mail = "touchmelenny@gmail.com"
password = 'Inu-noTaisho5@3$'

chrome_driver_path = "/home/lenny/development/chromedriver"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get('https://tinder.com/app/recs')

time.sleep(1)

try:
    log_in = driver.find_element(by=By.XPATH, value='//*[@id="u131058078"]/div/div[1]/div/div/main/div/div[2]/div/div'
                                                    '[3]/div/div/button[2]')

    driver.execute_script("arguments[0].click();", log_in)

    driver.implicitly_wait(10)

    log_fb = driver.find_element(by=By.XPATH,
                                 value='//*[@id="u-1597322998"]/div/div/div[1]/div/div[3]/span/div[2]/button')

    driver.execute_script("arguments[0].click();", log_fb)

    time.sleep(2)

    base_window = driver.window_handles[0]
    fb_log_window = driver.window_handles[1]
    driver.switch_to.window(fb_log_window)

    email_fb = driver.find_element(by=By.XPATH,
                                value='//*[@id="email"]')
    email_fb.send_keys(mail)

    password_fb = driver.find_element(by=By.ID,
                                      value='pass')
    password_fb.send_keys(password)

    to_log = driver.find_element(by=By.XPATH,
                                 value='//*[@id="loginbutton"]')
    driver.execute_script("arguments[0].click();", to_log)

    driver.switch_to.window(base_window)
    time.sleep(2)

    location = driver.find_element(by=By.XPATH,
                                   value='//*[@id="u-1597322998"]/div/div/div/div/div[3]/button[1]')
    driver.execute_script("arguments[0].click();", location)

    not_interested = driver.find_element(by=By.XPATH,
                                         value='//*[@id="u-1597322998"]/div/div/div/div/div[3]/button[2]')
    driver.execute_script("arguments[0].click();", not_interested)

    cookies = driver.find_element(by=By.XPATH,
                                  value='//*[@id="u131058078"]/div/div[2]/div/div/div[1]/div[1]/button')
    driver.execute_script("arguments[0].click();", cookies)

    next_person = driver.find_element(by=By.XPATH,
                                      value='//*[@id="u131058078"]/div/div[1]/div/div/main/div/div/'
                                            'div[1]/div/div[4]/div/div[2]/button')
    for n in range(100):
        time.sleep(2)
        driver.execute_script("arguments[0].click();", next_person)


except selenium.common.exceptions.NoSuchElementException:
    print('not working as expected')
