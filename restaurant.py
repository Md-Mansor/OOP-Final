from user import Admin, User, Customer


class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.item_list = []
        self.customer_list = []

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

    def add_customer(self, customer):
        self.customer_list.append(customer)

    def view_customers(self):
        print("**Customer List**")
        for customer in self.customer_list:
            print(f"Name: {customer.name}\tEmail: {customer.email}\tAddress: {customer.address}")

    @staticmethod
    def admin_menu(restaurant):
        name = input("Enter Admin Name: ")
        email = input("Enter Your Email Address: ")
        address = input("Enter Your Address: ")
        new_admin = Admin(name, email, address, restaurant)
        while True:
            print("1. Add Item")
            print("2. View Item")
            print("3. Remove Item")
            print("4. Update Item Price")
            print("5. Add Customer")
            print("6. View Customer")
            print("7. Remove Customer")
            print("8. Exit")
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                item_name = input("Enter Item Name: ")
                item_quantity = int(input("Enter Item Quantity: "))
                item_price = int(input("Enter Item Price: "))
                new_admin.add_items(item_name, item_quantity, item_price)
            elif choice == 2:
                new_admin.view_items()
            elif choice == 3:
                remove_name = input("Enter Name For Remove: ")
                new_admin.remove_items(remove_name)
            elif choice == 4:
                update_product = input("Enter Item Name For Update")
                new_price = int(input("Enter New Price: "))
                new_admin.update_item_price(update_product, new_price)
            elif choice == 5:
                customer_name = input("Enter Customer Name: ")
                customer_email = input("Enter Customer Email: ")
                customer_address = input("Enter Customer Address: ")
                new_admin.add_customer(customer_name, customer_email, customer_address)
            elif choice == 6:
                new_admin.view_customer()
            elif choice == 7:
                removable_name = input("Enter Item Name For Remove: ")
                new_admin.remove_customer(removable_name)
            elif choice == 8:
                break
            else:
                print("Invalid Input")

    def customer_menu(self, restaurant):
        your_name = input("Enter Your Name: ")
        old_customer = None
        for customer in self.customer_list:
            if your_name.lower() == customer.name.lower():
                your_email = input("Enter Your Email Address: ")
                if your_email.lower() == customer.email.lower():
                    old_customer = customer
                else:
                    print("Email Does Not Match")
            else:
                print("Name Does Not Match")

        if old_customer is None:
            return "Invalid Access"
        else:
            while True:
                print("1. View Menu")
                print("2. Add Product to Cart")
                print("3. View Cart")
                print("4. Place A Order Now")
                print("5. View past orders.")
                print("6. Add Fund")
                print("7. View Fund")
                print("8. Exit")
                choice = int(input("Please Select a option: "))
                if choice == 1:
                    old_customer.view_menu(restaurant)
                elif choice == 2:
                    i_name = input("Enter item name: ")
                    quant = int(input("Enter item Quant: "))
                    old_customer.cart(restaurant, i_name, quant)
                elif choice == 3:
                    old_customer.view_cart()
                elif choice == 4:
                    old_customer.place_order()
                elif choice == 5:
                    old_customer.view_past_order()
                elif choice == 6:
                    amount = int(input("Enter the amount: "))
                    old_customer.add_funds(amount)
                elif choice == 7:
                    old_customer.view_balance()
                elif choice == 8:
                    break
                else:
                    print("Invalid Input")
