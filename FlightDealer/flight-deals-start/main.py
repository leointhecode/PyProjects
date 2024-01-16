from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

SAME = False

print("Welcome to Leo's Flight Club.\nWe find the best deal flights 4 you.")

name = input("What is your first name: ")
last_name = input("What is your last name: ")

while not SAME:
    mail = input("What is your email: ")
    mail_test = input("Type your mail again: ")

    if mail == mail_test:
        SAME = True

        flight_search = FlightSearch()
        deal = flight_search.best_deal()

        add_to_sheet = DataManager(deal, name, last_name, mail)
        add_to_sheet.add_row()
        add_to_sheet.add_user()

        send_mail = NotificationManager(deal)
