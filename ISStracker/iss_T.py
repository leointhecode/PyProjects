import time
import requests
import datetime as dt
import smtplib

# CONSTANTS
MY_LAT = 19.282350
MY_LON = -99.177520
MY_EMAIL = "strongmaidboy@gmail.com"
MY_PASSWORD = "501073yt lol"


def iss_near():
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LON - 5 <= longitude <= MY_LON + 5 and time_now in range(22, 6):
        return True
    else:
        return False


# ISS
response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()

iss_position = response_iss.json()["iss_position"]
longitude = float(iss_position["longitude"])
latitude = float(iss_position["latitude"])

# TIME
response_sunrise = requests.get(url="https://api.sunrise-sunset.org/json?lat=19.4326296&lng=-99.1331785&formatted=0")
response_sunrise.raise_for_status()

time_now = int(str(dt.datetime.now().time()).split(":")[0])

data_sunrise = response_sunrise.json()
sunrise = int(data_sunrise['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data_sunrise['results']['sunset'].split("T")[1].split(":")[0])

while True:
    time.sleep(60)
    if iss_near():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)

            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="errnoleg@mofu.be",
                                msg="LOOK UP!!\n\n"
                                    "The iss is in the sky.",
                                )
    else:
        print("There's no ISS")
        pass
