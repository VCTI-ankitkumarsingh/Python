# Vehicle Rental Management System

## Structure

```text
vehicle_rental_management_system/
│
├── main.py
├── input_data.txt
├── README.md
│
└── vehicle_rental/
    ├── __init__.py
    ├── exceptions.py
    ├── payment.py
    ├── vehicle.py
    ├── customer.py
    ├── invoice.py
    ├── rental.py
    ├── service.py
    ├── data_loader.py
    └── cli.py
```

## Input data

Vehicle and customer details are loaded from `input_data.txt`.

The file has two sections:

```text
[VEHICLES]
...
[CUSTOMERS]
...
```

No vehicle or customer records are hard-coded inside `main.py`.

## Run

From the project directory:

```bash
python main.py
```

## Imports

The application uses only Python standard-library modules. No external packages are required.

Core imports are limited to:

```python
from abc import ABC, abstractmethod
from datetime import date, timedelta
from pathlib import Path
```

## Main behavior

- Customers are loaded from `input_data.txt`.
- The CLI asks each customer how many vehicles they want.
- Only currently available vehicle types are shown.
- Booked vehicles are not offered to later customers.
- Negative or zero rental duration is rejected before payment.
- Card and UPI are available as payment choices.
- Payment must succeed before a vehicle is marked rented.
- Each rented vehicle has an expected return date.
- The actual return date is entered through the CLI.
- Invalid return dates cause a retry instead of terminating the application.
- Each late day is charged at the normal daily rental rate plus a 20% late fee.
- The final customer invoice consolidates all rented vehicles.
- Returned vehicles become available again on their actual return date.

## OOP concepts

### Abstraction
`Vehicle` and `PaymentProcessor` define common contracts.

### Inheritance
`Car`, `Bike`, and `Van` inherit from `Vehicle`.

### Polymorphism
Each vehicle implements `calculate_rental_cost()` differently. The rental service calls the method through the common `Vehicle` interface.

### Encapsulation
Important state is kept in internal attributes and accessed through properties and methods.

### Composition
`Rental` works with a `Customer`, `Vehicle`, `PaymentProcessor`, and generated `Invoice`.

### Exception handling
Custom exceptions handle invalid inputs, unavailable vehicles, payment failures, and missing rentals.
