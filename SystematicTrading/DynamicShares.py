# region imports
from AlgorithmImports import *
# endregion

class DynamicShares(QCAlgorithm):

    def initialize(self):
        self.set_start_date(2015, 1, 1)
        self.set_end_date(2020, 1, 1)
        self.set_cash(100000)
        self.apple = self.add_equity("SPY", Resolution.DAILY)

        self.invest_toggle = True
        self.sell_toggle = True


    def on_data(self, data):

        if not data[self.apple.symbol]:
            return

        if not self.portfolio.invested and self.invest_toggle:

            shares_to_buy = int(self.portfolio.cash / data[self.apple.symbol].open)
            #Same as SetHoldings
            self.market_order(self.apple.symbol, shares_to_buy)

            invest_toggle = False

            return

        profit = self.portfolio[self.apple.symbol].unrealized_profit_percent

        if profit >=0.1 and self.sell_toggle:

            held_shares = self.portfolio[self.apple.symbol].quantity

            self.market_order(self.apple.symbol, -(held_shares//2))
            self.sell_toggle = False


    def on_order_event(self, order_event):

        if order_event.FillQuantity == 0:
            return

        fetched = self.transactions.get_order_by_id(order_event.OrderId)

        self.log(f"{str(fetched.type)} was filled")
        self.log(f"Symbol was: {str(order_event.Symbol)}")
        self.log(f"Quantity was: {str(order_event.FillQuantity)}")

