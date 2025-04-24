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
            item_name = input("Enter Item Name: ")
            item_price = int(input("Enter Item Price: "))
            item_quentity = int(input("Enter Item Quentity: "))
            item = FoodItem(item_name,item_price,item_quentity)
            admin.add_new_item(rest, item)
        elif choice == '2':
            e_name = input("Eployee Name: ")
            e_mail = input("Eployee Email: ")
            e_phone = input("Eployee Phone: ")
            e_address = input("Eployee Address: ")
            e_age = input("Eployee Age: ")
            e_designation = input("Eployee Designation: ")
            e_salary = input("Eployee Salary: ")
            employee = Employe(e_name, e_phone,e_mail, e_address, e_age, e_designation, e_salary)
            admin.add_employee(rest, employee)
        elif choice == '3':
            admin.view_employee(rest)
        elif choice == '4':
            admin.view_item(rest)
        elif choice == '5':
            ditem_name = input("Item Name: ")
            admin.delete_item(rest, ditem_name)
        elif choice == '6':
            break
        else:
             print("Wrong Choice")

while True:
     print("Wellcome!!")
     print("1. Customer")
     print("2. Admin")
     print("3. Exit")
     choice = input("Enter Your Choice: ")
     if choice == '1':
          customer_menu()
     elif choice == '2':
          admin_menu()
     elif choice == '3':
          break
     else:
          print("Invalid Choice")