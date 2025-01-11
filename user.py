from abc import ABC
from restaurant import Restaurant


class User(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.order_cart = []
        self.past_order = []

    def view_menu(self, restaurant):
        for item in restaurant.item_list:
            print(f"Name: {item.name}\t Quantity: {item.quantity}\t Price: {item.price}")

    def cart(self, restaurant, item_name, quantity):
        for item in restaurant.item_list:
            if item.name.lower() == item_name.lower() and item.quantity >= quantity:
                self.order_cart.append(f"(Name:{item.name},Price:{item.price}, Quantity:{quantity})")
                item.quantity -= quantity
                return
            else:
                print("Not Enough item available")
                return
        print("Item not found")

    def place_order(self):
        print("**Order Summary**")
        total_price = 0
        for name, price, quantity in self.order_cart:
            print(f"Item: {name}, Quantity: {quantity}, Unit Price: {price}, Total: {price * quantity}")
            total_price += price * quantity
            self.past_order.append({
                "Name": name,
                "Quantity": quantity,
                "Total": price * quantity,
                "Sub": total_price
            })
        self.order_cart.clear()
        print("Order placed successfully!")

    def view_past_order(self):
        print("**Past Orders**")
        for ordered_item in self.past_order:
            print(
                f"Name: {ordered_item['Name']}\tQuantity: {ordered_item['Quantity']}\t"
                f"Total: {ordered_item['Total']}\tSub Total: {ordered_item['Sub']}"
            )


class Admin(User):
    def __init__(self, name, email, address, restaurant):
        super().__init__(name, email, address)
        self.restaurant = restaurant
        self.customers = []

    def add_items(self, item_name, item_quantity, item_price):
        self.restaurant.add_item(item_name, item_quantity, item_price)

    def view_items(self):
        self.restaurant.view_item()

    def remove_items(self):
        self.restaurant.remove_item()

    def update_item_price(self, item_name, new_price):
        self.restaurant.update_price(item_name, new_price)

    def add_customer(self, name, email, address):
        new_customer = Customer(name, email, address)
        self.customers.append(new_customer)

    def view_customer(self):
        print("Employee_List")
        for cus in self.customers:
            print(f"Name : {cus.name}\t Email: {cus.email}\t Address : {cus.address}")

    def remove_customer(self, find_name):
        print("Removing Customer by their Name...")
        for remove_one in self.customers:
            if remove_one.name.lower() == find_name.lower():
                self.customers.remove(remove_one)
                print(f"Customer '{find_name}' has been removed.")
                return
        print("Customer name not found.")
