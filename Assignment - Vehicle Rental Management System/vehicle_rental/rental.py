from datetime import timedelta

from .exceptions import RentalError, ValidationError
from .invoice import Invoice


class Rental:

    def __init__(
        self,
        rental_id,
        customer,
        vehicle,
        start_date,
        days,
        payment
    ):
        if days <= 0:
            raise ValidationError(
                "Rental days must be greater than zero."
            )

        self._rental_id = rental_id
        self._customer = customer
        self._vehicle = vehicle
        self._start_date = start_date
        self._days = days
        self._expected_return_date = (
            start_date + timedelta(days=days)
        )
        self._actual_return_date = None
        self._base_amount = vehicle.calculate_rental_cost(days)
        self._extra_rental_charge = 0
        self._extra_days = 0
        self._late_fee = 0
        self._final_amount = self._base_amount
        self._payment = payment
        self._invoice = None
        self._status = "Active"

    @property
    def rental_id(self):
        return self._rental_id

    @property
    def customer(self):
        return self._customer

    @property
    def vehicle(self):
        return self._vehicle

    @property
    def days(self):
        return self._days

    @property
    def start_date(self):
        return self._start_date

    @property
    def expected_return_date(self):
        return self._expected_return_date

    @property
    def status(self):
        return self._status

    @property
    def base_amount(self):
        return self._base_amount

    @property
    def extra_days(self):
        return self._extra_days

    @property
    def extra_rental_charge(self):
        return self._extra_rental_charge

    @property
    def late_fee(self):
        return self._late_fee

    @property
    def final_amount(self):
        return self._final_amount

    @property
    def invoice(self):
        return self._invoice

    def calculate_final_amount(self, return_date):
        if return_date < self._start_date:
            raise ValidationError(
                "Return date cannot be before the rental start date."
            )

        self._extra_days = max(
            0,
            (return_date - self._expected_return_date).days
        )

        self._extra_rental_charge = (
            self._extra_days * self.vehicle.daily_rate
        )

        self._late_fee = (
            self._extra_days
            * 0.20
            * self.vehicle.daily_rate
        )

        self._final_amount = (
            self._base_amount
            + self._extra_rental_charge
            + self._late_fee
        )

        return (
            self._extra_rental_charge,
            self._late_fee,
            self._final_amount
        )

    def complete_rental(self, return_date):
        if self._status == "Completed":
            raise RentalError(
                "Rental has already been completed."
            )

        self._actual_return_date = return_date

        self.calculate_final_amount(return_date)

        self._vehicle.mark_as_available(return_date)
        self._status = "Completed"

        self._invoice = Invoice(
            self._rental_id,
            self._days,
            self._extra_days,
            self._base_amount,
            self._extra_rental_charge,
            self._late_fee,
            self._final_amount,
            return_date
        )

        return self._invoice.generate()
