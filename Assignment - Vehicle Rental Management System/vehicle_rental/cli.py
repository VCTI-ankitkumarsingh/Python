from datetime import date

from .exceptions import (
    PaymentError,
    ValidationError,
    VehicleUnavailableError,
)
from .payment import CardPayment, UPIPayment


def select_vehicle_type(service):
    while True:
        available_types = service.available_vehicle_types()

        if not available_types:
            print("No vehicles are currently available.")
            return None

        print("\nAvailable Vehicle Types")
        print("-" * 40)

        for index, vehicle_type in enumerate(available_types, 1):
            print(f"{index}. {vehicle_type.title()}")

        try:
            choice = int(input("Select vehicle type: "))

            if 1 <= choice <= len(available_types):
                return available_types[choice - 1]

            print("Invalid vehicle type selection.")

        except ValueError:
            print("Please enter a valid number.")


def select_vehicle(service):
    while True:
        vehicle_type = select_vehicle_type(service)

        if vehicle_type is None:
            return None

        vehicles = service.search_vehicles(
            vehicle_type=vehicle_type
        )

        available_vehicles = [
            vehicle for vehicle in vehicles
            if vehicle.available
        ]

        if not available_vehicles:
            print(
                f"No {vehicle_type.title()} is currently available."
            )
            print("Please select another vehicle type.")
            continue

        print(f"\nAvailable {vehicle_type.title()}s")
        print("-" * 70)

        for index, vehicle in enumerate(
            available_vehicles,
            1
        ):
            print(
                f"{index}. {vehicle.vehicle_id} | "
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
            return CardPayment()

        if choice == "2":
            return UPIPayment()

        print("Invalid payment method.")


def read_positive_days():
    while True:
        try:
            days = int(input("Enter rental days: "))

            if days <= 0:
                print(
                    "Rental days must be greater than zero. "
                    "Please enter a positive number."
                )
                continue

            return days

        except ValueError:
            print(
                "Invalid input. Rental days must be a "
                "positive whole number."
            )


def rent_for_customer(service, customer, rental_number):
    print("\n" + "=" * 60)
    print(f"Rental for: {customer.name}")
    print("=" * 60)

    while True:
        vehicle = select_vehicle(service)

        if vehicle is None:
            return None

        days = read_positive_days()
        payment = select_payment()
        rental_id = f"R{rental_number:03d}"

        try:
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
            print(
                f"Amount   : Rs. "
                f"{rental.base_amount:.2f}"
            )
            print(
                f"Available again from: "
                f"{rental.expected_return_date}"
            )

            return rental

        except (
            ValidationError,
            VehicleUnavailableError,
            PaymentError,
        ) as error:
            print(f"\nRental failed: {error}")
            print("Please try again.")


def parse_date(date_text):
    parts = date_text.strip().split("-")

    if len(parts) != 3:
        raise ValidationError(
            "Invalid date. Please use YYYY-MM-DD format."
        )

    if (
        len(parts[0]) != 4
        or len(parts[1]) != 2
        or len(parts[2]) != 2
    ):
        raise ValidationError(
            "Invalid date. Please use YYYY-MM-DD format."
        )

    try:
        return date(
            int(parts[0]),
            int(parts[1]),
            int(parts[2])
        )

    except ValueError:
        raise ValidationError(
            "Invalid date. Please enter a real date "
            "in YYYY-MM-DD format."
        )


def return_all_customer_vehicles(service, customers):
    print("\n" + "=" * 60)
    print("RETURN VEHICLES / FINAL INVOICES")
    print("=" * 60)

    for customer in customers:
        if not customer.rental_history:
            continue

        total_base = 0
        total_extra = 0
        total_late = 0
        total_final = 0
        total_days = 0
        total_extra_days = 0

        for rental in customer.rental_history:

            if rental.status != "Active":
                continue

            print(f"\nCustomer Name   : {customer.name}")
            print(
                f"Vehicle         : "
                f"{rental.vehicle.vehicle_id} - "
                f"{rental.vehicle.brand} "
                f"{rental.vehicle.model} "
                f"({rental.vehicle.vehicle_type()})"
            )
            print(f"Rental Start    : {rental.start_date}")
            print(
                f"Expected return : "
                f"{rental.expected_return_date}"
            )

            while True:
                return_text = input(
                    "Enter actual return date (YYYY-MM-DD): "
                )

                try:
                    return_date = parse_date(return_text)

                    if return_date < rental.start_date:
                        print(
                            "Return date cannot be before "
                            "the rental start date."
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
            total_extra += invoice.extra_rental_charge
            total_late += invoice.late_fee
            total_final += invoice.final_amount
            total_days += invoice.rental_days
            total_extra_days += invoice.extra_days

        print("\n" + "-" * 60)
        print("CUSTOMER FINAL INVOICE")
        print("-" * 60)
        print(
            f"Customer ID     : "
            f"{customer.customer_id}"
        )
        print(
            f"Customer Name   : "
            f"{customer.name}"
        )
        print(
            f"Vehicles rented : "
            f"{len(customer.rental_history)}"
        )
        print(f"Days rented     : {total_days}")
        print(f"Extra days      : {total_extra_days}")
        print(
            f"Base amount     : "
            f"Rs. {total_base:.2f}"
        )
        print(
            f"Extra day charge: "
            f"Rs. {total_extra:.2f}"
        )
        print(
            f"Late fee        : "
            f"Rs. {total_late:.2f}"
        )
        print(
            f"Final amount    : "
            f"Rs. {total_final:.2f}"
        )
        print("-" * 60)


def run_cli(service):
    customers = service.get_customers()
    rental_counter = 1

    print("\n" + "=" * 60)
    print("VEHICLE RENTAL MANAGEMENT SYSTEM")
    print("=" * 60)

    for customer in customers:
        print("\n" + "=" * 60)
        print(f"Customer: {customer.name}")
        print("=" * 60)

        available_count = 0
        for vehicle in service.get_vehicles():
            if vehicle.available:
                available_count += 1

        if available_count == 0:
            print("No vehicles are currently available.")
            continue

        while True:
            try:
                vehicle_count = int(
                    input(
                        f"How many vehicles do you want to rent "
                        f"(1-{available_count})? "
                    )
                )

                if 1 <= vehicle_count <= available_count:
                    break

                print(
                    f"Please enter a number between "
                    f"1 and {available_count}."
                )

            except ValueError:
                print("Please enter a valid number.")

        selection = 1

        while selection <= vehicle_count:
            print(
                f"\nVehicle {selection} of "
                f"{vehicle_count} for {customer.name}"
            )

            rental = rent_for_customer(
                service,
                customer,
                rental_counter
            )

            if rental is not None:
                rental_counter += 1
                selection += 1
            else:
                break

    return_all_customer_vehicles(
        service,
        customers
    )

    print("\n" + "=" * 60)
    print("VEHICLE STATUS AFTER RETURNS")
    print("=" * 60)

    service.display_available_vehicles()

    for customer in customers:
        customer.display_rental_history()
