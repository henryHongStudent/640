class Product:
    def __init__(self, product_name, productPrice):
        self.__product_name = product_name
        self.__productPrice = productPrice

    @property
    def product_name(self):
        return self.__product_name

    @property
    def productPrice(self):
        return self.__productPrice

    @productPrice.setter
    def productPrice(self, value):
        self.__productPrice = value
    def getPrice(self, quantity):
     return self.__productPrice * quantity
    def __str__(self):
        return f" {self.__product_name}, ${self.__productPrice} "
