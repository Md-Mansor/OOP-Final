class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.item_list = []

    def add_item(self, item_name, item_quantity, item_price):
        new_item = Item(item_name, item_quantity, item_price)
        self.item_list.append(new_item)
