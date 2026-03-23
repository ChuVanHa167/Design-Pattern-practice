# Polymorphism (OOP), vấn đề (hệ thống có nhiều phương thức thanh toán), 
# ý tưởng (Thay vì để logic tạo object nằm rải rác, mình gom nó lại vào một nơi gọi là Factory), 
# Factory Pattern giúp tách việc tạo object ra khỏi business logic, giúp code dễ mở rộng và tuân theo nguyên tắc Open-Closed.

class CreditCardPayment:

    def pay(self, amount):
        print(f"Credit Card payment: ${amount}")


class PaypalPayment:

    def pay(self, amount):
        print(f"Paypal payment: ${amount}")


class PaymentFactory: #class chuyên để tạo object

    @staticmethod
    def create_payment(method):

        if method == "credit": # Nếu người dùng chọn credit thì factory sẽ tạo CreditCardPayment
            return CreditCardPayment()

        elif method == "paypal":
            return PaypalPayment()

        else:
            raise Exception("Invalid payment method")
