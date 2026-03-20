class DiscountStrategy:

    def apply(self, price):
        return price


class TenPercentDiscount(DiscountStrategy):

    def apply(self, price):
        return price * 0.9


class PriceCalculator(DiscountStrategy):

    def __init__(self, discount_strategy):
        self._discount_strategy = discount_strategy

    def calculate(self, price):
        return self._discount_strategy.apply(price)