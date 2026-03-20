class CreditCardPayment:

    def pay(self, amount):
        print(f"Credit Card payment: ${amount}")


class PaypalPayment:

    def pay(self, amount):
        print(f"Paypal payment: ${amount}")


class PaymentFactory:

    @staticmethod
    def create_payment(method):

        if method == "credit":
            return CreditCardPayment()

        elif method == "paypal":
            return PaypalPayment()

        else:
            raise Exception("Invalid payment method")
