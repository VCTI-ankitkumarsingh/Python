from .exceptions import ValidationError


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
                raise ValidationError(
                    f"{field_name} cannot be empty."
                )

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
                f"{rental.rental_id} | "
                f"{rental.vehicle.vehicle_id} | "
                f"{rental.vehicle.vehicle_type()} | "
                f"Status: {rental.status} | "
                f"Final Amount: Rs. "
                f"{rental.final_amount:.2f}"
            )
