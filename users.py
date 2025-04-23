from abc import ABC
from orders import Order
class Users(ABC):
    def __init__(self, name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
class Employe(Users):
    def __init__(self, name, phone, email, address,age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary
class Customer(Users):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
    def view_menu(self,restaurent):
        restaurent.menu.show_item()
    def add_to_cart(self,restaurent,item_name, quentity):
        pass
        item = restaurent.menu.find_item(item_name)
        if item:
            if item.quentity < quentity:
                print("Item Quantity Exceeded")
            else:
                self.cart.add_item(item,quentity)
                print(f"{item.name} added to cart.")
        else:
            print("Product Not Found")
    def view_cart(self):
        print("*****Cart*****")
        if not self.cart:
            print("Cart is empty.")
        else:
            print("Name \t Price \t Quentity")
            for item,quentity in self.cart.items.items():
                print(f'{item.name}\t {item.price} \t {quentity}')
            print(f'Total Price: {self.cart.total_price}')  
class Admin(Users):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    def add_employee(self,restaurent, employee):
        restaurent.add_employee(employee)
    def view_employee(self, restaurent):
       restaurent.view_employee()
    def add_new_item(self,restaurent,item):
        restaurent.menu.add_item(item)

# admin = Admin("Likhon", 8801310847553, "contact@likhon.com.bd", "Sirajganj")
# rest = Restaurent("Foodie's Heaven")
# admin.add_new_item(rest, FoodItem("Burger", 250, 20))
# admin.add_new_item(rest, FoodItem("Pizza", 100, 12))
# admin.add_new_item(rest, FoodItem("Biriyani", 350, 11))
# admin.add_new_item(rest, FoodItem("Kabab and Grill", 270, 100))
# admin.add_new_item(rest, FoodItem("Chowmin Pasta", 370, 6))
# admin.add_new_item(rest, FoodItem("Set Meal", 500, 9))
# rest.menu.show_item()

# # Customer actions
# cust = Customer("Rahim", "017xxxxxxxx", "rahim@email.com", "Sirajganj")
# cust.view_menu(rest)  # View available items in the restaurant

# # Add item to cart
# # cust.add_to_cart(rest, "Burger", 1)
# # cust.add_to_cart(rest, "Pizza", 2)
# # cust.add_to_cart(rest, "Set Meal", 3)
# item_name = input("Enter item name: ")
# item_quentity = int(input("Enter Item Quantity: "))
# cust.add_to_cart(rest, item_name, item_quentity)
# # View cart summary
# cust.view_cart()


