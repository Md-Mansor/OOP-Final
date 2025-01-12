from restaurant import Restaurant

restaurant = Restaurant("Food Paradise")

while True:
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")
    choice = int(input("Enter Your User Type: "))
    if choice == 1:
        restaurant.admin_menu(restaurant)
    if choice == 2:
        restaurant.customer_menu(restaurant)
    if choice == 3:
        break
    else:
        print("Invalid Choice")
