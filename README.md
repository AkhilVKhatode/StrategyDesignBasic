# Payment Strategy Pattern Implementation in Python

This project demonstrates the implementation of the **Strategy Pattern** in Python for processing different types of payments. The Strategy Pattern allows an object to change its behavior at runtime based on the selected strategy, in this case, different payment methods.

## Overview

The program defines a `PaymentStrategy` interface and several concrete strategies for different payment types:
- **Credit Card Payment**
- **PayPal Payment**
- **Crypto Payment**
- **Stripe Payment**

The payment processing logic is encapsulated in the `PaymentProcessor` class, which can dynamically switch between different payment strategies.

## How it Works

1. **PaymentStrategy Interface**: Defines the common interface (`process_payment`) that all payment strategies must implement.
2. **Concrete Payment Strategies**: Implements the `process_payment` method for various payment types like Credit Card, PayPal, Crypto, and Stripe.
3. **PaymentProcessor**: Uses a `PaymentStrategy` to process payments. It allows changing the payment strategy at runtime.

## Usage

The example code demonstrates how to use the `PaymentProcessor` class to process different types of payments:

```python
from payment_processor import PaymentProcessor, CreditCardPayment, PayPalPayment, CryptoPayment, StripePayment

# Create strategy instances for each payment type
credit_card = CreditCardPayment()
pay_pal = PayPalPayment()
crypto = CryptoPayment()
stripe = StripePayment()

# Use the Strategy Pattern to process payments
processor = PaymentProcessor(credit_card)
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
```
