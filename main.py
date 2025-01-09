from abc import ABC
from restaurant import Restaurant


class User(ABC):
    def __int__(self, name, mobile, email, address):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, mobile, email, address):
        super().__init__(name, mobile, email, address)

    def view_menu(self, restaurant):
        for item in restaurant.item_list:
            print(f"Name: {item.item_name}\t Quantity: {item.item_quantity}\t Price: {item.item_price} ")


class Admin(User):
    def __init__(self, name, mobile, email, address, nid):
        super().__init__(name, mobile, email, address)
        self.nid = nid
