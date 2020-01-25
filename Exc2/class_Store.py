class Store:
    "This is a main Store class"
    def __init__(self):
        self.goods = {}
        self.number_of_products = 0
        self.overall_price_no_discount = 0
        self.overall_price_with_discount = 0

    def show_overall_price_no_discount(self):
        print('overall_price_no_discount: ' +
              str(self.overall_price_no_discount) +
              ' - for' + str(self.__class__.__mro__[0].__name__))

    def show_overall_price_with_discount(self):
        print('overall_price_with_discount: ' +
              str(self.overall_price_with_discount) +
              ' - for' + str(self.__class__.__mro__[0].__name__))

    def add_item(self, item):
        self.item = item
        self.overall_price_no_discount += item.price
        self.overall_price_with_discount += item.discounted_price
        self.goods[item.__class__.__name__] = self.item.price
        print('{} added'.format(self.item.__class__.__name__))

    def remove_item(self, item):
        self.item = item
        if self.item.__class__.__name__ in self.goods:
            self.overall_price_no_discount -= item._price
            self.overall_price_with_discount -= item.discounted_price
            del self.goods[item.__class__.__name__]
            print('{} has removed from {}'.format
            (self.item.__class__.__name__, self.__class__.__mro__[0].__name__))
        else:
            print('{} can\'t be removed. It is not in {} '.format
            (self.item.__class__.__name__, self.__class__.__mro__[0].__name__))

    def show_all_items(self):
        print('All goods in {}: {}'.format
            (self.__class__.__mro__[0].__name__,self.goods))
