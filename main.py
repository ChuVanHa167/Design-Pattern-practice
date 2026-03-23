from patterns.creational.payment_factory import PaymentFactory
from patterns.creational.singleton_logger import Logger
from patterns.structural.order_facade import OrderFacade
from patterns.behavioral.discount_strategy import TenPercentDiscount, PriceCalculator



payment = PaymentFactory.create_payment("credit") #Client không cần biết tạo object như thế nào, chỉ cần gọi factory
payment.pay(200)

logger = Logger() # Client có thể tạo nhiều instance của Logger nhưng tất cả đều trỏ đến cùng một instance duy nhất.
logger.log("Order started") 

facade = OrderFacade() 
facade.place_order() # Client chỉ cần gọi phương thức place_order() của facade mà không cần quan tâm đến các bước phức tạp bên trong hệ thống.

discount = TenPercentDiscount() # Client có thể dễ dàng thay đổi chiến lược giảm giá bằng cách tạo một instance của chiến lược mới và truyền nó vào PriceCalculator mà không cần sửa đổi code của PriceCalculator hoặc các phần khác của hệ thống.

calculator = PriceCalculator(discount) # PriceCalculator sử dụng một đối tượng DiscountStrategy để tính toán giá sau khi áp dụng giảm giá. Điều này cho phép chúng ta dễ dàng thay đổi chiến lược giảm giá mà không cần sửa đổi code của PriceCalculator hoặc các phần khác của hệ thống.

print("Discount price:", calculator.calculate(100))