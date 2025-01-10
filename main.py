from restaurant import Restaurant
from user import Admin

# Create an instance of Restaurant
restaurant = Restaurant("Food Paradise")

# Pass the restaurant instance to Admin
admin = Admin("Me", "admin@example.com", "123 Admin St.", restaurant)

# Add customers
admin.add_customer("John Doe", "john.doe@example.com", "123 Elm Street")
admin.add_customer("Jane Smith", "jane.smith@example.com", "456 Oak Avenue")

# Add items to the restaurant
admin.add_items("Burger", 50, 20)
admin.add_items("Pizza", 30, 40)

# Display the added items
print("Menu Items:")
for item in restaurant.item_list:
    print(f"Item: {item.name}, Quantity: {item.quantity}, Price: ${item.price:.2f}")

# View customers
admin.view_customer()
admin.remove_customer("john doe")
admin.view_customer()
