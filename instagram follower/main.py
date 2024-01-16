from InstagramGrowingBot import Bot

CHROME_DRIVER_PATH = "/home/lenny/development/chromedriver"
SIMILAR_ACCOUNT = "enfjmemesdaily"
IG_EMAIL = 'leonardespicass@gmail.com'
IG_PASSWORD = "Inu-noTaisho5@3$"

ig = Bot(CHROME_DRIVER_PATH)
ig.login(ig_mail=IG_EMAIL, ig_password=IG_PASSWORD)
ig.find_followers(account=SIMILAR_ACCOUNT)
