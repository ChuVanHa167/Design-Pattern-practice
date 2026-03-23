# vấn đề (Hệ thống có nhiều bước phức tạp để đặt hàng),
# ý tưởng (Facade pattern cung cấp một giao diện đơn giản để tương tác với một hệ thống phức tạp),
# kết luận (Facade pattern giúp giảm sự phụ thuộc giữa client và hệ thống phức tạp, làm cho code dễ đọc và bảo trì hơn)

class PaymentService: # Lớp PaymentService đại diện cho một dịch vụ thanh toán, nó có phương thức pay() để xử lý thanh toán. Đây là một phần của hệ thống phức tạp mà chúng ta muốn ẩn đi khỏi client.

    def pay(self):
        print("Processing payment")


class ShippingService: # Lớp ShippingService đại diện cho một dịch vụ vận chuyển, nó có phương thức ship() để xử lý việc vận chuyển đơn hàng. Đây cũng là một phần của hệ thống phức tạp mà chúng ta muốn ẩn đi khỏi client.

    def ship(self):
        print("Shipping order")


class NotificationService: # Lớp NotificationService đại diện cho một dịch vụ thông báo, nó có phương thức notify() để gửi thông báo cho khách hàng. Đây cũng là một phần của hệ thống phức tạp mà chúng ta muốn ẩn đi khỏi client.

    def notify(self):
        print("Sending notification")


class OrderFacade: # Lớp OrderFacade là lớp facade, nó cung cấp một giao diện đơn giản để client có thể đặt hàng mà không cần quan tâm đến các bước phức tạp bên trong hệ thống. Phương thức place_order() sẽ gọi các dịch vụ cần thiết để hoàn thành việc đặt hàng.

    def place_order(self): # Phương thức place_order() là phương thức chính của facade, nó sẽ gọi các dịch vụ cần thiết để hoàn thành việc đặt hàng. Client chỉ cần gọi phương thức này mà không cần quan tâm đến các bước phức tạp bên trong hệ thống.

        payment = PaymentService()
        shipping = ShippingService()
        notification = NotificationService()

        payment.pay()
        shipping.ship()
        notification.notify()