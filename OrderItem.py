class OrderItem:
    def __init__(self, quantity, product):
        self._quantity = quantity
        self._product = product

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def product(self):
        return self._product

    def __str__(self):
        return f"Quantity: {self._quantity}, Product: {self._product}"

