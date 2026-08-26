from abc import ABC, abstractmethod
from datetime import date, timedelta


# ----------------------------
# Custom exceptions
# ----------------------------

class RentalError(Exception):
    pass


class ValidationError(RentalError):
    pass


class VehicleUnavailableError(RentalError):
    pass


class PaymentError(RentalError):
    pass


class RentalNotFoundError(RentalError):
    pass


# ----------------------------
# Payment abstraction
# ----------------------------

class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class CardPayment(PaymentProcessor):
    def __init__(self, masked_card):
        if not masked_card:
            raise ValidationError("Card information is required.")
        self._masked_card = masked_card

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


# ----------------------------
# Vehicle hierarchy
# ----------------------------

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
        self._validate_required(registration_number, "Registration number")
        self._validate_required(brand, "Brand")
        self._validate_required(model, "Model")

        if daily_rate <= 0:
            raise ValidationError("Daily rental rate must be greater than zero.")

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
            raise ValidationError(f"{field_name} cannot be empty.")

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
        if self.available:
            status = "Available"
        else:
            status = "Unavailable"

        print(
            f"{self.vehicle_id} | {self.vehicle_type()} | "
            f"{self.brand} | {self.model} | "
            f"Rs. {self.daily_rate:.2f}/day | {status} | "
            f"Available from: {self._available_from}"
        )

    def mark_as_rented(self, available_from):
        if not self._available:
            raise VehicleUnavailableError(
                f"Vehicle {self.vehicle_id} is already unavailable."
            )
        self._available = False
        self._available_from = available_from

    def mark_as_available(self, available_from=None):
        self._available = True
        self._available_from = available_from or date.today()


class Car(Vehicle):
    def vehicle_type(self):
        return "Car"

    def display_details(self):
        print(
            f"{self.vehicle_id} | Car | {self.brand} | {self.model} | "
            f"Rs. {self.daily_rate:.2f}/day | "
            f"{'Available' if self.available else 'Rented'} | "
            f"Available from: {self.available_from}"
        )

    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValidationError("Rental days must be greater than zero.")
        return self.daily_rate * days


class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"

    def display_details(self):
        print(
            f"{self.vehicle_id} | Bike | {self.brand} | {self.model} | "
            f"Rs. {self.daily_rate:.2f}/day | "
            f"{'Available' if self.available else 'Rented'} | "
            f"Available from: {self.available_from}"
        )

    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValidationError("Rental days must be greater than zero.")

        amount = self.daily_rate * days

        if days > 5:
            amount *= 0.95

        return amount


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
            raise ValidationError("Service charge cannot be negative.")

        self._service_charge = service_charge

    @property
    def service_charge(self):
        return self._service_charge

    def vehicle_type(self):
        return "Van"

    def display_details(self):
        print(
            f"{self.vehicle_id} | Van | {self.brand} | {self.model} | "
            f"Rs. {self.daily_rate:.2f}/day | "
            f"{'Available' if self.available else 'Rented'} | "
            f"Available from: {self.available_from}"
        )

    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValidationError("Rental days must be greater than zero.")

        return (self.daily_rate * days) + self.service_charge


# ----------------------------
# Customer
# ----------------------------

class Customer:
    def __init__(
        self,
        customer_id,
        name,
        email,
        licence_number
    ):
        for value, field_name in [
            (customer_id, "Customer ID"),
            (name, "Name"),
            (email, "Email"),
            (licence_number, "Driving licence number")
        ]:
            if not value or not value.strip():
                raise ValidationError(f"{field_name} cannot be empty.")

        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._licence_number = licence_number
        self._rental_history = []

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def licence_number(self):
        return self._licence_number

    @property
    def rental_history(self):
        return self._rental_history.copy()

    def add_rental(self, rental):
        self._rental_history.append(rental)

    def display_rental_history(self):
        print(f"\nRental History - {self.name}")
        print("-" * 70)

        if not self._rental_history:
            print("No rentals found.")
            return

        for rental in self._rental_history:
            print(
                f"{rental.rental_id} | {rental.vehicle.vehicle_id} | "
                f"{rental.vehicle.vehicle_type()} | "
                f"Status: {rental.status} | "
                f"Final Amount: Rs. {rental.final_amount:.2f}"
            )


# ----------------------------
# Invoice
# ----------------------------

class Invoice:
    def __init__(self, rental_id, base_amount, late_fee, final_amount, generated_on):
        self._rental_id = rental_id
        self._base_amount = base_amount
        self._late_fee = late_fee
        self._final_amount = final_amount
        self._generated_on = generated_on

    def generate(self):
        return self

    @property
    def rental_id(self):
        return self._rental_id

    @property
    def base_amount(self):
        return self._base_amount

    @property
    def late_fee(self):
        return self._late_fee

    @property
    def final_amount(self):
        return self._final_amount

    def display(self):
        print("\n" + "=" * 50)
        print("FINAL INVOICE")
        print("=" * 50)
        print(f"Rental ID      : {self.rental_id}")
        print(f"Invoice Date   : {self._generated_on}")
        print(f"Base Amount    : Rs. {self.base_amount:.2f}")
        print(f"Late Fee       : Rs. {self.late_fee:.2f}")
        print(f"Final Amount   : Rs. {self.final_amount:.2f}")
        print("=" * 50)


# ----------------------------
# Rental
# ----------------------------

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
            raise ValidationError("Rental days must be greater than zero.")

        self._rental_id = rental_id
        self._customer = customer
        self._vehicle = vehicle
        self._start_date = start_date
        self._days = days
        self._expected_return_date = start_date + timedelta(days=days)
        self._actual_return_date = None
        self._base_amount = vehicle.calculate_rental_cost(days)
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
            raise ValidationError("Return date cannot be before rental start date.")

        late_days = max(
            0,
            (return_date - self._expected_return_date).days
        )

        late_fee = late_days * 0.20 * self.vehicle.daily_rate
        final_amount = self._base_amount + late_fee

        return late_fee, final_amount

    def complete_rental(self, return_date):
        if self._status == "Completed":
            raise RentalError("Rental has already been completed.")

        self._actual_return_date = return_date
        self._late_fee, self._final_amount = self.calculate_final_amount(return_date)

        self._vehicle.mark_as_available(return_date)
        self._status = "Completed"

        self._invoice = Invoice(
            self.rental_id,
            self._base_amount,
            self._late_fee,
            self._final_amount,
            return_date
        )

        return self._invoice.generate()


# ----------------------------
# Rental service
# ----------------------------

class RentalService:
    def __init__(self):
        self._vehicles = []
        self._customers = []
        self._rentals = []

    def add_vehicle(self, vehicle):
        self._vehicles.append(vehicle)

    def add_customer(self, customer):
        self._customers.append(customer)

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
            if vehicle_id and vehicle.vehicle_id.lower() != vehicle_id.lower():
                continue

            if vehicle_type and vehicle.vehicle_type().lower() != vehicle_type.lower():
                continue

            if min_price is not None and vehicle.daily_rate < min_price:
                continue

            if max_price is not None and vehicle.daily_rate > max_price:
                continue

            result.append(vehicle)

        return result

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
            raise ValidationError("Rental days must be greater than zero.")

        if not vehicle.available:
            raise VehicleUnavailableError(
                f"Vehicle {vehicle.vehicle_id} is unavailable."
            )

        amount = vehicle.calculate_rental_cost(days)

        payment_success = payment_processor.process_payment(amount)

        if not payment_success:
            raise PaymentError("Payment failed. Rental was not confirmed.")

        rental_start_date = start_date or date.today()
        expected_return_date = rental_start_date + timedelta(days=days)

        vehicle.mark_as_rented(expected_return_date)

        rental = Rental(
            rental_id,
            customer,
            vehicle,
            rental_start_date,
            days,
            payment_processor
        )

        self._rentals.append(rental)
        customer.add_rental(rental)

        return rental

    def return_vehicle(self, rental_id, return_date):
        for rental in self._rentals:
            if rental.rental_id == rental_id:
                return rental.complete_rental(return_date)

        raise RentalNotFoundError(f"Rental {rental_id} was not found.")


# ----------------------------
# CLI / Demonstration
# ----------------------------

def select_vehicle(service):
    while True:
        available_types = []

        for vehicle_type in ["car", "bike", "van"]:
            vehicles = service.search_vehicles(vehicle_type=vehicle_type)
            if any(vehicle.available for vehicle in vehicles):
                available_types.append(vehicle_type)

        if not available_types:
            print("No vehicles are currently available.")
            return None

        print("\nAvailable Vehicle Types")
        print("-" * 40)

        for i, vehicle_type in enumerate(available_types, 1):
            print(f"{i}. {vehicle_type.title()}")

        try:
            type_choice = int(input("Select vehicle type: "))
            if not 1 <= type_choice <= len(available_types):
                print("Invalid vehicle type selection.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        vehicle_type = available_types[type_choice - 1]
        vehicles = service.search_vehicles(vehicle_type=vehicle_type)
        available_vehicles = [v for v in vehicles if v.available]

        # Normally this cannot become empty between the checks above, but
        # keeping the check makes the CLI safe if the state changes.
        if not available_vehicles:
            print(f"No {vehicle_type.title()} is currently available.")
            print("Please select another vehicle type.")
            continue

        print(f"\nAvailable {vehicle_type.title()}s")
        print("-" * 70)

        for i, vehicle in enumerate(available_vehicles, 1):
            print(
                f"{i}. {vehicle.vehicle_id} | "
                f"{vehicle.brand} {vehicle.model} | "
                f"Rs. {vehicle.daily_rate:.2f}/day | "
                f"Available from: {vehicle.available_from}"
            )

        try:
            choice = int(input("Select vehicle: "))
            if 1 <= choice <= len(available_vehicles):
                return available_vehicles[choice - 1]
            print("Invalid vehicle selection.")
        except ValueError:
            print("Please enter a valid number.")


def select_payment():
    while True:
        print("\nPayment Method")
        print("1. Card")
        print("2. UPI")
        choice = input("Select payment method: ").strip()

        if choice == "1":
            return CardPayment("**** **** **** 1234")

        if choice == "2":
            return UPIPayment()

        print("Invalid payment method.")


def rent_for_customer(service, customer, rental_number):
    print("\n" + "=" * 60)
    print(f"Rental for: {customer.name}")
    print("=" * 60)

    while True:
        vehicle = select_vehicle(service)
        if vehicle is None:
            return None

        try:
            # Rental duration must be a positive whole number.
            while True:
                try:
                    days = int(input("Enter rental days: "))

                    if days <= 0:
                        print(
                            "Rental days must be greater than zero. "
                            "Please enter a positive number."
                        )
                        continue

                    break

                except ValueError:
                    print(
                        "Invalid input. Rental days must be a "
                        "positive whole number."
                    )

            payment = select_payment()
            rental_id = f"R{rental_number:03d}"

            rental = service.rent_vehicle(
                rental_id,
                customer,
                vehicle,
                days,
                payment
            )

            print("\nRental confirmed successfully.")
            print(f"Customer : {customer.name}")
            print(f"Vehicle  : {vehicle.vehicle_id}")
            print(f"Type     : {vehicle.vehicle_type()}")
            print(f"Days     : {days}")
            print(f"Amount   : Rs. {rental.base_amount:.2f}")
            print(f"Available again from: {rental.expected_return_date}")
            return rental

        except (ValidationError, VehicleUnavailableError, PaymentError) as error:
            print(f"\nRental failed: {error}")
            print("Please try again.")


def parse_date(date_text):
    date_text = date_text.strip()

    # Require exactly YYYY-MM-DD.
    parts = date_text.split("-")

    if len(parts) != 3:
        raise ValidationError(
            "Invalid date. Please use YYYY-MM-DD format."
        )

    if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        raise ValidationError(
            "Invalid date. Please use YYYY-MM-DD format."
        )

    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        return date(year, month, day)

    except ValueError:
        raise ValidationError(
            "Invalid date. Please enter a real date in YYYY-MM-DD format."
        )


def cli_demo():
    service = RentalService()

    # ----------------------------
    # Add vehicles
    # ----------------------------
    car1 = Car("V101", "MH12AB1234", "Toyota", "Camry", 2000)
    car2 = Car("V104", "MH12GH3456", "Honda", "City", 1800)

    bike1 = Bike("V102", "MH12CD5678", "Yamaha", "FZ", 700)
    bike2 = Bike("V105", "MH12JK7890", "Honda", "Shine", 600)

    van1 = Van("V103", "MH12EF9012", "Tata", "Winger", 3000, 500)

    service.add_vehicle(car1)
    service.add_vehicle(car2)
    service.add_vehicle(bike1)
    service.add_vehicle(bike2)
    service.add_vehicle(van1)

    # ----------------------------
    # Add customers
    # ----------------------------
    customers = [
            Customer(
                "C101",
                "Ankit Singh",
                "ankit@example.com",
                "DL-101"
            ),
            Customer(
                "C102",
                "Shahbaz Athar",
                "shahbaz@example.com",
                "DL-102"
            ),
            Customer(
                "C103",
                "Ashish Tandi",
                "ashish@example.com",
                "DL-103"
            )
    ]

    for customer in customers:
        service.add_customer(customer)

    rental_counter = 1

    # ----------------------------
    # Ask each customer how many
    # vehicles they want
    # ----------------------------
    for customer in customers:

        print("\n" + "=" * 60)
        print(f"Customer: {customer.name}")
        print("=" * 60)

        while True:
            available_count = 0

            for vehicle_type in ["car", "bike", "van"]:
                for vehicle in service.search_vehicles(
                    vehicle_type=vehicle_type
                ):
                    if vehicle.available:
                        available_count += 1

            if available_count == 0:
                print("No vehicles are currently available.")
                break

            try:
                vehicle_count = int(
                    input(
                        f"How many vehicles do you want to rent "
                        f"(1-{available_count})? "
                    )
                )

                if vehicle_count < 1 or vehicle_count > available_count:
                    print(
                        f"Please enter a number between "
                        f"1 and {available_count}."
                    )
                    continue

                break

            except ValueError:
                print("Please enter a valid number.")

        # Customer now selects vehicles one by one.
        for selection in range(vehicle_count):

            print(
                f"\nVehicle {selection + 1} of "
                f"{vehicle_count} for {customer.name}"
            )

            rental = rent_for_customer(
                service,
                customer,
                rental_counter
            )

            if rental is not None:
                rental_counter += 1

    # ----------------------------
    # Return all vehicles and
    # create one final invoice
    # per customer
    # ----------------------------
    print("\n" + "=" * 60)
    print("RETURN VEHICLES / FINAL INVOICES")
    print("=" * 60)

    for customer in customers:

        if not customer.rental_history:
            continue

        total_base = 0
        total_late_fee = 0
        total_final = 0

        for rental in customer.rental_history:

            if rental.status != "Active":
                continue

            print(f"Customer Name   : {customer.name}")
            print(
                f"Vehicle         : {rental.vehicle.vehicle_id} - "
                f"{rental.vehicle.brand} {rental.vehicle.model} "
                f"({rental.vehicle.vehicle_type()})"
            )
            print(f"Rental Start    : {rental.start_date}")
            print(f"Expected return : {rental.expected_return_date}")

            while True:
                return_date_text = input(
                    "Enter actual return date (YYYY-MM-DD): "
                ).strip()

                try:
                    return_date = parse_date(return_date_text)

                    if return_date < rental.start_date:
                        print(
                            "Return date cannot be before the rental start date."
                        )
                        continue

                    break

                except ValidationError as error:
                    print(f"Invalid input: {error}")
                    print("Please try again.")

            invoice = service.return_vehicle(
                rental.rental_id,
                return_date
            )

            total_base += invoice.base_amount
            total_late_fee += invoice.late_fee
            total_final += invoice.final_amount

        print("\n" + "-" * 60)
        print("CUSTOMER FINAL INVOICE")
        print("-" * 60)
        print(f"Customer ID    : {customer.customer_id}")
        print(f"Customer Name  : {customer.name}")
        print(f"Vehicles rented: {len(customer.rental_history)}")
        print(f"Base amount    : Rs. {total_base:.2f}")
        print(f"Late fee       : Rs. {total_late_fee:.2f}")
        print(f"Final amount   : Rs. {total_final:.2f}")
        print("-" * 60)

    # ----------------------------
    # Vehicles available after
    # all returns
    # ----------------------------
    print("\n" + "=" * 60)
    print("VEHICLE STATUS AFTER RETURNS")
    print("=" * 60)

    service.display_available_vehicles()

    # ----------------------------
    # Rental histories
    # ----------------------------
    for customer in customers:
        customer.display_rental_history()


if __name__ == "__main__":
    cli_demo()
