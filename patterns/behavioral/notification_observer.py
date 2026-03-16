class Observer:

    def update(self, message):
        pass


class EmailService(Observer):

    def update(self, message):
        print(f"Email notification: {message}")


class SMSService(Observer):

    def update(self, message):
        print(f"SMS notification: {message}")