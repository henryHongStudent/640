class Product:
    def __init__(self, product_name, productPrice):
        self._product_name = product_name
        self._productPrice = productPrice

    @property
    def product_name(self):
        return self._product_name

    @property
    def productPrice(self):
        return self._productPrice

    @productPrice.setter
    def productPrice(self, value):
        self._productPrice = value

    def __str__(self):
        return f" {self._product_name}"
