from INTC_Stock import Stock

businessman = Stock("INTC", "Intel Corporation", 20.5, 20.35)
print(
    f"\nThe price change percentage of INTC's stock is {businessman.get_ChangePercent()}\n")