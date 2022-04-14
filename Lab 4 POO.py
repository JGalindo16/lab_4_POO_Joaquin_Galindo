from book import Book
from bookcopy import Bookcopy
from employee import Employee
from book_search import Book_search
from customer import Customer
from rental import Rental

book_list=[]
number_list=[]
disponibility=[]
author_list=[]
gender_list=[]
employee_list=[]
price_list=[]
tenant_list=[]
ingress_date_list=[]
return_date_list=[]
existencia=True
while True:
    print(" (0) Salir \n (1) Ver inventario de la biblioteca \n (2) Manejo de arriendos \n (3) Libros por categoría \n (4) Modificar inventarios \n (5) Registrar Empleados")
    menu=input("Ingrese el número de la acción que desea realizar: ")
    if menu == "0":
        print()
        print("---------------------------------------")
        print("Muchas gracias por utilizar el programa")
        print("---------------------------------------")
        print()
        break
    elif menu == "1":
        inventary_show=Bookcopy(book_list, number_list, disponibility, author_list, gender_list, existencia)
        inventary_show.inventary
            
    elif menu == "2":
        print()
        name_user=input("Cual es tu nombre")
        if name_user in employee_list or name_user == customer_list:
            rental=Rental(book_list, number_list, disponibility, ingress_date_list, return_date_list, tenant_list, price_list)
            action=input("Que accion quieres realizar: \n (1) Arrendar libros \n (2) Devolver libros \n (3) Volver al menú de inicio \n\n Escriba el numero de la acción que desea realizar: ")
            if action == "1":
                returned_from_rental=rental.rent_a_book()
                if returned_from_rental != None:
                    tenant_list=returned_from_rental[0]
                    disponibility=returned_from_rental[1]
                    ingress_date_list=returned_from_rental[2]
                    return_date_list=returned_from_rental[3]

            elif action == "2":
                rental.return_a_book()
                if returned_from_rental != None:
                    tenant_list=returned_from_rental[0]
                    disponibility=returned_from_rental[1]
                    ingress_date_list=returned_from_rental[2]
                    return_date_list=returned_from_rental[3]
        else:
            print("No estas registrado, registrate primero")

    elif action == "3":
            pass

    elif menu == "3":
        print()
        research=Book_search(book_list, number_list, author_list, gender_list)
        action=input("Que accion quieres realizar: \n (1) Buscar por autor \n (2) Buscar por Genero \n (3) Volver al menú de inicio \n\n Escriba el numero de la acción que desea realizar: ")
        if action == "1":
            author=input("¿Por qué autor quieres filtrar?: ")
            research.search_for_autor(author)
        elif action == "2":
            gender=input("¿Por qué genero quieres filtrar?: ")
            research.search_for_gender(gender)
    
    elif menu == "4":
        print()        
        action=input("Que accion quieres realizar: \n (1) Agregar libro \n (2) Eliminar libro \n (3) Volver al menú de inicio \n\n Escriba el numero de la acción que desea realizar: ")
        if action == "1":
            book_for_action=Book(book_list, number_list, disponibility, author_list, gender_list, price_list, tenant_list, ingress_date_list, return_date_list)
            list_retuned=book_for_action.add_book()
            book_list=list_retuned[0]
            number_list=list_retuned[1]
            disponibility=list_retuned[2]
            author_list=list_retuned[3]
            gender_list=list_retuned[4] 
            price_list=list_retuned[5]
            tenant_list=list_retuned[6]
            ingress_date_list=list_retuned[7]
            return_date_list=list_retuned[8]
            existencia=False          
        elif action == "2":
            book_for_action=Book(book_list, number_list, disponibility, author_list, gender_list,price_list, tenant_list, ingress_date_list, return_date_list)
            list_retuned=book_for_action.delete_book()
            if list_retuned != None:
                book_list=list_retuned[0]
                number_list=list_retuned[1]
                disponibility=list_retuned[2]
                author_list=list_retuned[3]
                gender_list=list_retuned[4]
                price_list=list_retuned[5]
                tenant_list=list_retuned[6]
                ingress_date_list=list_retuned[7]
                return_date_list=list_retuned[8]
            if len(book_list) == 0:
                existencia=True

    elif menu == "5":
        print()
        action=input("Que accion quieres realizar: \n (1) Registrar empleado \n (2) Registrar usuario \n (3) Volver al menú de inicio \n\n Escriba el numero de la acción que desea realizar: ")
        if action == "1":
            employee_name=input("¿Cómo te llamas?: ")
            employee=Employee(employee_name)
            employee_list=employee.employee_register()
        elif action == "2":
            customer_name=input("¿Cómo te llamas?: ")
            customer=Customer(customer_name)
            customer_list=customer.customer_register()
    else:
        print()
        print("--------------------------------------------------------------------")
        print("No seleccionaste ninguna de las opciones válidas, intenta nuevamente")
        print("--------------------------------------------------------------------")
        print()
        

