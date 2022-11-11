import requests
import time
city = "Moscow,RU"
appid = "a972e521afd5bb3e79325885525d43f5"
exclude='minute,hourly'
res = requests.get(f"http://api.openweathermap.org/data/2.5/forecast/daily",
                   params ={'q': city,'units': 'metric','appid':appid,"cnt":"8"})

data = res.json()






print("Прогноз погоды на неделю")
for i in data['list']:

    print(time.ctime(i['dt']),"Температура Утренняя",i["temp"]["morn"],
          "\r\n Температура Дневная",i["temp"]["day"],
           "\r\n Температура Вечерняя",i["temp"]["eve"],
            "\r\n Среднесуточная температура",(i["temp"]["morn"] + i["temp"]["day"]+i["temp"]['eve'])/3)