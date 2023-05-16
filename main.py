import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

#from binance.client import Client
#from binance.um_futures import UMFutures
api_key = 'SqhK9j9t156vaQpf4AirqaBBmEWzAxZfrtugd4O3WiTPeE26sAynvhuxpY8BOfo2'
api_secret = '7V2Vy7WvaOHgBN7sFyH1V9FJ48n0NMsqhHF5oPXkWi0cfEAZH113oW0NUcHmfChT'

def forecast_cpi():
                header = {'User-Agent': 'Mozilla/5.0',
                        'Content-Type': 'text/html;charset=utf-8'
                        }
                response = requests.get("https://www.investing.com/economic-calendar/cpi-733", headers=header)

                contents = BeautifulSoup(response.content, 'html.parser')

                forecast_cpi = contents.find('div',{'class':'arial_14 noBold'})
                float_forecast = forecast_cpi.text
                x = ""
                i = 0
                while i < len(float_forecast) - 1:
                    x = x + float_forecast[i]
                    i += 1

                return(x)

def actual_cpi():
                header = {'User-Agent': 'Mozilla/5.0',
                          'Content-Type': 'text/html;charset=utf-8'
                          }
                response = requests.get("https://www.investing.com/economic-calendar/cpi-733", headers = header)

                contents = BeautifulSoup(response.content, 'html.parser')

                actual_cpi = contents.find('div',{'class':'arial_14 greenFont'})
                float_actual = actual_cpi.text
                x = ""
                i = 0
                while i < len(float_actual) - 1:
                    x = x + float_actual[i]
                    i += 1
                return(x)


def open_long():
        #futures_client.new_order(symbol="BTCBUSD", side="BUY", type="MARKET", quantity=0.001)
        #time.sleep(10)
        #while len(client.futures_get_open_orders(symbol="BTCBUSD")) >= 2:
        #        time.sleep(0.1)
        #futures_client.cancel_open_orders(symbol="BTCBUSD")
        #return
        print("open long")

def open_short():
    #futures_client.new_order(symbol="BTCBUSD", side="SELL", type="MARKET", quantity=0.001)
    #time.sleep(10)
    #while len(client.futures_get_open_orders(symbol="BTCBUSD")) >= 2:
    #    time.sleep(0.1)
    #futures_client.cancel_open_orders(symbol="BTCBUSD")
    #return
    print("open short")

def trading_loop():
    dates = []
    while True:
        print("yes")
        header = {'User-Agent': 'Mozilla/5.0',
                  'Content-Type': 'text/html;charset=utf-8'
                  }
        response = requests.get("https://www.investing.com/economic-calendar/cpi-733", headers=header)

        contents = BeautifulSoup(response.content, 'html.parser')
        date = contents.find('div', {'class': 'noBold'})
        dates.append(date)
        if len(dates) > 4:
            dates.remove(dates[0])
        a_cpi = float(actual_cpi())
        f_cpi = float(forecast_cpi())
        if len(dates) > 2:
            if dates[-1] != dates[-2]:
                if f_cpi > a_cpi:
                        if f_cpi - a_cpi > 0.3:
                                open_long()
                elif a_cpi > f_cpi:
                        if a_cpi - f_cpi > 0.3:
                                open_short()
        time.sleep(1)
"""
def main():
        client = Client(api_key, api_secret)
        futures_client = UMFutures(key=api_key, secret=api_secret)
        while True:
                ema = startup_loop(client)
                trading_loop(futures_client, client, ema)
"""
if __name__ == "__main__":
    trading_loop()

