class Order:
    orderID = 1
    nextID = 1

    def __init__(self, customer, orderDate):
        self._customer = customer
        self._orderDate = orderDate
        self._orderID = Order.orderID
        self._prodList = []
        Order.nextID += 1
        Order.orderID += 1

    @property
    def customer(self):
        return self._customer


    @property
    def orderDate(self):
        return self._orderDate

    @orderDate.setter
    def orderDate(self, value):
        self._orderDate = value

    @property
    def orderID(self):
        return self._orderID

    @property
    def prodList(self):
        return self._prodList

    def addProdList(self, orderItem):
        self._prodList.append(orderItem)

    def __str__(self):
        order_items_str = ', '.join(str(item) for item in self._prodList)
        return f"Order ID: {self._orderID}, Customer: {self._customer}, Date: {self._orderDate}, Product: [{order_items_str}]"


