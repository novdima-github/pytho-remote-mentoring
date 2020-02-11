"""This is a Store module"""

from goods import Tool, Food


class Store:
    """This is a main Store class"""

    def __init__(self, good=None):
        self.good = good
        self.all_goods = set()

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
        all_goods = set()
        for good in self.all_goods:
            all_goods.add(good.__class__.__name__)
        return all_goods

    def remove_good(self, good):
        """Remove item from the store"""
        if good in self.all_goods:
            self.all_goods.remove(good)
            print(f"{good.__class__.__name__} was removed from "
                  f"{self.__class__.__name__}")
        else:
            print(f"{good.__class__.__name__} "
                  f"not in {self.__class__.__name__}")


class GroceryStore(Store):
    """GroceryStore inherited from Store"""

    def add_good(self, good):
        """Add a good to the store"""
        if isinstance(good, Food):
            self.all_goods.add(good)
            print(f"{good.__class__.__name__} was added to the "
                  f"{self.__class__.__name__}")
        else:
            print(f"Sorry, {good.__class__.__name__} can't be added to "
                  f"the {self.__class__.__name__} store")

    def add_goods(self, *items):
        """Add items to the store"""
        for item in items:
            self.add_good(item)


class HardwareStore(Store):
    """HardwareStore inherited from Store"""

    def add_good(self, good):
        """Add a good to the store"""
        if isinstance(good, Tool):
            self.all_goods.add(good)
            print(f"{good.__class__.__name__} was added to the "
                  f"{self.__class__.__name__}")
        else:
            print(f"Sorry, {good.__class__.__name__} can't be added to "
                  f"the {self.__class__.__name__} store")

    def add_goods(self, *items):
        """Add items to the store"""
        for item in items:
            self.add_good(item)
