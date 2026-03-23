# vấn đề (Hệ thống cần thông báo cho nhiều phần khác nhau khi có sự kiện xảy ra),
# ý tưởng (Observer pattern cho phép một object (subject) thông báo cho các object khác (observer) khi có sự thay đổi trạng thái)
# kết luận (Observer pattern giúp giảm sự phụ thuộc giữa các object và cho phép xây dựng hệ thống linh hoạt hơn)

class Observer: # Lớp Observer là một interface (hoặc abstract class) mà tất cả các observer sẽ kế thừa. Nó định nghĩa phương thức update() mà các observer phải triển khai.

    def update(self, message):
        pass


class EmailService(Observer):

    def update(self, message):
        print(f"Email notification: {message}")


class SMSService(Observer):

    def update(self, message):
        print(f"SMS notification: {message}")