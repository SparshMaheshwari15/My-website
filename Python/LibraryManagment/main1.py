from os import read, write
from typing import ValuesView
Li=[]
class library:
    def __init__(self,List_Of_Books):
        self.books=List_Of_Books
    def Display_Available_Books(self):
        print("Books are present in the library are: ")
        for book in self.books:
            print("* "+book)
    def BorrowBook(self,bookname):
        IdNumber=input("Enter your ID Number: ")
        with open("Id number.txt") as f:
            id=f.read()
        if IdNumber in id:
            print("For verification purpose")
            name=input("Enter your name: ")
            with open("Student Id database.txt") as f:
                names=f.read()
                if f"{IdNumber} {name}" in names:
                    print("Verified")
                    print("issuing book in progress")


                    if bookname in self.books:
                        print(f"{bookname} Book is issued ")
                        self.books.remove(bookname)
                        #IdNumber=str(IdNumber)
                        f=open("Book issued.txt","a")
                        f.write(f"{bookname} Book is issued by student with id number {IdNumber} \n")
                        f.close()
                        return True
                    else:
                        print("Book is not available")
                        return False
                else:
                    print("name id does't match")
            
        
        else:
            print("Your Id number is not present in library database")
    def ReturnBook(self,bookname):
        IdNumber=input("Enter your Id number: ")
        f=open("Book issued.txt")
        data=f.read()
        f.close()
        if f"{bookname} Book is issued by student with id number {IdNumber}" in data:
            self.books.append(bookname)

            print("Book written success")
            f=open("Book issued.txt","a")
            f.write(f"{bookname} Book is returned by student with id number {IdNumber} \n")
            f.close()
        else:
            print("Invalid input")
    def AddBook(self,bookname):

        self.books.append(bookname)
    def NewRegistration():
        
        
            
        name=input("Enter your name: ")
        Li.append(name)
        Id=Li.index(name)+3
        
            #print(Li)
        
        
        with open("Student Id database.txt","a")as f:
            f.write(f"{Id} {name} \n")
        print(f"Your id is {Id}")
        '''
        ID=[1,2,3,4,5,6,7]
        n=0
        newid=ID[n]
        IDregistered=[]
        
        if newid in IDregistered:
            n=n+1
            
        print(f"Your ID is {newid}")
        ID.remove(newid)
        print(ID)
                

        IDregistered.append(newid)
        print(IDregistered)'''
        '''id=self.id
        new_id=id[1]
        id.pop(new_id)
        print(f"Your are registred your id is {new_id}")'''
        #print(f"{n}2ND")
        #ID=set(ID)
    def Suggestion():
        Name=input("Enter your name")
        suggestion=input("Enter your suggestion")
        with open("Suggestion.txt","a") as f:
            f.write(f"{Name}: {suggestion}\n")
    def ViewSuggestion():
        name=input("Enter your name: ")
        id=input("Enter your id: ")
        birthdate=input("Enter your birthdate in dd/mm/yyyy format: ")
        
        with open("owner.txt","r") as f:
            data1=f.read()
            print(f"{id} {name} {birthdate} ")
            if f"{id} {name} {birthdate} " in data1:
                print(a)
                print("You are the authorised person","r")
                with open("Suggestion.txt") as f:
                    data=f.read()
                    print(data)
            else:
                print("You are not the authorised person to see this information")

class Fine:
    
    pass


class Student:
    def requestbook(self):
        self.book=input("Enter the name of the book you want: ")
        return self.book
    def returnbook(self):
        self.book=input("Enter the name of the book you return: ")
        
        return self.book
    def AddBook(self):
        self.book=input("Enter the name of the book: ")
        name=input("Enter your name")
        print("Book added success")
        with open("Added book.txt","a") as f:
            f.write(f"{name} has donated book {self.book} ")

        return self.book
if __name__ == "__main1__":
    Central_Library=library(["Math","Calculus","Python","Physics","a","Road to unknown"])
    student=Student()
    #total_books_available=["Math","Calculus","Python","Physics"]
    #ID=[1,2,3,4,5,6,7,8]
    #Central_Library.Display_Available_Books()
    
    while(True): 
        WelcomeMsg='''Welcome to the library
Choose any option
1 View book
2 issue book
3 return book
4 Donate book
5 View donated book
6 New Student registration
7 Suggestions
8 View suggestion
9 exit the library

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
            Central_Library.AddBook(student.AddBook())
        elif a==5:
            name=input("Enter your name: ")
            id=input("Enter your ID number: ")
            date=input("Enter your date of birth in dd/mm/yyyy format: ")
            with open("owner.txt") as f:
                data=f.read()
                if (f"{id} {name} {date}") in data:
                    with open("Added book.txt") as f:
                        data=f.read()
                        print(data)
                else:
                    print("You are not a authorised person")
        elif a==6:
            
            #exit()
            library.NewRegistration()
        elif a==7:
            library.Suggestion()
        elif a==8:
            name=input("Enter your name: ")
            id=input("Enter your ID number: ")
            date=input("Enter your date of birth in dd/mm/yyyy format: ")
            with open("owner.txt") as f:
                data=f.read()
                if (f"{id} {name} {date}") in data:
                    with open("Suggestion.txt") as f:
                        data=f.read()
                        print(data)
            
            #library.ViewSuggestion()
        elif a==9:
            print("Thanks for visiting")
            f=open("Book issued.txt","w")
            f.write("")
            f.close()
            
            f=open("Added book.txt","w")
            f.write("")
            f.close()
            with open("Suggestion.txt","w") as f:
                f.write("")
            exit()
        else:
            print("Invalid option")
