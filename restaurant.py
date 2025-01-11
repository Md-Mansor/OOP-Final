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

    def view_item(self):
        print("**View Item**")
        for item in self.item_list:
            print(f"Item Name: {item.name}\tItem Quantity: {item.quantity}\t Item Price: {item.price}")

    def remove_item(self, item_name):
        print("Remove Item By Select Name")
        for remove_one in self.item_list:
            if remove_one.name.lower() == item_name.lower():
                self.item_list.remove(remove_one)
                print(f"Item {item_name} has been removed")
                return
        print("Item has not found")

    def update_price(self, item_name, new_price):
        for item in self.item_list:
            if item.name.lower() == item_name.lower():
                item.price = new_price
                print(f"The price of {item_name} has been updated to {new_price}")
                return
        print(f"Item {item_name} not found, price update failed.")
