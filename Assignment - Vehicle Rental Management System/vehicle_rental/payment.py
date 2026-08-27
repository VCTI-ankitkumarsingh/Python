from abc import ABC, abstractmethod

from .exceptions import PaymentError, ValidationError


class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class CardPayment(PaymentProcessor):

    def __init__(self):
        pass

    def process_payment(self, amount):
        if amount <= 0:
            raise PaymentError("Payment amount must be greater than zero.")

        print(f"Card payment processed for Rs. {amount:.2f}")
        return True


class UPIPayment(PaymentProcessor):

    def __init__(self):
        pass

    def process_payment(self, amount):
        if amount <= 0:
            raise PaymentError("Payment amount must be greater than zero.")

        print(f"UPI payment processed for Rs. {amount:.2f}")
        return True
