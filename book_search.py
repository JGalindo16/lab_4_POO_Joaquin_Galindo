class Book_search():
    def __init__(self, book_list:list, number_list:list, author_list:list, gender_list:list):
        self.book_list=book_list
        self.number_list= number_list
        self.author_list= author_list
        self.gender_list= gender_list


    def search_for_autor(self, author):
        if author in self.author_list:
            print()
            print("-------------------------------------------------------------")
            for i in range(len(self.author_list)):
                if self.author_list[i] == author:
                    print(f"El libro {self.book_list[i]}, numero de serie {self.number_list[i]} es del autor {self.author_list[i]}") 
            print("-------------------------------------------------------------")
            print()     
        else:
            print("No hay libros de ese autor en la biblioteca")
    
    def search_for_gender(self, gender):
        if gender in self.gender_list:
            print()
            print("-------------------------------------------------------------")
            for i in range(len(self.gender_list)):
                if self.gender_list[i] == gender:
                    print(f"El libro {self.book_list[i]}, numero de serie {self.number_list[i]} es del genero {self.gender_list[i]}") 
            print("-------------------------------------------------------------")
            print()     
        else:
            print("No hay libros de ese genero en la biblioteca")
