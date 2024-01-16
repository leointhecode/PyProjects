from RentDataExtractor import ExtractData
from DataEntryBot import DataBot

FORM = "https://forms.gle/6S81dmXE3sNfDa9QA"
SEARCH = "https://anitrendz.net/charts/top-anime/"

CHROME_DRIVER_PATH = "/home/lenny/development/chromedriver"

data = ExtractData(url=SEARCH)
ranking = data.get_data()

bot = DataBot(driver_path=CHROME_DRIVER_PATH)

bot.submit_to_form(form=FORM, data=ranking)
