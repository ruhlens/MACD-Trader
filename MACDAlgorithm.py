"""
THIS IS A PAPER TRADING PROGRAM BASED ON THE RSI ALGORITHM
BUY AT RSI = 30
SELL AT RSI = 70
"""

from algorithms import Algorithm
from graph import Graph
import keyboard
from datetime import datetime
from FinnHubData import FinnHubData
import time

#get data collection function running on a separate thread

def unixTime(days):
    return days * 86400

def main():
    """Main function to handle the algorithm."""
    print("RSI Trading Algorithm Started. Press 'Q' to Close")
    run = True
    money = 100000
    shares = 0
    x = []
    y = []
    index = 0
    graph = Graph()
    buys = []
    sells = []
    avBuyPrice = 0
    avSellPrice = 0
    percentage = 0
    key = 'cc06epiad3idf21ispa0'
    while run:
        if keyboard.is_pressed("q"):
            run = False
        ticker = "AAPL"
        client = FinnHubData(key)
        call = client.getMACD(ticker, int(time.time() - unixTime(365)), int(time.time()))
        time.sleep(1)
        currentPrice = call.get('c')[-1]
        currentTime = datetime.now().time().strftime("%H:%M:%S")
        indicator = call.get('macdHist')[-1]
        x.append(currentTime)
        y.append(float(f'{currentPrice:.2f}'))
        if len(x) > 20:
            x.remove(x[0])
            graph.clear()
        if len(y) > 20:
            y.remove(y[0])
            graph.clear()
        index += 1
        algo = Algorithm(indicator).MACD(indicator, 0, 0, currentPrice, money, shares)
        orderType = algo[0]
        money = algo[1]
        shares = algo[2]
        price = algo[3]
        percentage = (money - 100000) / 100000
        graph.liveGraph(x,y, buys, avBuyPrice, avSellPrice, percentage, money, indicator)
        if orderType == "B":
            buys.append(price)
        if orderType == "S":
            sells.append(price)
        if len(buys) > 0:
            avBuyPrice = sum(buys) / len(buys)
        if len(sells) > 0:
            avSellPrice = sum(sells) / len(sells)
    graph.show()

if __name__ == "__main__":
    main()
