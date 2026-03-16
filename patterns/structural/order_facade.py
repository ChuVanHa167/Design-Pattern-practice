class PaymentService:

    def pay(self):
        print("Processing payment")


class ShippingService:

    def ship(self):
        print("Shipping order")


class NotificationService:

    def notify(self):
        print("Sending notification")


class OrderFacade:

    def place_order(self):

        payment = PaymentService()
        shipping = ShippingService()
        notification = NotificationService()

        payment.pay()
        shipping.ship()
        notification.notify()