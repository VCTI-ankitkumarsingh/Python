from abc import ABC, abstractmethod
from datetime import date

from .exceptions import ValidationError, VehicleUnavailableError


class Vehicle(ABC):

    def __init__(
        self,
        vehicle_id,
        registration_number,
        brand,
        model,
        daily_rate
    ):
        self._validate_required(vehicle_id, "Vehicle ID")
        self._validate_required(
            registration_number,
            "Registration number"
        )
        self._validate_required(brand, "Brand")
        self._validate_required(model, "Model")

        if daily_rate <= 0:
            raise ValidationError(
                "Daily rental rate must be greater than zero."
            )

        self._vehicle_id = vehicle_id
        self._registration_number = registration_number
        self._brand = brand
        self._model = model
        self._daily_rate = daily_rate
        self._available = True
        self._available_from = date.today()

    @staticmethod
    def _validate_required(value, field_name):
        if not value or not value.strip():
            raise ValidationError(
                f"{field_name} cannot be empty."
            )

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @property
    def registration_number(self):
        return self._registration_number

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def daily_rate(self):
        return self._daily_rate

    @property
    def available(self):
        # A vehicle is considered available only from its availability date.
        return self._available and date.today() >= self._available_from

    @property
    def available_from(self):
        return self._available_from

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

    @abstractmethod
    def vehicle_type(self):
        pass

    def display_details(self):
        status = "Available" if self.available else "Unavailable"

        print(
            f"{self.vehicle_id} | {self.vehicle_type()} | "
            f"{self.brand} | {self.model} | "
            f"Rs. {self.daily_rate:.2f}/day | {status} | "
            f"Available from: {self._available_from}"
        )

    def mark_as_rented(self, available_from):
        if not self.available:
            raise VehicleUnavailableError(
                f"Vehicle {self.vehicle_id} is unavailable."
            )

        self._available = False
        self._available_from = available_from

    def mark_as_available(self, available_from=None):
        self._available = True
        self._available_from = available_from or date.today()


class Car(Vehicle):

    def vehicle_type(self):
        return "Car"

    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValidationError(
                "Rental days must be greater than zero."
            )

        return self.daily_rate * days

    def display_details(self):
        super().display_details()


class Bike(Vehicle):

    def vehicle_type(self):
        return "Bike"

    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValidationError(
                "Rental days must be greater than zero."
            )

        amount = self.daily_rate * days

        if days > 5:
            amount *= 0.95

        return amount

    def display_details(self):
        super().display_details()


class Van(Vehicle):

    def __init__(
        self,
        vehicle_id,
        registration_number,
        brand,
        model,
        daily_rate,
        service_charge
    ):
        super().__init__(
            vehicle_id,
            registration_number,
            brand,
            model,
            daily_rate
        )

        if service_charge < 0:
            raise ValidationError(
                "Service charge cannot be negative."
            )

        self._service_charge = service_charge

    @property
    def service_charge(self):
        return self._service_charge

    def vehicle_type(self):
        return "Van"

    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValidationError(
                "Rental days must be greater than zero."
            )

        return (
            self.daily_rate * days
            + self.service_charge
        )

    def display_details(self):
        super().display_details()
