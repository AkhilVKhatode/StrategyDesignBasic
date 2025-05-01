from abc import ABC, abstractmethod

# PaymentStrategy interface (defines the common method for all payment types)
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self):
        pass

# Concrete strategy for credit card payment
class CreditCardPayment(PaymentStrategy):
    def process_payment(self):
        print("Processing credit card payment...")

# Concrete strategy for PayPal payment
class PayPalPayment(PaymentStrategy):
    def process_payment(self):
        print("Processing PayPal payment...")

# Concrete strategy for crypto payment
class CryptoPayment(PaymentStrategy):
    def process_payment(self):
        print("Processing crypto payment...")

# Concrete strategy for Stripe payment
class StripePayment(PaymentStrategy):
    def process_payment(self):
        print("Processing Stripe payment...")

class PaymentProcessor:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    # Process payment using the current strategy
    def process_payment(self):
        self.payment_strategy.process_payment()

    # Dynamically change payment strategy at runtime
    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

# Main function to simulate payment processing
if __name__ == "__main__":
    # Create strategy instances for each payment type
    credit_card = CreditCardPayment()
    pay_pal = PayPalPayment()
    crypto = CryptoPayment()
    stripe = StripePayment()

    # Use the Strategy Pattern to process payments
    processor = PaymentProcessor(credit_card)  # Initially using CreditCardPayment
    processor.process_payment()  # Processing credit card payment...

    # Dynamically change the payment strategy to PayPal
    processor.set_payment_strategy(pay_pal)
    processor.process_payment()  # Processing PayPal payment...

    # Switch to Crypto
    processor.set_payment_strategy(crypto)
    processor.process_payment()  # Processing crypto payment...

    # Switch to Stripe
    processor.set_payment_strategy(stripe)
    processor.process_payment()  # Processing Stripe payment...
