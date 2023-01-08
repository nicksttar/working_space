class Calculator():
    """Calculator Beta made by nicksttar 
    In this code only basic calculator funcions XD"""

    def __init__(self, item1, value, item2):
        # self.item1 = valid(item1)
        self.item1 = int(item1)
        self.value = value
        self.item2 = int(item2)

    def plus(self):
        return str(self.item1 + self.item2)
        
    def minus(self):
        return str(self.item1 - self.item2)

    def xxx(self):
        return str(self.item1 * self.item2)

    def dell(self):
        if self.item1 == 0 and self.item2 == 0:
            return "Zero Division"
        return str(self.item1 / self.item2)
    def percent(self):
        pass
