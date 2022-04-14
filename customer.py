from person import Person

class Customer(Person):
    def __init__(self, customer_name):
        self.customer_name= customer_name
        self.customer_list=[]
    
    def customer_register(self):
        if self.customer_name in self.customer_list:
            print()
            print("-----------------------------------------------------------")
            print("Ya estás registrado como usuario de la biblioteca, es decir\nya puedes arrendar libros como usuario en la biblioteca")
            print("-----------------------------------------------------------")
            print()
        else:
            self.customer_list.append(self.customer_name)
            print()
            print("------------------------------------------")
            print("Te has registarado como usuario con exito")
            print("------------------------------------------")
            print()
        return self.employee_list
        
    def checkout(self):
        if self.customer_name in self.customer_list:
            return True
        else:
            return False