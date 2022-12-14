# name: Villas, Justin Lawrence DL.
#lab: 3.3
#cource: cmpe30053
# -------------------------------------------------------------------------

class Stock:

    # ------------------------------------------------------------------
    # purpose: initilize the variables that will be used
    # parameter: pecifiedSymbol, name, previousPrice and currentPrice are the ints containg the INTC'S info.
    # return:    none
    def __init__(self, specifiedSymbol, name, previousPrice, currentPrice):
        self.__specifiedSymbol = specifiedSymbol
        self.__name = name
        self.__previousPrice = previousPrice
        self.__currentPrice = currentPrice

    # ------------------------------------------------------------------
    # purpose: when called return the value of self.__name
    # parameter: none
    # return:  self.__name

    def corp_name(self):
        return self.__name

    # ------------------------------------------------------------------
    # purpose: when called return the value of self.__specifiedSymbol
    # parameter: none
    # return:  self.__specifiedSymbol
    def corp_symbol(self):
        return self.__specifiedSymbol

    # ------------------------------------------------------------------
    # purpose: when called return the value of self.__previousPrice
    # parameter: none
    # return:  self.__previousPrice

    def get_previousPrice(self):
        return self.__previousPrice.get()

    # ------------------------------------------------------------------
    # purpose: when called return the value of self.__currentPrice
    # parameter: none
    # return:  self.__currentPrice
    def get_currentPrice(self):
        return self.__currentPrice.get()

    # purpose: Set the value of self.__previousPrice to previousPrice
    # parameter: none
    # return:  none
    def set_previousPrice(self):
        self.__previousPrice = previousPrice

    # purpose: Set the value of self.___currentPrice = currentPrice
    # parameter: none
    # return:  none
    def set_currentPrice(self):
        self.___currentPrice = currentPrice

    # purpose: Calculate the  percentage   changed.
    # parameter: none
    # return:  percentage   changed
    def get_ChangePercent(self):
        diffPrice = self.__previousPrice - self.__currentPrice
        qoutientChange = (diffPrice / self.__previousPrice)*100
        formatFloat = "{:.2f}".format(qoutientChange)
        percentagechanged = formatFloat
        return percentagechanged



