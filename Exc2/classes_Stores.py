from Exc2.classes_Goods import Tool, Food
from Exc2.class_Store import Store

class GroceryStore(Store):
    "GroceryStore inherited from Store"
    def add_item(self, item):
        self.item = item
        self.parent_class = Food
        if isinstance(self.item, self.parent_class) == True:
            self.overall_price_no_discount += item._price
            self.overall_price_with_discount += item.discounted_price
            self.goods[item.__class__.__name__] = self.item._price
            print('{} added to the {}'.format
            (self.item.__class__.__name__, self.__class__.__mro__[0].__name__))
        else:
            print('{} can\'t be added to the {}'.format
            (self.item.__class__.__name__, self.__class__.__mro__[0].__name__))

    def add_items(self, *items):
        self.items = items
        self.parent_class = Food
        for self.item in items:
            if isinstance(self.item, self.parent_class) == True:
                self.overall_price_no_discount += self.item._price
                self.overall_price_with_discount += self.item.discounted_price
                self.goods[self.item.__class__.__name__] = self.item._price
                print('{} added to the {}'.format
                (self.item.__class__.__name__, self.__class__.__mro__[0].__name__))
            else:
                print('{} can\'t be added to the {}'.format
                (self.item.__class__.__name__, self.__class__.__mro__[0].__name__))


class HardwareStore(Store):
    "HardwareStore inherited from Store"
    def add_item(self, item):
        self.item = item
        self.parent_class = Tool
        if isinstance(self.item, self.parent_class) == True:
            self.overall_price_no_discount += item._price
            self.overall_price_with_discount += item.discounted_price
            self.goods[item.__class__.__name__] = self.item._price
            print('{} added to the {}'.format
            (self.item.__class__.__name__, self.__class__.__mro__[0].__name__))
        else:
            print('{} can\'t be added to the {}'.format
            (self.item.__class__.__name__, self.__class__.__mro__[0].__name__))

    def add_items(self, *items):
        self.items = items
        self.parent_class = Tool
        for self.item in items:
            if isinstance(self.item, self.parent_class) == True:
                self.overall_price_no_discount += self.item._price
                self.overall_price_with_discount += self.item.discounted_price
                self.goods[self.item.__class__.__name__] = self.item._price
                print('{} added to the {}'.format
                (self.item.__class__.__name__, self.__class__.__mro__[0].__name__))
            else:
                print('{} can\'t be added to the {}'.format
                (self.item.__class__.__name__, self.__class__.__mro__[0].__name__))