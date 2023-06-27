import finnhub

class FinnHubData:

    def __init__(self, key):
        self.key = key
        self.client = finnhub.Client(api_key=self.key)

    def getCandle(self, ticker, resolution, start, end):
        '''
        Returns candlestick data for the given ticker
        Args:
            ticker(str): the given ticker
            resolution(str): the timeframe for the data (1, 5, 15, 30, 60, D, W, M)
            start(str): unix timestamp for start time 
            end(str): unix timestamp for end time
        Returns:
            self.client.stock_candles(ticker, resolution)
        '''
        return self.client.stock_candles(ticker, resolution)

    def getPrice(self, ticker):
        return self.client.quote(ticker).get('c')

    def getEMA(self, ticker, timeperiod=3, seriestype='c'):
        #this line is broken fix it
        return self.client.technical_indicator(symbol=ticker, indicator='ema', timeperiod=3, seriestype='c')

    def getMACD(self, ticker, start, end, res='D', stype='c', fastperiod=12, slowperiod=26, signalperiod=9):
        '''
        Returns data for a given ticker containing the MACD correlating to the args specified in this format:
        {'c': [], 'h': [], 'l': [], 'o': [], 's': '', 'macd': [], 't': [], 'v': []}
        Args:
            ticker
            start
            end
            res
            stype
            fastperiod
            slowperiod
            signal_period
        Returns:
            self.client.technical_indicator(symbol=ticker, indicator= 'macd', resolution=res, _from=start,
            to=end, indicator_fields={'seriestype': stype, 'fastperiod': fastperiod,
            'slowperiod': slowperiod, 'signalperiod': signalperiod})
        '''
        return self.client.technical_indicator(symbol=ticker, indicator= 'macd', resolution=res, _from=start, to=end, indicator_fields={'seriestype': stype,
                                                                                                   'fastperiod': fastperiod, 'slowperiod': slowperiod,
                                                                                                   'signalperiod': signalperiod})

