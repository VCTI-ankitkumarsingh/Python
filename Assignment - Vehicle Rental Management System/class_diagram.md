# Class Diagram

'''
classDiagram

class Vehicle {
    <<abstract>>
    -vehicle_id
    -registration_number
    -brand
    -model
    -daily_rate
    -available
    -available_from
    +calculate_rental_cost(days)*
    +vehicle_type()*
    +display_details()
    +mark_as_rented(available_from)
    +mark_as_available(available_from)
}

class Car
class Bike
class Van {
    -service_charge
}

Vehicle <|-- Car
Vehicle <|-- Bike
Vehicle <|-- Van

class Customer {
    -customer_id
    -name
    -email
    -licence_number
    -rental_history
    +add_rental()
    +display_rental_history()
}

class PaymentProcessor {
    <<interface>>
    +process_payment(amount)*
}

class CardPayment
class UPIPayment

PaymentProcessor <|.. CardPayment
PaymentProcessor <|.. UPIPayment

class Rental {
    -rental_id
    -customer
    -vehicle
    -start_date
    -expected_return_date
    -actual_return_date
    -days
    -base_amount
    -late_fee
    -final_amount
    -payment
    -invoice
    -status
    +calculate_final_amount(return_date)
    +complete_rental(return_date)
}

class Invoice {
    -rental_id
    -base_amount
    -late_fee
    -final_amount
    -generated_on
    +generate()
    +display()
}

class RentalService {
    -vehicles
    -customers
    -rentals
    +add_vehicle()
    +add_customer()
    +search_vehicles()
    +rent_vehicle()
    +return_vehicle()
}

Rental --> Customer : contains
Rental --> Vehicle : contains
Rental --> PaymentProcessor : uses
Rental --> Invoice : creates
Customer "1" --> "0..*" Rental : rental history
RentalService --> Vehicle : manages
RentalService --> Customer : manages
RentalService --> Rental : manages
'''
