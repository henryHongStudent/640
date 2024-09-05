class Order:
    # 클래스 변수

    nextID = 10000

    def __init__(self, customer, orderDate):
        self._customer = customer
        self._orderDate = orderDate
        self._orderID = Order.nextID  # 클래스 변수에서 ID를 가져옴
        self._prodList = []
        self._totalPrice =0
        Order.nextID += 1


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
    def getTotalPrice(self,totalPrice):
        self._totalPrice += totalPrice
        return self._totalPrice
        
    def __str__(self):
        order_items_str = ', '.join(str(item) for item in self._prodList)
        return (f"Order ID: {self._orderID}, "
                f"Customer: {self._customer}, "
                f"Date: {self._orderDate}, "
                f"Products: {order_items_str}, "
                f"Total Price: {self._totalPrice} \n"
                )