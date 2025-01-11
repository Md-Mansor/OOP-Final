from restaurant import Restaurant
from user import Admin

restaurant = Restaurant("Food Paradise")

admin = Admin("Me", "admin@example.com", "123 Admin St.", restaurant)

admin.add_customer("John Doe", "john.doe@example.com", "123 Elm Street")
admin.add_customer("Jane Smith", "jane.smith@example.com", "456 Oak Avenue")

admin.add_items("Burger", 50, 20)
admin.add_items("Pizza", 30, 40)

admin.view_items()

admin.view_customer()
admin.remove_customer("john doe")
admin.view_customer()
