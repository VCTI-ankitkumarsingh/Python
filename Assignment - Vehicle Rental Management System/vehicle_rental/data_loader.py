from .customer import Customer
from .exceptions import ValidationError
from .vehicle import Bike, Car, Van


def _parse_line(line):
    parts = [part.strip() for part in line.split("|")]

    if len(parts) < 1:
        raise ValidationError("Invalid input record.")

    return parts


def load_data(file_path):
    vehicles = []
    customers = []

    section = None

    with open(file_path, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()

            if not line or line.startswith("#"):
                continue

            if line.upper() == "[VEHICLES]":
                section = "vehicles"
                continue

            if line.upper() == "[CUSTOMERS]":
                section = "customers"
                continue

            if section == "vehicles":
                parts = _parse_line(line)

                vehicle_type = parts[0].lower()

                if vehicle_type == "car":
                    if len(parts) != 6:
                        raise ValidationError(
                            "Car record must have 6 fields."
                        )

                    vehicles.append(
                        Car(
                            parts[1],
                            parts[2],
                            parts[3],
                            parts[4],
                            float(parts[5])
                        )
                    )

                elif vehicle_type == "bike":
                    if len(parts) != 6:
                        raise ValidationError(
                            "Bike record must have 6 fields."
                        )

                    vehicles.append(
                        Bike(
                            parts[1],
                            parts[2],
                            parts[3],
                            parts[4],
                            float(parts[5])
                        )
                    )

                elif vehicle_type == "van":
                    if len(parts) != 7:
                        raise ValidationError(
                            "Van record must have 7 fields."
                        )

                    vehicles.append(
                        Van(
                            parts[1],
                            parts[2],
                            parts[3],
                            parts[4],
                            float(parts[5]),
                            float(parts[6])
                        )
                    )

                else:
                    raise ValidationError(
                        f"Unknown vehicle type: {parts[0]}"
                    )

            elif section == "customers":
                parts = _parse_line(line)

                if len(parts) != 4:
                    raise ValidationError(
                        "Customer record must have 4 fields."
                    )

                customers.append(
                    Customer(
                        parts[0],
                        parts[1],
                        parts[2],
                        parts[3]
                    )
                )

            else:
                raise ValidationError(
                    "Input file must contain [VEHICLES] or [CUSTOMERS]."
                )

    return vehicles, customers
