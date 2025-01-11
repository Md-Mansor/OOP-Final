from restaurant import Restaurant
from user import Admin, Customer

restaurant = Restaurant("Food Paradise")

admin = Admin("Admin", "admin@example.com", "123 Admin St.", restaurant)

admin.add_items("Burger", 50, 20)
admin.add_items("Pizza", 30, 40)

admin.view_items()

customer = Customer("John Doe", "john.doe@example.com", "123 Main St")
restaurant.add_customer(customer)

add_fund_input = int(input("Add Amount to your account: "))
customer.add_funds(add_fund_input)
customer.view_menu(restaurant)

customer.cart(restaurant, "Burger", 2)
customer.place_order()

admin.view_customer()
