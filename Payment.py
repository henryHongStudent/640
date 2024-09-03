class Payment:
    def __init__(self, paymentDate, paymentAmount):
        self._paymentDate = paymentDate
        self._paymentAmount = paymentAmount

    @property
    def paymentDate(self):
        return self._paymentDate

    @paymentDate.setter
    def paymentDate(self, value):
        self._paymentDate = value

    @property
    def paymentAmount(self):
        return self._paymentAmount

    @paymentAmount.setter
    def paymentAmount(self, value):
        self._paymentAmount = value

    def __str__(self):
        return f"Payment Date: {self._paymentDate}, Payment Amount: {self._paymentAmount}"

