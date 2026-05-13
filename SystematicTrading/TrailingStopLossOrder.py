# region imports
from AlgorithmImports import *
# endregion

class TrailingStopLossOrder(QCAlgorithm):

    def initialize(self):
        self.set_start_date(2018, 1, 1)
        self.set_end_date(2019,1,1)
        self.set_cash(100000)
        self.spy = self.add_equity("SPY", Resolution.DAILY)

        self.invest = True
        self.first_close_price = None
        self.sell_ticket = None
        self.highest_price = 0

    def on_data(self, data):
        if not self.portfolio.invested and self.invest:
            self.market_order(self.spy.symbol, 1)
            self.first_close_price = self.securities['SPY'].close
            self.invest = False

        if self.sell_ticket is None:
            self.sell_ticket = self.stop_market_order(self.spy, -1, self.first_close_price * 0.9)


    def on_end_of_day(self):
        if self.sell_ticket is None:
            return

        if self.securities['SPY'].close > self.highest_price:
            self.highest_price = self.securities['SPY'].close
            update_ticket = UpdateOrderFields()
            update_ticket.stop_price = self.highest_price * 0.9
            status = self.sell_ticket.update(update_ticket)

            if status.is_success:
               self.log(f"Updated Stop price {update_ticket.stop_price}")

