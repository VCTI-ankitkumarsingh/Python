from pathlib import Path

from vehicle_rental.cli import run_cli
from vehicle_rental.data_loader import load_data
from vehicle_rental.exceptions import RentalError
from vehicle_rental.service import RentalService


def main():
    data_file = Path(__file__).parent / "input_data.txt"

    try:
        vehicles, customers = load_data(data_file)
    except (OSError, RentalError, ValueError) as error:
        print(f"Unable to load input data: {error}")
        return

    service = RentalService()

    for vehicle in vehicles:
        service.add_vehicle(vehicle)

    for customer in customers:
        service.add_customer(customer)

    print(f"Loaded vehicles : {len(vehicles)}")
    print(f"Loaded customers: {len(customers)}")

    run_cli(service)


if __name__ == "__main__":
    main()
