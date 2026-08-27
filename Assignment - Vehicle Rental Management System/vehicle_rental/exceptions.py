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
