"""This is a Store module"""

from goods import Tool, Food


class Store:
    """This is a main Store class"""

    def __init__(self):
        self.all_goods = set()

    def remove_good(self, good):
        """Remove item from the store"""

    @property
    def overall_price_no_discount(self):
        """Show overall price without discount"""
        total = 0
        for good in self.all_goods:
            total += good.price
        return f"Total overall {self.__class__.__name__} price: " \
               f"{str(round(total, 2))}"

    @property
    def overall_price_with_discount(self):
        """Show overall price with discount"""
        total = 0
        for good in self.all_goods:
            total += good.price_with_discount
        return f"Total overall {self.__class__.__name__} price with " \
               f"discount: {str(round(total, 2))}"

    @property
    def all_goods_in_store(self):
        """Show all items"""
        all_goods = []
        for good in self.all_goods:
            all_goods.append(good.__class__.__name__)
        return all_goods


class GroceryStore(Store):
    """GroceryStore inherited from Store"""

    def __init__(self):
        super().__init__()

    def add_good(self, good):
        """Add a good to the store"""
        self.good = good
        if isinstance(self.good, Food):
            self.all_goods.add(self.good)
            print(f"{self.good.__class__.__name__} was added to the "
                  f"{self.__class__.__name__}")
        else:
            print(f"Sorry, {self.good.__class__.__name__} can't be added to "
                  f"the {self.__class__.__name__} store")

    def add_goods(self, *items):
        """Add items to the store"""
        for self.item in items:
            self.add_good(self.item)


class HardwareStore(Store):
    """HardwareStore inherited from Store"""

    def __init__(self):
        super().__init__()

    def add_good(self, good):
        """Add a good to the store"""
        self.good = good
        if isinstance(self.good, Tool):
            self.all_goods.add(self.good)
            print(f"{self.good.__class__.__name__} was added to the "
                  f"{self.__class__.__name__}")
        else:
            print(f"Sorry, {self.good.__class__.__name__} can't be added to "
                  f"the {self.__class__.__name__} store")

    def add_goods(self, *items):
        """Add items to the store"""
        for self.item in items:
            self.add_good(self.item)
