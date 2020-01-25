class Good:

    def __init__(self, price):
        if price > 0:
            self._price = price
        else:
            raise ValueError
        self.discounted_price = price

    @property
    def price(self):
        print("{} price: {}".format(self.__class__.__name__,
                                    self._price))
        return self._price

    def set_discount(self, discount):
        self.discount = discount
        self.discounted_price = self._price * (
                    1 - self.discount / 100)
        print("{} discounted price set: {}".format(
            self.__class__.__name__,
            self.discounted_price))
        return self.discounted_price


class Food(Good):
    pass


class Banana(Food):
    pass


class Apple(Food):
    pass


class Lemon(Food):
    pass


class Tool(Good):
    pass


class Nail(Tool):
    pass


class Axe(Tool):
    pass


class Hammer(Tool):
    pass

