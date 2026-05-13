# region imports
from AlgorithmImports import *
# endregion

class FormalAsparagusFly(QCAlgorithm):

    def initialize(self):
        self.set_start_date(2020, 1, 1)
        self.set_end_date(2021,2,1)
        self.set_cash(10000000)

        self.universe_settings.resolution = Resolution.DAILY
        self.add_universe(self.CoarseSelection, self.FineSelection)

 #   def CoarseSelection(self, coarse):
#
 #       sort_by_price = sorted(coarse, key=lambda eq: eq.Price, reverse= True)
#
 #       self.list_of_symbols = [x.Symbol for x in sort_by_price][:10]
#
 #       return self.list_of_symbols
    def CoarseSelection(self, coarse):

        self.filtered_by_price = [x.Symbol for x in coarse if x.Price > 20 and x.DollarVolume > 10000000 and x.HasFundamentalData]

        return self.filtered_by_price

    def FineSelection(self, fine):
        self.filtered_by_pe = [sec for sec in fine if sec.ValuationRatios.PERatio < 100]

        sorted_by_ebit = sorted(self.filtered_by_pe, key=lambda x: x.FinancialStatements.IncomeStatement.EBIT.TwelveMonths)

        self.list_of_symbols = [x.Symbol for x in sorted_by_ebit]

        return self.list_of_symbols

    def OnData(self, data):

        self.log(self.time)

 #       for sec in self.securities.values:
#
  #          if not data.ContainsKey(sec.Symbol) or not data[sec.Symbol]:
 #               return
#
 #           self.log(f"{data[sec.Symbol].Symbol} opened at: {data[sec.Symbol].Open}")

        self.log("--------------------")

    def on_securities_changed(self, changes):

        self.log("CHANGE IN UNIVERSE")

        for sec in changes.RemovedSecurities:
            self.liquidate(sec.Symbol)
            self.log(f"Sold: {sec}")

        for sec in changes.AddedSecurities:
            self.set_holdings(sec.Symbol, 0.1)
            self.log(f"BOUGHT: {sec}")
