import matplotlib.pyplot as plt

class Graph:

    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def liveGraph(self,x,y, buys, avBuyPrice, avSellPrice, percentage, money, indicator):
        """Creates a live updating graph which displays the average
            buy and sell prices of a given crypto as well as the percentage
            profit margin of the trading session and total money.

        Args:
            x(list): X axis points
            y(list): Y axis points
        """
        self.ax.plot(x,y)
        self.fig.suptitle(f"AverageBuy$: {avBuyPrice:.2f}\nAverageSell$: {avSellPrice:.2f}\nMoney: ${money:.2f}")
        plt.xticks(rotation=45)
        plt.pause(0.05)

    def clear(self):
        plt.cla()

    def plot(self, y, x, color):
        self.ax.plot(y, x,color)

    def show(self):
        plt.show()
