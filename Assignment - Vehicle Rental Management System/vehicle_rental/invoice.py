class Invoice:

    def __init__(
        self,
        rental_id,
        rental_days,
        extra_days,
        base_amount,
        extra_rental_charge,
        late_fee,
        final_amount,
        generated_on
    ):
        self._rental_id = rental_id
        self._rental_days = rental_days
        self._extra_days = extra_days
        self._base_amount = base_amount
        self._extra_rental_charge = extra_rental_charge
        self._late_fee = late_fee
        self._final_amount = final_amount
        self._generated_on = generated_on

    def generate(self):
        return self

    @property
    def rental_id(self):
        return self._rental_id

    @property
    def rental_days(self):
        return self._rental_days

    @property
    def extra_days(self):
        return self._extra_days

    @property
    def base_amount(self):
        return self._base_amount

    @property
    def extra_rental_charge(self):
        return self._extra_rental_charge

    @property
    def late_fee(self):
        return self._late_fee

    @property
    def final_amount(self):
        return self._final_amount

    def display(self):
        print("\n" + "=" * 50)
        print("FINAL INVOICE")
        print("=" * 50)
        print(f"Rental ID        : {self.rental_id}")
        print(f"Invoice Date     : {self._generated_on}")
        print(f"Days Rented      : {self.rental_days}")
        print(f"Extra Days       : {self.extra_days}")
        print(f"Base Amount      : Rs. {self.base_amount:.2f}")
        print(
            f"Extra Day Charge : "
            f"Rs. {self.extra_rental_charge:.2f}"
        )
        print(f"Late Fee         : Rs. {self.late_fee:.2f}")
        print(f"Final Amount     : Rs. {self.final_amount:.2f}")
        print("=" * 50)
