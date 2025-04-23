from menu import Menu
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