'Goods classes'

class Good:
    'Main class Good for all goods'
    def __init__(self, price):
        if price > 0:
            self._price = price
        else:
            raise ValueError
        self.discounted_price = price

    @property
    def price(self):
        'Set price for any good'
        print("{} price: {}".format(self.__class__.__name__,
                                    self._price))
        return self._price

    def set_discount(self, discount):
        'Set discount for any good'
        self.discount = discount
        self.discounted_price = self._price * (
                    1 - self.discount / 100)
        print("{} discounted price set: {}".format(
            self.__class__.__name__,
            self.discounted_price))
        return self.discounted_price


class Food(Good):
    'Food is a child of a Good class'


class Banana(Food):
    'Banana is a child of a Food class'


class Apple(Food):
    'Apple is a child of a Food class'
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


class Lemon(Food):
    'Lemon is a child of a Food class'


class Tool(Good):
    'Tool is a child of a Good class'


class Nail(Tool):
    'Nail is a child of a Tool class'


class Axe(Tool):
    'Axe is a child of a Tool class'


class Hammer(Tool):
    'Hammer is a child of a Tool class'

