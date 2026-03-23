# vấn đề (Hệ thống cần áp dụng các chiến lược giảm giá khác nhau mà không làm thay đổi code chính),
# ý tưởng (Strategy pattern cho phép định nghĩa một họ các thuật toán, đóng gói chúng và làm cho chúng có thể thay thế cho nhau),
# kết luận (Strategy pattern giúp tách biệt thuật toán giảm giá ra khỏi phần còn lại của hệ thống, cho phép dễ dàng thêm các chiến lược mới mà không ảnh hưởng đến code hiện tại.)

class DiscountStrategy: # Lớp DiscountStrategy là một interface (hoặc abstract class) mà tất cả các chiến lược giảm giá sẽ kế thừa. Nó định nghĩa phương thức apply() mà các chiến lược phải triển khai.

    def apply(self, price):
        return price


class TenPercentDiscount(DiscountStrategy): # Chiến lược giảm giá cụ thể, nó triển khai phương thức apply() để áp dụng giảm giá 10% cho giá gốc.

    def apply(self, price):
        return price * 0.9


class PriceCalculator(DiscountStrategy): # Lớp PriceCalculator sử dụng một đối tượng DiscountStrategy để tính toán giá sau khi áp dụng giảm giá.

    def __init__(self, discount_strategy):
        self._discount_strategy = discount_strategy

    def calculate(self, price):
        return self._discount_strategy.apply(price)