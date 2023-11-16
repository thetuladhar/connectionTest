class Payment:
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PaypalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing cash payment of ${amount}")


list_of_payment_methods = [
    CreditCardPayment(),
    PaypalPayment(),
    CashPayment()
]

amount = 100.00

for methods in list_of_payment_methods:
    methods.process_payment(amount)