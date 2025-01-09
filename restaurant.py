class Item:
    def __init__(self, item_name, item_quantity, item_price):
        self.item_name = item_name
        self.item_quantity = item_quantity
        self.item_price = item_price


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.item_list = []
        self.customer = []

    def add_item(self, item_name, item_quantity, item_price):
        new_item = Item(item_name, item_quantity, item_price)
        self.item_list.append(new_item)


restaurant = Restaurant("Food Center")
