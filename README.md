# Design-Pattern-practice
thực hành DP

# Thực Hành Design Pattern với Python

## Mini Project: Advanced Order System

---

# 1. Giới thiệu

Repository này là **phần 3 trong chuỗi thực hành Software Design**:

1. OOP Practice
2. SOLID Practice
3. Design Pattern Practice
4. Architecture Integration (OOP + SOLID + Design Pattern)

Repo này tập trung vào **Design Pattern**.

Mục tiêu là hiểu cách **giải quyết các vấn đề thiết kế phần mềm bằng pattern**.

---

# 2. Mục tiêu học tập

Sau khi hoàn thành repo này bạn sẽ:

* Hiểu **3 nhóm Design Pattern**
* Biết **khi nào cần dùng pattern**
* Biết **giải quyết các vấn đề thiết kế phổ biến**
* Biết **viết code linh hoạt và dễ mở rộng**

---

# 3. Ba nhóm Design Pattern

## Creational Patterns

Giải quyết vấn đề:

> **Tạo object như thế nào?**

Ví dụ:

```
Factory
Singleton
Builder
```

---

## Structural Patterns

Giải quyết vấn đề:

> **Tổ chức và kết hợp các class như thế nào?**

Ví dụ:

```
Adapter
Decorator
Facade
```

---

## Behavioral Patterns

Giải quyết vấn đề:

> **Các object giao tiếp với nhau như thế nào?**

Ví dụ:

```
Strategy
Observer
Command
```

---

# 4. Bài toán thực hành

Xây dựng **hệ thống đặt hàng nâng cao**.

Yêu cầu:

* Hỗ trợ nhiều phương thức thanh toán
* Hỗ trợ nhiều chiến lược giảm giá
* Hệ thống gửi notification khi order hoàn thành
* Logging hệ thống

Đây là những vấn đề **Design Pattern được sinh ra để giải quyết**.

---

# 5. Cấu trúc project

Tạo cấu trúc:

```
repo3-design-pattern

src/

models/
    product.py
    order.py

patterns/

creational/
    payment_factory.py
    singleton_logger.py

structural/
    payment_adapter.py
    order_facade.py

behavioral/
    discount_strategy.py
    notification_observer.py

main.py
```

---

# 6. Creational Pattern

## Problem

Hệ thống có nhiều loại payment:

```
CreditCard
Paypal
BankTransfer
Crypto
```

Nếu tạo object trực tiếp:

```
payment = CreditCardPayment()
```

code sẽ **khó mở rộng**.

---

## Solution — Factory Pattern

File:

```
patterns/creational/payment_factory.py
```

Code:

```python
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
```

---

## Sử dụng

```
payment = PaymentFactory.create_payment("credit")

payment.pay(100)
```

---

## Ý nghĩa

Factory giúp:

```
tách logic tạo object khỏi business logic
```

---

# 7. Creational Pattern 2 — Singleton

## Problem

Logger nên **chỉ có 1 instance** trong hệ thống.

---

File:

```
patterns/creational/singleton_logger.py
```

Code:

```python
class Logger:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def log(self, message):
        print(f"[LOG] {message}")
```

---

## Test

```
logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)
```

Output:

```
True
```

---

# 8. Structural Pattern — Facade

## Problem

Checkout order cần gọi nhiều hệ thống:

```
Payment
Inventory
Shipping
Notification
```

Nếu gọi trực tiếp sẽ rất phức tạp.

---

## Solution — Facade

File:

```
patterns/structural/order_facade.py
```

Code:

```python
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
```

---

## Sử dụng

```
order = OrderFacade()

order.place_order()
```

---

## Ý nghĩa

Facade giúp:

```
ẩn sự phức tạp của hệ thống
```

---

# 9. Behavioral Pattern — Strategy

## Problem

Hệ thống có nhiều cách giảm giá:

```
No discount
10% discount
20% discount
```

Nếu dùng `if else` code sẽ xấu.

---

## Solution — Strategy Pattern

File:

```
patterns/behavioral/discount_strategy.py
```

Code:

```python
class DiscountStrategy:

    def apply(self, price):
        return price


class TenPercentDiscount(DiscountStrategy):

    def apply(self, price):
        return price * 0.9


class TwentyPercentDiscount(DiscountStrategy):

    def apply(self, price):
        return price * 0.8
```

---

## Context

```python
class PriceCalculator:

    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, price):
        return self.strategy.apply(price)
```

---

## Test

```
discount = TenPercentDiscount()

calculator = PriceCalculator(discount)

print(calculator.calculate(100))
```

Output:

```
90
```

---

# 10. Behavioral Pattern — Observer

## Problem

Khi order hoàn thành:

```
email
sms
analytics
```

đều cần được thông báo.

---

## Solution — Observer Pattern

File:

```
patterns/behavioral/notification_observer.py
```

Code:

```python
class Observer:

    def update(self, message):
        pass


class EmailService(Observer):

    def update(self, message):
        print(f"Email notification: {message}")


class SMSService(Observer):

    def update(self, message):
        print(f"SMS notification: {message}")
```

---

## Subject

```python
class Order:

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self):

        for obs in self.observers:
            obs.update("Order completed")
```

---

# 11. Demo chương trình

File:

```
main.py
```

```python
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
```

---

# 12. Sau khi hoàn thành repo này

Bạn sẽ làm:

```
repo4-clean-architecture-system
```

Trong repo này bạn sẽ **kết hợp toàn bộ:**

```
OOP
SOLID
Design Pattern
Architecture
```

để xây dựng **một hệ thống hoàn chỉnh**.
