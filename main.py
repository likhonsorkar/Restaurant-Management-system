from fooditem import FoodItem
from orders import Order
from menu import Menu
from restaurent import Restaurent
from users import Customer, Admin, Employe
rest = Restaurent("Foodie's Heaven")
def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your e-mail: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")

    customer = Customer(name,phone,email,address)

    while True:
        print(f"Wellcome {customer.name} !! ")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
                customer.view_menu(rest)
        elif choice == '2':
             item_name = input("Enter Item name: ")
             quentity = int(input("Enter your Quentity: "))
             customer.add_to_cart(rest,item_name, quentity)
        elif choice == '3':
             customer.view_cart()
        elif choice == '4':
             print("Paybill:")
             customer.cart.clear()
             print("Bill Pay Succesfull")
        elif choice == '5':
             break
        else:
             print("Wrong Choice")
def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your e-mail: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")

    admin = Admin(name, phone, email, address)

    while True:
        print(f"Wellcome {admin.name} !! ")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            break
        else:
             print("Wrong Choice")

admin_menu()