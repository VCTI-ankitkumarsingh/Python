# Vehicle Rental Management System

## Project overview

This is a console-based Python implementation of the **Vehicle Rental Management System** OOP case study.

The implementation follows the assignment requirements for:
- Vehicle management
- Customer management
- Rental and return workflow
- Late-fee calculation
- Payment abstraction
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism
- Method overriding
- Search
- Composition
- Exception handling

## Main files

### 'vehicle_rental_system.py'
Complete application and CLI.

### 'class_diagram.md'
Class diagram covering inheritance, composition, association, and payment abstraction.

### 'polymorphism_explanation.md'
Short explanation of polymorphism and why it removes vehicle-type conditionals.

### 'discussion_questions_answers.md'
Answers to the discussion questions included in the assignment.

### 'Output.txt'
Captured console output from the complete application and CLI workflow.

## Imports

The application uses only two standard-library modules:

'''python
from abc import ABC, abstractmethod
from datetime import date, timedelta
'''

No external packages are required.

## How to run

'''bash
python vehicle_rental_system.py
'''

The CLI:
1. Starts with registered customers.
2. Asks each customer how many vehicles they want.
3. Shows only vehicle types that still have available vehicles.
4. Shows available vehicles and availability dates.
5. Asks for rental days.
6. Allows Card or UPI payment.
7. Confirms a rental only after payment succeeds.
8. Marks the selected vehicle unavailable.
9. Shows its expected availability date.
10. Requests actual return dates.
11. Calculates late fees.
12. Produces one consolidated final invoice for each customer.
13. Shows rental history and vehicle availability after return.

## Run tests

'''bash
python -m unittest -v
'''

## OOP concepts

### Classes and objects
The core classes are 'Vehicle', 'Car', 'Bike', 'Van', 'Customer', 'Rental', 'Invoice', 'RentalService', and payment classes.

### Encapsulation
State is held in '_private' attributes with controlled access through properties and methods.

### Abstraction
'Vehicle' is an abstract base class and 'PaymentProcessor' defines a common payment contract.

### Inheritance
'Car', 'Bike', and 'Van' inherit from 'Vehicle'.

### Polymorphism
'calculate_rental_cost(days)' behaves differently for Car, Bike, and Van. 'RentalService' calls it through the 'Vehicle' reference, so it does not need a vehicle-type conditional.

### Method overriding
'Car', 'Bike', and 'Van' override 'calculate_rental_cost()', 'vehicle_type()', and 'display_details()'.

### Search / method overloading
Python does not provide Java-style compile-time method overloading by signature. The 'search_vehicles()' method supports multiple search forms using optional parameters: vehicle ID, vehicle type, and price range.

### Composition
A 'Rental' contains references to a 'Customer', 'Vehicle', payment processor, and generated invoice.

### Exception handling
The program handles:
- invalid rental days
- empty required values
- unavailable vehicles
- payment failure
- invalid return dates
- return before rental start
- missing rental IDs

## Business rules implemented

- Rental days must be greater than zero.
- Unavailable vehicles cannot be rented.
- A vehicle cannot be rented by two customers simultaneously.
- Registration number is required.
- Payment must succeed before confirmation.
- Sensitive card information is represented only by masked data.
- Returned vehicles become available again.
- Late fee = late days × 20% × vehicle daily rental rate.

## Van service charge

The assignment requires a van service charge but does not define its amount. The implementation therefore makes the service charge configurable for each 'Van'. The demonstration uses Rs. 500.

## Invoice behavior

A 'Rental' calculates its own final amount on return. A customer's CLI invoice consolidates the base amount, late fees, and final amounts across all vehicles rented by that customer.
