"""Goods classes"""


class Good:
    """Main class Good for all goods"""

    def __init__(self, price, discount=0):
        self._discount = discount
        if price > 0:
            self._price = price
        else:
            raise ValueError

    @property
    def price(self):
        """Check price for any good"""
        return self._price

    @price.setter
    def price(self, value):
        """Set secret price"""
        if value == 30:
            self._price = value
            print(f"{value} is a secret price you may set")
        else:
            print(f"Sorry, price can't be reset")

    @property
    def price_with_discount(self):
        """Check price with discount for any good"""
        return self._price * (1 - self.discount / 100)

    @property
    def discount(self):
        """Check discount for any good"""
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Set discount for any good"""
        assert 1 <= discount <= 99, "Can't be less than 1 or more than 99"
        self._discount = discount


class Food(Good):
    """Food is a child of a Good class"""


class Banana(Food):
    """Banana is a child of a Food class"""


class Apple(Food):
    """Apple is a child of a Food class"""


class Lemon(Food):
    """Lemon is a child of a Food class"""


class Pear(Food):
    """Lemon is a child of a Food class"""


class Tool(Good):
    """Tool is a child of a Good class"""


class Nail(Tool):
    """Nail is a child of a Tool class"""


class Axe(Tool):
    """Axe is a child of a Tool class"""


class Hammer(Tool):
    """Hammer is a child of a Tool class"""
