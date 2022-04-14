class Bookcopy():
    def __init__(self, book_list:list, number_list:list, disponibility:list, author_list:list, gender_list:list, existencia:bool):
        self.book_list = book_list
        self.number_list= number_list
        self.disponibility= disponibility
        self.author_list= author_list
        self.gender_list= gender_list
        self.existencia= existencia
    @property
    def inventary(self):
        print("hola")
        return self.book_list, self.number_list, self.disponibility, self.author_list, self.gender_list, self.existencia
    
    @inventary.getter
    def inventary(self):
        if self.existencia == False:
            print()
            print("----------------------------------------------------------------------------------------------------------------")
            for i in range(len(self.book_list)):
                print(f"El libro {self.book_list[i]} del autor {self.author_list[i]}, numero de serie {self.number_list[i]} y genero {self.gender_list[i]} está {self.disponibility[i]}")
            print("----------------------------------------------------------------------------------------------------------------")
            print()

        else:
            print()
            print("-----------------------------------------------------------------------------")
            print("No Hay libros en el iventario, prueba en manejar inventario y agrega un libro")
            print("-----------------------------------------------------------------------------")
            print()

