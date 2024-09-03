class Customer:

    customerId_counter = 1000  

    def __init__(self, customer_name):
        self.__customerID = Customer.customerId_counter
        self.__customer_name = customer_name
        self.__customerBalance = []
        self.__payment = []
        Customer.customerId_counter += 1
    

    @property
    def customerId(self):
        return self.__customerID

    @property
    def customer_name(self):
        return self.__customer_name

    @property
    def customerBalance(self):
        return self.__customerBalance

    @customerBalance.setter
    def customerBalance(self, value):
        self.__customerBalance = value

    @property
    def payment(self):
        return self.__payment

    @payment.setter
    def payment(self, value):
        self.___payment = value
    def addCustomerBalance(self, payment):
        self.__customerBalance.append(payment)
  

    
    def __str__(self):
        return (f"=========================\n"
                f"ID: {self.__customerID}\n"
                f"Customer Name: {self.__customer_name}\n"
                f"Balance: {self.__customerBalance}\n"
                f"=========================\n")

