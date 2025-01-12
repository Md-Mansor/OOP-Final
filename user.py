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
        if not self.order_cart:
            print("Your cart is empty.")
            return
        for product in self.order_cart:
            print(
                f"item name: {product['Name']}\t product quantity: {product['Quantity']} unit price: {product['Price']}\t total price: {product['Price'] * product['Quantity']}")

    def place_order(self):
        if len(self.order_cart) == 0:
            print("Your cart is empty.")
            return

        subtotal = sum(item["Price"] * item["Quantity"] for item in self.order_cart)

        if self.initial_balance < subtotal:
            print("Insufficient balance. Please add funds.")
            return

        print("**Order Summary**")
        for order in self.order_cart:
            name = order["Name"]
            price = order["Price"]
            quantity = order["Quantity"]
            total = price * quantity
            print(f"Item: {name}, Quantity: {quantity}, Unit Price: {price}, Total: {total}")
            order["Total"] = total
            self.past_order.append(order)

        print(f"Subtotal: {subtotal}")

        self.initial_balance -= subtotal
        print(f"Remaining Balance: {self.initial_balance}")

        self.order_cart.clear()
        print("Order placed successfully!")

    def view_past_order(self):
        print("**Past Orders**")
        if not self.past_order:
            print("No past orders available.")
            return

        grand_total = 0
        for ordered_item in self.past_order:
            total = ordered_item["Price"] * ordered_item["Quantity"]
            grand_total += total
            print(
                f"Name: {ordered_item['Name']}\tQuantity: {ordered_item['Quantity']}\t"
                f"Unit Price: {ordered_item['Price']}\tTotal: {total}"
            )
        print(f"Subtotal of All Orders: {grand_total}")

    def add_funds(self, money):
        self.initial_balance += money

    def view_balance(self):
        print(f"Your Total Balance: {self.initial_balance}")


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
