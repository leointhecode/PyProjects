import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/home/lenny/development/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get('https://www.linkedin.com/jobs/search/?keywords=Python%20Developer&location=United%20States&locationId='
           '&geoId=103644278&f_TPR=&f_WT=2&f_PP=105126671%2C102571732%2C102277331&position=1&pageNum=0')

sign_in_button = driver.find_element(by=By.CLASS_NAME, value='nav__button-secondary')

sign_in_button.click()

time.sleep(2)

username = driver.find_element(by=By.ID, value='username')
password = driver.find_element(by=By.ID, value='password')
final_sign_in = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')

username.send_keys('leonardespicass@gmail.com')
password.send_keys('Inu-noTaisho5@3$')
final_sign_in.click()

time.sleep(2)

tags = driver.find_elements(by=By.CSS_SELECTOR, value='.job-card-container--clickable')
save_button = driver.find_element(by=By.CSS_SELECTOR, value='.jobs-save-button')

for tag in tags:
    try:
        time.sleep(2)
        save_button.click()
    except selenium.common.exceptions.StaleElementReferenceException:
        pass
    except selenium.common.exceptions.ElementNotInteractableException:
        pass

