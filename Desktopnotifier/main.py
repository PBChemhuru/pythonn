import datetime
import time
import requests  # for retrieving coronavirus data from web
from plyer import notification  # for getting notification on your PC

covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/zimbabwe/")
except:
    print("Please! Check your internet connection")

if covidData is not None:
    data = covidData.json()["Success"]

    while True:
        notification.notify(
            title="COVID19 Stats on {}".format(datetime.date.today()),
            message="Total cases : {totalcases} \nToday cases : {todaycases} \nToday deaths :{todaydeaths}\nTotal "
                    "active :{active} ".format(
                totalcases=data["cases"],
                todaycases=data["todayCases"],
                todaydeaths=data["todayDeaths"],
                active=data["active"]),
            # creating icon for the notification
            # we need to download a icon of ico file format

            timeout=50,
            app_name="covidcasehunter"
        )
        # sleep for 4 hrs => 60*60*4 sec
        # notification repeats after every 4hrs
        time.sleep(60 * 60 * 4)

#title: title of notification
#message:Message of the notification
#app_name:Name of the app launching this notififcation
#app_icon:Icon to be displayed along with message
#timeout:time to display the message for
#ticker:text to display on the status bar as the notification arrives
#toast:simple message instead of full notification