# Polymorphism Explanation

## Where polymorphism is used

The main polymorphic method is:

'''python
vehicle.calculate_rental_cost(days)
'''

'Vehicle' declares the method as abstract.

'Car', 'Bike', and 'Van' each override it:

'''text
Car  -> daily rate × days
Bike -> daily rate × days, with 5% discount after five days
Van  -> daily rate × days + service charge
'''

'RentalService.rent_vehicle()' receives a 'Vehicle' reference and simply calls:

'''python
amount = vehicle.calculate_rental_cost(days)
'''

There is no code such as:

'''python
if vehicle.vehicle_type() == "Car":
    ...
elif vehicle.vehicle_type() == "Bike":
    ...
elif vehicle.vehicle_type() == "Van":
    ...
'''

## Why this improves the design

The rental calculation responsibility remains inside each vehicle class.

If a new vehicle type such as 'ElectricCar' is added, it can inherit from 'Vehicle' and implement 'calculate_rental_cost()' without changing the existing rental calculation code.

This follows the assignment's design expectation that rental calculations should be selected through polymorphism instead of long vehicle-type conditional blocks.
