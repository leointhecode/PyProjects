
import requests
import smtplib

# CONSTANTS ------------------------------------------------------------------------------------------------------------
CURRENCY = "BTC"
MY_CURRENCY = "USD"
CRYPTO_URL = "https://www.alphavantage.co/query"
NEWS_URL = " https://newsapi.org/v2/everything"

CRYPTO_API_KEY = "O1A275JJI0QBNTW5"
NEWS_API_KEY = "c72d3280e7ef4f97acd78868e45110b2"
MY_EMAIL = "strongmaidboy@gmail.com"
MY_PASSWORD = "501073yt lol"
EMAIL_TS = "leonardespicass@gmail.com"

# CRYPTO API -----------------------------------------------------------------------------------------------------------

crypto_parameters = {
    "function": 'DIGITAL_CURRENCY_DAILY',
    "symbol": CURRENCY,
    "market": MY_CURRENCY,
    "apikey": CRYPTO_API_KEY
}

crypto_api = requests.get(CRYPTO_URL, params=crypto_parameters)
crypto_data = crypto_api.json()

crypto_3days = list(crypto_data['Time Series (Digital Currency Daily)'].items())[1:3]
difference = [float(f_price[1]['4a. close (USD)']) for f_price in crypto_3days]

percent_difference = int(((difference[1] - difference[0]) * 100) / difference[0])
percent_difference_str = f"{percent_difference}%"

# NEWS API -------------------------------------------------------------------------------------------------------------
news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": "bitcoin",
}

news_api = requests.get(NEWS_URL, params=news_parameters)
news_data = news_api.json()['articles'][:3]

if percent_difference > 4.9 or percent_difference < -4.9:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=EMAIL_TS,
                            msg=f"Subject:The {CURRENCY} has changed \n\n"
                            f"{CURRENCY} : {percent_difference_str}\n\n"
                            "RELEVANT NEWS:\n\n"

                                f"HEADLINE: {news_data[0]['title'].upper().encode('ascii', 'ignore').decode('ascii')}\n"
                                f"SUMMARY: {news_data[0]['description'].encode('ascii', 'ignore').decode('ascii')}\n"
                                f"URL: {news_data[0]['url']} \n\n"

                                f"HEADLINE: {news_data[1]['title'].upper().encode('ascii', 'ignore').decode('ascii')}\n"
                                f"SUMMARY: {news_data[1]['description'].encode('ascii', 'ignore').decode('ascii')}\n"
                                f"URL: {news_data[1]['url']} \n\n"

                                f"HEADLINE: {news_data[2]['title'].upper().encode('ascii', 'ignore').decode('ascii')}\n"
                                f"SUMMARY: {news_data[2]['description'].encode('ascii', 'ignore').decode('ascii')}\n"
                                f"URL: {news_data[2]['url']} \n\n"
                            )
else:
    print("no important issues")
