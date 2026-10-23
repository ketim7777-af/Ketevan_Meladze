class Payment:
    def process_payment(self, amount):
        print("Payment is processing")


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        super().process_payment(amount)
        print(f"Paid by bank card: {amount} Lari")


class PayPalPayment(Payment):
    def process_payment(self, amount):
        super().process_payment(amount)
        print(f"Paid by PayPal: {amount} Lari")


credit_card = CreditCardPayment()
paypal = PayPalPayment()

credit_card.process_payment(500)
paypal.process_payment(250)
