from abc import ABC


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
        self.initial_balance = 0

    def view_menu(self, restaurant):
        for item in restaurant.item_list:
            print(f"Name: {item.name}\t Quantity: {item.quantity}\t Price: {item.price}")

    def cart(self, restaurant, item_name, quantity):
        for item in restaurant.item_list:
            if item.name.lower() == item_name.lower():
                if item.quantity >= quantity:
                    self.order_cart.append({
                        "Name": item.name,
                        "Price": item.price,
                        "Quantity": quantity
                    })
                    item.quantity -= quantity
                    print(f"{quantity} {item.name}(s) added to the cart.")
                    return
                else:
                    print("Not enough items available.")
                    return
        print("Item not found.")

    def view_cart(self):
        for product in self.order_cart:
            print(
                f"item name: {product["Name"]}\t product quantity: {product["Quantity"]} unit price: {product["Price"]}\t total price: {product["Price"] * ["Quantity"]}")

    def place_order(self):
        if not self.order_cart:
            print("Your cart is empty.")
            return
        print("**Order Summary**")
        total_price = 0
        for order in self.order_cart:
            name = order["Name"]
            price = order["Price"]
            quantity = order["Quantity"]
            print(f"Item: {name}, Quantity: {quantity}, Unit Price: {price}, Total: {price * quantity}")
            total_price += price * quantity
            self.past_order.append(order)
        self.order_cart.clear()
        print(f"Total Price: {total_price}")
        print("Order placed successfully!")

    def view_past_order(self):
        print("**Past Orders**")
        for ordered_item in self.past_order:
            print(
                f"Name: {ordered_item['Name']}\tQuantity: {ordered_item['Quantity']}\t"
                f"Total: {ordered_item['Total']}\tSub Total: {ordered_item['Sub']}"
            )

    def add_funds(self, money):
        self.initial_balance += money

    def view_balance(self):
        print(self.initial_balance)


class Admin(User):
    def __init__(self, name, email, address, restaurant):
        super().__init__(name, email, address)
        self.restaurant = restaurant

    def add_items(self, item_name, item_quantity, item_price):
        self.restaurant.add_item(item_name, item_quantity, item_price)

    def view_items(self):
        self.restaurant.view_item()

    def remove_items(self, item_name):
        self.restaurant.remove_item(item_name)

    def update_item_price(self, item_name, new_price):
        self.restaurant.update_price(item_name, new_price)

    def add_customer(self, name, email, address):
        new_customer = Customer(name, email, address)
        self.restaurant.customer_list.append(new_customer)

    def view_customer(self):
        print("Employee_List")
        for cus in self.restaurant.customer_list:
            print(f"Name : {cus.name}\t Email: {cus.email}\t Address : {cus.address}")

    def remove_customer(self, find_name):
        print("Removing Customer by their Name...")
        for remove_one in self.restaurant.customer_list:
            if remove_one.name.lower() == find_name.lower():
                self.restaurant.customer_list.remove(remove_one)
                print(f"Customer '{find_name}' has been removed.")
                return
        print("Customer name not found.")
