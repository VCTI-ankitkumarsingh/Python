# Discussion Questions

## 1. Why should Vehicle be abstract?

'Vehicle' represents the common state and behavior shared by 'Car', 'Bike', and 'Van', but each vehicle type has its own rental-cost rule. Making 'Vehicle' abstract ensures that only concrete vehicle types are instantiated and that each subclass provides the required rental-cost behavior.

## 2. How does polymorphism remove vehicle-type conditionals?

'RentalService' calls 'vehicle.calculate_rental_cost(days)'. The appropriate implementation is selected based on the actual vehicle object, so 'RentalService' does not need separate 'if/elif' conditions for Car, Bike, and Van.

## 3. Why should vehicle and customer fields remain private?

Private/internal fields prevent uncontrolled changes to important business data. Properties and methods provide controlled access and allow validation to remain inside the appropriate class.

## 4. What is the relationship between Rental, Customer, and Vehicle?

A 'Rental' contains references to a 'Customer' and a 'Vehicle'. A 'Customer' can have multiple 'Rental' records over time, representing their rental history.

## 5. How can a new vehicle type be added without changing existing classes?

A new vehicle type can be created as a subclass of 'Vehicle'. It implements the required abstract methods and provides its own rental-cost rule. The existing rental calculation logic does not need to be changed.

## 6. What should happen when payment processing fails?

The rental must not be confirmed, and the vehicle must remain available. A 'PaymentError' should be raised or handled, and the vehicle should only be marked as rented after successful payment.

## 7. Which parts demonstrate composition?

'Rental' brings together a 'Customer', 'Vehicle', 'PaymentProcessor', and 'Invoice'. These objects work together as part of a rental record, demonstrating composition.

## 8. How would the model change if one booking could contain multiple vehicles?

A booking would contain a collection of vehicles or rental items instead of a single vehicle reference. The booking could then calculate the combined rental cost, late fees, and final amount for all vehicles, while the customer would maintain the booking in their history.
