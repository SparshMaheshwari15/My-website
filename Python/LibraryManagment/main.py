class library:
    def __init__(self,List_Of_Books):
        self.books=List_Of_Books
        
    def Display_Available_Books(self):
        print("Books are present in the library are: ")
        for book in self.books:
            print("* "+book)
    def BorrowBook(self,bookname):
        if bookname in self.books:
            print(f"Book is issued {bookname}")
            self.books.remove(bookname)
            return True
        else:
            print("Book is not available")
            return False
    def ReturnBook(self,bookname):
        self.books.append(bookname)
        print("Book written success")
class Student:
    def requestbook(self):
        self.book=input("Enter the name of the book you want: ")
        return self.book
    def returnbook(self):
        self.book=input("Enter the name of the book you return: ")
        return self.book
if __name__ == "__main__":
    Central_Library=library(["Math","Calculus","Python","Physics"])
    student=Student()
    #Central_Library.Display_Available_Books()
    
    while(True): 
        WelcomeMsg='''Welcome to the library
Choose any option
1 View book
2 issue book
3 return book
4 exit the library
        '''
        print(WelcomeMsg)
        a=int(input("Enter your option "))
        if a==1:
            Central_Library.Display_Available_Books()
        elif a==2:
            Central_Library.BorrowBook(student.requestbook())
        elif a==3:
            Central_Library.ReturnBook(student.returnbook())
        elif a==4:
            print("Thanks for visiting")
            exit()
        else:
            print("Invalid option")
