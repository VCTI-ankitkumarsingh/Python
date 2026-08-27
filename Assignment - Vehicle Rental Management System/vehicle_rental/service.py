from datetime import date, timedelta

from .exceptions import (
    PaymentError,
    RentalNotFoundError,
    ValidationError,
    VehicleUnavailableError,
)
from .rental import Rental


class RentalService:

    def __init__(self):
        self._vehicles = []
        self._customers = []
        self._rentals = []

    def add_vehicle(self, vehicle):
        self._vehicles.append(vehicle)

    def add_customer(self, customer):
        self._customers.append(customer)

    def get_vehicles(self):
        return self._vehicles.copy()

    def get_customers(self):
        return self._customers.copy()

    def display_available_vehicles(self):
        print("\nVehicle Availability")
        print("-" * 100)

        for vehicle in self._vehicles:
            vehicle.display_details()

    def search_vehicles(
        self,
        vehicle_id=None,
        vehicle_type=None,
        min_price=None,
        max_price=None
    ):
        result = []

        for vehicle in self._vehicles:

            if vehicle_id:
                if vehicle.vehicle_id.lower() != vehicle_id.lower():
                    continue

            if vehicle_type:
                if vehicle.vehicle_type().lower() != vehicle_type.lower():
                    continue

            if min_price is not None:
                if vehicle.daily_rate < min_price:
                    continue

            if max_price is not None:
                if vehicle.daily_rate > max_price:
                    continue

            result.append(vehicle)

        return result

    def available_vehicle_types(self):
        types = []

        for vehicle_type in ["car", "bike", "van"]:
            vehicles = self.search_vehicles(
                vehicle_type=vehicle_type
            )

            for vehicle in vehicles:
                if vehicle.available:
                    types.append(vehicle_type)
                    break

        return types

    def rent_vehicle(
        self,
        rental_id,
        customer,
        vehicle,
        days,
        payment_processor,
        start_date=None
    ):
        if days <= 0:
            raise ValidationError(
                "Rental days must be greater than zero."
            )

        if not vehicle.available:
            raise VehicleUnavailableError(
                f"Vehicle {vehicle.vehicle_id} is unavailable."
            )

        amount = vehicle.calculate_rental_cost(days)

        if not payment_processor.process_payment(amount):
            raise PaymentError(
                "Payment failed. Rental was not confirmed."
            )

        rental_start = start_date or date.today()
        expected_return = rental_start + timedelta(days=days)

        rental = Rental(
            rental_id,
            customer,
            vehicle,
            rental_start,
            days,
            payment_processor
        )

        vehicle.mark_as_rented(expected_return)

        self._rentals.append(rental)
        customer.add_rental(rental)

        return rental

    def return_vehicle(self, rental_id, return_date):
        for rental in self._rentals:
            if rental.rental_id == rental_id:
                return rental.complete_rental(return_date)

        raise RentalNotFoundError(
            f"Rental {rental_id} was not found."
        )
