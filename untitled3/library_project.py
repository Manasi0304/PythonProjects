def issue_book():
    ''' accept Book number (to issue)
        accept student enrollment number (to issue)
        fetch current date and it will be issue-date
        directly add "NA" as returned-date

    '''
    bnum=input("enter book number : ")
    senr=input("enter enrollment number : ")



def return_book():
    pass


def add_new_student():
    enr = input("Enter Student Enrollment Number : ")
    sname = input("Enter Student Name : ")
    sclass = input("Enter Student Class : ")
    smob = input("Enter Student Mobile Number : ")
    semail = input("Enter Student Email : ")

    fobj = open("all_studs.txt", "a")
    fobj.write(enr + "," + sname + "," + sclass + "," + smob + "," + semail + "\n")
    fobj.close()
    print("New Student Added..")


def add_new_book():
    bnum = input("Enter Book Number : ")
    btitle = input("Enter Book Title : ")
    bauth = input("Enter Book Author : ")
    bpub = input("Enter Book Publication : ")

    fobj = open("all_books.txt", "a")
    fobj.write(bnum + "," + btitle + "," + bauth + "," + bpub + "\n")
    fobj.close()
    print("New Book Added..!")


def book_history():
    pass


def stud_history():
    pass


def search_book():
    print("Select an option")
    print("1 - Search By Book Number")
    print("2 - Search By Book Title")
    print("3 - Search By Author Name")
    print("4 - Search By Publication")
    ch = int(input("Provide Your Choice : "))
    if ch==1:
        pass
    elif ch==2:
        pass
    elif ch==3:
        pass
    elif ch==4:
        pass


def search_stud():
    print("Select an option")
    print("1 - Search By Enrollment Number")
    print("2 - Search By Mobile Number")
    print("3 - Search By Email Address")
    ch = int(input("Provide Your Choice : "))
    if ch==1:
        pass
    elif ch==2:
        pass
    elif ch==3:
        pass


def view_not_returned_books():
    pass


while True:
    print("\nSelect an option")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - Add New Book")
    print("4 - Add New Student")
    print("5 - Book History")
    print("6 - Student History")
    print("7 - Search Book")
    print("8 - Search Student")
    print("9 - Not Returned Books")
    print("0 - Exit")
    ch = int(input("Provide Your Choice : "))

    if ch==1:
        issue_book()
    elif ch==2:
        return_book()
    elif ch==3:
        add_new_book()
    elif ch==4:
        add_new_student()
    elif ch==5:
        book_history()
    elif ch==6:
        stud_history()
    elif ch==7:
        search_book()
    elif ch==8:
        search_stud()
    elif ch==9:
        view_not_returned_books()
    elif ch==0:
        exit(0)


