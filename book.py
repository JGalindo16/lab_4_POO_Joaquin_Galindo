class Book:

    def __init__(self, book_list:list, number_list:list, disponibility:list, author_list:list, gender_list:list, price_list:list, tenant_list:list, ingress_date_list:list, return_date_list:list):
        print()
        self.book_list = book_list
        self.number_list= number_list
        self.disponibility= disponibility
        self.author_list= author_list
        self.gender_list= gender_list
        self.price_list=price_list
        self.tenant_list=tenant_list
        self.ingress_date_list=ingress_date_list
        self.return_date_list=return_date_list

    def add_book(self):
        self.book_name = input("Cual es el nombre del libro: ")
        self.number= input("Cual es el número de serie del libro: ")
        if self.book_name in self.book_list and self.number in self.number_list:
            print()
            print("----------------------------------")
            print("Tu libro ya está en la biblioteca")
            print("----------------------------------")
            print()
        elif self.book_name in self.book_list and self.number not in self.number_list:
            self.author= input("Quien es el autor del libro: ")
            self.gender= input("De que genero es el libro: ")
            self.price= input("Cuanto cuesta el arriendo diario del libro: ")
            self.book_list.append(self.book_name)
            self.number_list.append(self.number)
            self.author_list.append(self.author)
            self.gender_list.append(self.gender)
            self.disponibility.append("Disponible")
            self.price_list.append(self.price)
            self.price_list.append(self.price)
            self.tenant_list.append("")
            self.ingress_date_list.append("")
            self.return_date_list.append("")
            print()
            print("----------------------------------")
            print("El libro se agregó con exito, pero \ncuidado que existe un libro con el mismo nombre pero distinto número de serie")
            print("----------------------------------")
            print()
        elif self.book_name not in self.book_list and self.number not in self.number_list:
            self.author= input("Quien es el autor del libro: ")
            self.gender= input("De que genero es tu libro: ")
            self.price= input("Cuanto cuesta el arriendo diario del libro: ")
            self.book_list.append(self.book_name)
            self.number_list.append(self.number)
            self.author_list.append(self.author)
            self.gender_list.append(self.gender)
            self.disponibility.append("Disponible")
            self.price_list.append(self.price)
            self.tenant_list.append("")
            self.ingress_date_list.append("")
            self.return_date_list.append("")
            print()
            print("----------------------------------")
            print("El libro se agregó con exito")
            print("----------------------------------")
            print()
        list_of_added_books=[self.book_list, self.number_list, self.disponibility, self.author_list, self.gender_list, self.price_list, self.tenant_list, self.ingress_date_list, self.return_date_list]        
        return list_of_added_books

    def delete_book(self):
        if len(self.book_list) == 0:
            print()
            print("-------------------------------------------")
            print("No hay libros para eliminar en este momento")
            print("-------------------------------------------")
            print()
        else:
            self.book_name = input("Cual es el nombre del libro: ")
            self.number= input("Cual es el número de serie del libro: ")
            if self.book_name not in self.book_list or self.number not in self.number_list:
                print()
                print("----------------------------------------------------------------")
                print("Tu libro no está en la biblioteca, por ende no se puede eliminar")
                print("----------------------------------------------------------------")
                print()
            elif self.book_name in self.book_list and self.number in self.number_list:
                index_of_book= self.number_list.index(self.number)
                self.book_list.pop(index_of_book)
                self.number_list.pop(index_of_book)
                self.author_list.pop(index_of_book)
                self.gender_list.pop(index_of_book)
                self.disponibility.pop(index_of_book)
                self.price_list.pop(index_of_book)
                self.tenant_list.pop(index_of_book)
                self.ingress_date_list.pop(index_of_book)
                self.return_date_list.pop(index_of_book)
                print()
                print("----------------------------------")
                print("El libro se ha eliminado con exito")
                print("----------------------------------")
                print()
            
        list_of_added_books=[self.book_list, self.number_list, self.disponibility, self.author_list, self.gender_list, self.price_list, self.tenant_list, self.ingress_date_list, self.return_date_list]
        
        return list_of_added_books