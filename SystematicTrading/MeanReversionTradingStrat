# region imports
from AlgorithmImports import *
# endregion

class MeanReversionTrading(QCAlgorithm):

    def initialize(self):
        self.set_start_date(2018, 10, 16)
        self.set_end_date(2020, 10, 16)
        self.set_cash(10000)

        self.vnq = self.add_equity("VNQ", Resolution.DAILY)
        self.vnqi = self.add_equity("VNQI", Resolution.DAILY)


    def on_data(self, data):
        
        vnqi_gain = (self.vnqi.close - self.vnqi.open)/self.vnqi.open
        vnq_gain = (self.vnq.close - self.vnq.open)/self.vnq.open


        if vnqi_gain > 0.02 and vnqi_gain > vnq_gain:
            self.set_holdings(self.vnq.symbol,1,True)
            self.log(f"VNQI GAIN: {vnqi_gain}")

        if vnq_gain > 0.02 and vnq_gain > vnqi_gain:
            self.set_holdings(self.vnqi.symbol,1,True)
            self.log(f"VNQ GAIN: {vnq_gain}")

        else:
            self.log("No Action Taken")
            return
        

