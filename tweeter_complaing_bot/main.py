from InternetSpeedBot import Bot

PROMISED_DOWN = 100
PROMISED_UP = 100
CHROME_DRIVER_PATH = "/home/lenny/development/chromedriver"
TWITTER_EMAIL = 'touchmelenny@gmail.com'
TWITTER_PASSWORD = "Inu-noTaisho5@3$"


bot = Bot(CHROME_DRIVER_PATH)

data = bot.get_internet_speed()

if data[0] < 101.0 or data[1] < 101.0:
    bot.tweet_provider(data=data, twitter_mail=TWITTER_EMAIL, password=TWITTER_PASSWORD)
else:
    bot.quit_all()
