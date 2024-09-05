class Customer:

    customerId_counter = 1000  

    def __init__(self, customer_name):
        self.__customerID = Customer.customerId_counter
        self.__customer_name = customer_name
        self.__customerBalance = 0
        self.__payment = []
        self.__updates = []
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
        self.balanceUpdate()

    @property
    def payment(self):
        return self.__payment

    @payment.setter
    def payment(self, value):
        self.__payment = value
        self.customerBalance -= value.payment

    def addCustomerBalance(self, payment):
        self.__customerBalance += payment
        self.balanceUpdate()

    def deleteCustomerBalance(self, payment):
        balance = self.__customerBalance
        if balance == 0:
            return "No balance."
        elif balance < payment:
            return "payment amount exceeds the current balance."
        elif balance >= payment:
            self.__customerBalance -= payment
            self.balanceUpdate()
            return f"Payment of ${payment} processed successfully."
       

    def addPayment(self, payment):
        self.__payment.append(payment)
        print(f"{payment} has been added to the payment list.")

    def addUpdate(self, update):
        self.__updates.append(update)

    def balanceUpdate(self):
        for update in self.__updates:
            update(self)

    def __str__(self):
        return (f"=========================\n"
                f"ID: {self.__customerID}\n"
                f"Customer Name: {self.__customer_name}\n"
                f"Balance: ${self.__customerBalance:.2f}\n"
                f"=========================\n")
