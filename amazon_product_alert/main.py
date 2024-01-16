import smtplib
import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com.mx/Computadora-Port%C3%A1til-Poli%C3%A9ster-Impermeable-Business/dp/B09BJHLLN3/" \
      "ref=sr_1_3?qid=1646481654&refinements=p_4%3ALubardy&s=apparel&sr=1-3"

headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Accept-Language':
    'en-US, en;q=0.9'
}

response = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

price = soup.find(name='span', class_='a-price-whole').getText()
price = float(price[:-1])

# EMAIL PART ----------------------------------------------------------------------------------------------------------

MY_EMAIL = "strongmaidboy@gmail.com"
MY_PASSWORD = "INU-noTaisho3$4"
DESIRED_PRICE = 290

if price <= 290:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs='touchmelenny@gmail.com',
                            msg="Subject:The price is lower uwu!! \n\n"
                                f"The price of the product is in {price}$ \n i'll leave you the link: \n\n {URL}")
else:
    pass
