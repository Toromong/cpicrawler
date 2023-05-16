import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

header = {'User-Agent': 'Mozilla/5.0',
                        'Content-Type': 'text/html;charset=utf-8'
                        }
response = requests.get("https://www.investing.com/economic-calendar/cpi-733", headers=header)

contents = BeautifulSoup(response.content, 'html.parser')

forecast_cpi = contents.find('div',{'class':'arial_14 noBold'})
float_forecast =(forecast_cpi.text)
x = ""
i = 0
while i<len(float_forecast)-1:
    x = x + float_forecast[i]
    i += 1

print(x)
print(float_forecast)
                #return(forecast_cpi.text)



actual_cpi = contents.find('div', {'class': 'arial_14 greenFont'})
print(actual_cpi)
dates = []
i = 0
while i<3:
    date = contents.find('div', {'class': 'noBold'})
    dates.append(date.text)
    i+=1
    #if len(dates)>2:
    #   dates.remove(date)
    #  if dates[-1] != dates[-2]:

print(dates)
        # return(actual_cpi.text)