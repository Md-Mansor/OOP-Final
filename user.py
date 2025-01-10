from abc import ABC


class User(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def view_menu(self, restaurant):
        for item in restaurant.item_list:
            print(f"Name: {item.name}\t Quantity: {item.quantity}\t Price: {item.price}")


class Admin(User):
    def __init__(self, name, email, address, restaurant):
        super().__init__(name, email, address)
        self.restaurant = restaurant
        self.customers = []

    def add_items(self, item_name, item_quantity, item_price):
        self.restaurant.add_item(item_name, item_quantity, item_price)

    def add_customer(self, name, email, address):
        new_customer = Customer(name, email, address)
        self.customers.append(new_customer)

    def view_customer(self):
        print("Employee_List")
        for cus in self.customers:
            print(f"Name : {cus.name}\t Email: {cus.email}\t Address : {cus.address}")

    def remove_customer(self, fine_name):
        print("Removing Customer by their Name...")
        for remove_item in self.customers:
            if remove_item.name.lower() == fine_name.lower():
                self.customers.remove(remove_item)
                print(f"Customer '{fine_name}' has been removed.")
                return
        print("Customer name not found.")
