# region imports
from AlgorithmImports import *
# endregion

class EnergeticFluorescentPinkChicken(QCAlgorithm):

    def initialize(self):
        self.set_start_date(2020, 1, 1)
        self.set_end_date(2021, 1, 1)
        self.set_cash(10000)
        self.spy = self.add_equity("SPY", Resolution.DAILY)
        self.securities['SPY'].set_leverage(100)
        self.invest = True

    def on_data(self, data):
        if not self.portfolio.invested and self.invest:
            self.set_holdings(self.spy.symbol,99)
            self.invest = False

    def on_margin_call(self, requests):
        for order in requests:
            new_quantity = int(order.quantity*1.1)
            requests.remove(order)
            new_order = SubmitOrderRequest(order.OrderType, order.SecurityType, order.symbol, new_quantity, order.StopPrice, order.LimitPrice, self.time, "OnMarginCall")
            requests.append(new_order)
    
        return requests
