import smtplib
from data_manager import emails

MY_EMAIL = "strongmaidboy@gmail.com"
MY_PASSWORD = "INU-noTaisho3$4"


class NotificationManager:
    def __init__(self, parameters: dict):
        self.name = parameters[-1]['city']
        self.IATA = parameters[-1]['iataCode']
        self.price = parameters[-1]['lowestPrice']
        self.arrival = parameters[-1]['arrival']
        self.departure = parameters[-1]['departure']
        self.send_mail()

    def send_mail(self):
        for mail in emails:
            print(mail)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)

                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=mail,
                                    msg="Subject:Best Daily Deal \n\n"
                                        f"A wild round flight to {self.name} {self.IATA} came out from the grass, "
                                        f"it costs {self.price} "
                                        f"and it arrives on {self.arrival} to depart on {self.departure}"
                                    )

