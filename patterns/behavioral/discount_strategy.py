class DiscountStrategy:

    def apply(self, price):
        return price


class TenPercentDiscount(DiscountStrategy):

    def apply(self, price):
        return price * 0.9


class TwentyPercentDiscount(DiscountStrategy):

    def apply(self, price):
        return price * 0.8