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
class Admin(Users):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees = [] #employee list

    def add_employee(self,name,phone,email,address, age, designation, salary):
        emp = Employe(name,phone,email,address, age, designation, salary)
        self.employees.append(emp)
        print(f"{name} is added as employee")
    def view_employee(self):
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address, emp.age, emp.designation, emp.salary)
    
admin = Admin("Likhon", 8801310847553, "Contact@likhon.com.bd", "Biyara, Banbariya, Sirajganj Sadar, Sirajganj")
admin.add_employee("Arju Molla", 8801724510193, "hafezmohammadarju193@gmail.com", "Biyara Ghat, Sirajganj Sadar Sirajganj", "24","Manager", 25000)
admin.view_employee()