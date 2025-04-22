from abc import ABC
class Users(ABC):
    def __init__(self, name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        # super().__init__()
class Employe(Users):
    def __init__(self, name, phone, email, address,age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary
class Customer(Users):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = []
    def view_menu(self,restaurent):
        restaurent.menu.show_item()
    def add_to_cart(self,restaurent,item_name):
        pass
        item = restaurent.menu.find_item(item_name)
        if item:
            self.cart.append(item)
            print(f"{item.name} added to cart.")
        else:
            print("Product Not Found")
    def view_cart(self):
        print("*****Cart*****")
        if not self.cart:
            print("Cart is empty.")
        else:
            total = 0
            for item in self.cart:
                print(f"{item.name} - {item.price} BDT")
                total += item.price
            print(f"Total: {total} BDT")      
        
class Admin(Users):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    def add_employee(self,restaurent, employee):
        restaurent.add_employee(employee)
    def view_employee(self, restaurent):
       restaurent.view_employee()
    def add_new_item(self,restaurent,item):
        restaurent.menu.add_item(item)
class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = [] #employee list
        self.menu = Menu()
    def add_employee(self,employee):
        self.employees.append(employee)
        print(f"{employee.name} is added as employee")
    def view_employee(self):
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address, emp.age, emp.designation, emp.salary)
class Menu:
    def __init__(self):
        self.items = [] 
    def add_item(self, item):
        self.items.append(item)
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Delete Successfully")
        else:
            print("Item Not Found")
    def show_item(self):
        print("*********menu*********")
        print("Name \t Price \t Quentity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quentity}")

class FoodItem:
    def __init__(self,name,price,quentity):
        self.name = name
        self.price = price
        self.quentity = quentity
    

# admin = Admin("Likhon", 8801310847553, "Contact@likhon.com.bd", "Biyara, Banbariya, Sirajganj Sadar, Sirajganj")
# admin.add_employee("Arju Molla", 8801724510193, "hafezmohammadarju193@gmail.com", "Biyara Ghat, Sirajganj Sadar Sirajganj", "24","Manager", 25000)
# admin.view_employee()

# mn = Menu()
# item = FoodItem("Headphone", 500, 30)
# mn.add_item(item)
# mn.show_item()

admin = Admin("Likhon", 8801310847553, "contact@likhon.com.bd", "Sirajganj")
rest = Restaurent("Foodie's Heaven")

item = FoodItem("Burger", 250, 20)
admin.add_new_item(rest, item)

rest.menu.show_item()

cust = Customer("Rahim", "017xxxxxxxx", "rahim@email.com", "Sirajganj")
cust.view_menu(rest)            # View available items in the restaurant
cust.add_to_cart(rest, "Burger") # Add an item to the cart
cust.view_cart()                # See cart summary


