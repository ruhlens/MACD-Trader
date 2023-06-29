import matplotlib.pyplot as plt

class Graph:

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.fig.set_facecolor('black')

    def liveGraph(self,x,y, shares, avBuyPrice, avSellPrice, percentage, money, indicator, price, ticker):
        """Creates a live updating graph which displays the average
            buy and sell prices of a given crypto as well as the percentage
            profit margin of the trading session and total money.

        Args:
            x(list): X axis points
            y(list): Y axis points
        """
        self.ax.plot(x,y, color='red')
        value = shares * price
        plt.title(f'{ticker} LiveTrader', color='white')
        suptitle = self.fig.suptitle(f"Price: ${price}\n\nAvBuy: \${avBuyPrice:.2f}\n\nAvSell: \${avSellPrice:.2f}\n\nMACD: {indicator:.2f}\n\n#ofShares: {shares}\n\nValue: ${value}\n\nCash: ${money:.2f}\n\nTotal$: ${value + money}", color='white')
        suptitle.set_position((0.93, 0.8))  # Adjust the position
        plt.subplots_adjust(right=0.8, left = 0.08)
        plt.gca().set_facecolor('black')
        plt.xticks(rotation=45)
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        plt.pause(0.05)

    def clear(self):
        plt.cla()

    def plot(self, y, x, color):
        self.ax.plot(y, x,color)

    def show(self):
        plt.show()
