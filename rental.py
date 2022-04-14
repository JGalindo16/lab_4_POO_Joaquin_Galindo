from sympy import Add


class Rental():
    def __init__(self, book_list:list, number_list:list, disponibility:list, ingress_date_list:list, return_date_list:list, tenant_list:list, price_list:list ):
        self.book_list=book_list
        self.number_list=number_list
        self.disponibility=disponibility
        self.ingress_date_list=ingress_date_list
        self.return_date_list=return_date_list
        self.tenant_list=tenant_list
        self.price_list=price_list

    def rent_a_book(self):
        book_title=input("¿Cuál es el nombre del libro?: ")
        serie_number=input("¿Cuál es el número de serie del libro?: ")
        if book_title in self.book_list:
            book_index=self.number_list.index(serie_number)
            if book_title == self.book_list[book_index]:
                if self.disponibility[book_index] != "Arrendado":
                    ingress_date=input("Fecha de arriendo (Recordar que debe poner dd/mm/aaaa): ")
                    if len(ingress_date) == 10 or len(ingress_date) == 9 or len(ingress_date) == 8:
                        tenant_name=input("A nombre de quien está el arriendo: ")
                        return_date=ingress_date.split("/")
                        self.ingress_date_list[book_index]=ingress_date
                        Add=int(return_date[0])+7
                        Add1=int(return_date[1])
                        Add2=int(return_date[2])
                        if Add > 31:
                            Add-=31
                            Add1+=1
                            if Add1 > 12:
                                Add1-=12
                                Add2+=1
                        self.return_date_list[book_index]=f"{Add}/{Add1}/{Add2}"
                        self.tenant_list[book_index]=tenant_name
                        self.disponibility[book_index]="Arrendado"
                        print()
                        print("-----------------------------------------------------------------------------------------------------------")
                        print(f"Tu libro ha sido arrendado con exito, debe devolverlo el {self.return_date_list[book_index]} ")
                        print("-----------------------------------------------------------------------------------------------------------")
                        print()   
                        return self.tenant_list, self.disponibility, self.ingress_date_list, self.return_date_list
                    else:
                        print()
                        print("-----------------------------------------------------------------------------------------------------------")
                        print(f"La fecha no es como se precisó en la instrucción")
                        print("-----------------------------------------------------------------------------------------------------------")
                        print()
                else:
                    print()
                    print("-----------------------------------------------------------------------------------------------------------")
                    print(f"El libro ya está arrendado")
                    print("-----------------------------------------------------------------------------------------------------------")
                    print()
            else:
                print()
                print("-------------------------------------------")
                print("Tu libro no coincide con el numero de serie")
                print("-------------------------------------------")
                print()
        else:
            print()
            print("-------------------------------------------")
            print("El libro no está en el inventario")
            print("-------------------------------------------")
            print()

    def return_a_book(self):
        book_name=input("Nombre del libro que quieres devolver: ")
        serie_number=input("Ingrese el número de serie: ")
        if book_name in self.book_list:
            book_index=self.number_list.index(serie_number) 
            if self.book_list[book_index] == book_name:
                if self.disponibility[book_index] == "Arrendado":
                    real_return_date=input("En que fecha devolvió el libro (dd/mm/aaaa): ")
                    ideal_return_date=self.return_date_list[book_index]
                    real_return_date=real_return_date.split("/")
                    ideal_return_date=ideal_return_date.split("/")
                    if int(real_return_date[2]) >= int(ideal_return_date[2]):
                        year=int(real_return_date[2]) - int(ideal_return_date[2])

                        if int(real_return_date[1]) >= int(ideal_return_date[1]):
                            month=int(real_return_date[1]) - int(ideal_return_date[1])

                            if int(real_return_date[0]) >=  int(ideal_return_date[0]):
                                day=int(real_return_date[0])- (int(ideal_return_date[0])-7)
                                total_days=(year*365 + month*31 + day)
                                
                                if total_days>7:
                                    late_book="atrasado"
                                else:
                                    late_book="a tiempo"
                                price=total_days*int(self.price_list[book_index])
                                print(f"El libro {book_name} se entrego {late_book}, dado que estuvo {total_days} con el usuario y por ende debe {price}")
                                self.return_date_list[book_index]=""
                                self.tenant_list[book_index]=""
                                self.disponibility[book_index]="Disponible"
                                self.ingress_date_list[book_index]=""
                                return self.tenant_list, self.disponibility, self.ingress_date_list, self.return_date_list
                            elif year != 0 or month != 0:
                                day=(38-int(ideal_return_date[0]))+ int(real_return_date[0])
                                total_days=(year*365 + (month-1)*31 + day)
                                print(total_days)
                                if total_days>7:
                                    late_book="atrasado"
                                else:
                                    late_book="a tiempo"
                                price=total_days*self.price_list[book_index]
                                print(f"El libro {book_name} se entrego {late_book}, dado que estuvo {total_days} con el usuario y por ende debe {price}")
                                self.return_date_list[book_index]=""
                                self.tenant_list[book_index]=""
                                self.disponibility[book_index]="Disponible"
                                self.ingress_date_list[book_index]=""
                                return self.tenant_list, self.disponibility, self.ingress_date_list, self.return_date_list
                            else:
                                print()
                                print("-----------------------------------------------------------------------------------------------------------")
                                print("Ingresa una fecha válida ")
                                print("-----------------------------------------------------------------------------------------------------------")
                                print()

                        elif int(real_return_date[1]) < int(ideal_return_date[1]) and year !=0:
                            month=int(ideal_return_date[1])- int(real_return_date[1])
                            if int(real_return_date[0]) >=  int(ideal_return_date[0]):
                                day=(int(real_return_date[0])-7)-int(ideal_return_date[0])
                                total_days=(year*365 - month*31 - day)
                                if total_days>7:
                                    late_book="atrasado"
                                else:
                                    late_book="a tiempo"
                                price=total_days*self.price_list[book_index]
                                print(f"El libro {book_name} se entrego {late_book}, dado que estuvo {total_days} con el usuario y por ende debe {price}")
                                self.return_date_list[book_index]=""
                                self.tenant_list[book_index]=""
                                self.disponibility[book_index]="Disponible"
                                self.ingress_date_list[book_index]=""
                                return self.tenant_list, self.disponibility, self.ingress_date_list, self.return_date_list
                            else:
                                day=int(ideal_return_date[0])-(int(real_return_date[0])-7)
                                total_days=(year*365 -(month*31 + day))
                                print(total_days)
                                if total_days>7:
                                    late_book="atrasado"
                                else:
                                    late_book="a tiempo"
                                price=total_days*self.price_list[book_index]
                                print(f"El libro {book_name} se entrego {late_book}, dado que estuvo {total_days} con el usuario y por ende debe {price}")
                                self.return_date_list[book_index]=""
                                self.tenant_list[book_index]=""
                                self.disponibility[book_index]="Disponible"
                                self.ingress_date_list[book_index]=""
                                return self.tenant_list, self.disponibility, self.ingress_date_list, self.return_date_list
                    else:
                        print()
                        print("-----------------------------------------------------------------------------------------------------------")
                        print("Ingresa una fecha válida ")
                        print("-----------------------------------------------------------------------------------------------------------")
                        print()
                else:
                    print()
                    print("-----------------------------------------------------------------------------------------------------------")
                    print("El libro está disponible")
                    print("-----------------------------------------------------------------------------------------------------------")
                    print()
            else:
                print()
                print("-----------------------------------------------------------------------------------------------------------")
                print("El libro y su número de serie no coinciden")
                print("-----------------------------------------------------------------------------------------------------------")
                print()
                
        else:
            print()
            print("-----------------------------------------------------------------------------------------------------------")
            print("El libro no esta en el inventario")
            print("-----------------------------------------------------------------------------------------------------------")
            print()
        
