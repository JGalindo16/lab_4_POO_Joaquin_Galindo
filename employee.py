from person import Person

class Employee(Person):

    def __init__(self, employee_name):
        self.employee_name= employee_name
        self.employee_list=[]

    def employee_register(self):
        if self.employee_name in self.employee_list:
            print()
            print("-----------------------------------------------------------")
            print("Ya estás registrado como empleado de la biblioteca, es decir\nya puedes arrendar libros como empleado en la biblioteca")
            print("-----------------------------------------------------------")
            print()
        else:
            self.employee_list.append(self.employee_name)
            print()
            print("------------------------------------------")
            print("Te has registarado como empleado con exito")
            print("------------------------------------------")
            print()
        return self.employee_list
        
    def checkout(self):
        if self.employee_name in self.employee_list:
            return True
        else:
            return False
        