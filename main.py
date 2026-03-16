from patterns.creational.payment_factory import PaymentFactory
from patterns.creational.singleton_logger import Logger
from patterns.structural.order_facade import OrderFacade
from patterns.behavioral.discount_strategy import TenPercentDiscount, PriceCalculator


payment = PaymentFactory.create_payment("credit")
payment.pay(200)

logger = Logger()
logger.log("Order started")

facade = OrderFacade()
facade.place_order()

discount = TenPercentDiscount()

calculator = PriceCalculator(discount)

print("Discount price:", calculator.calculate(100))