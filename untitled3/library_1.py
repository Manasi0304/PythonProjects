import datetime as dt

def issue_book():
    bnum = input("Enter Book Number to Issue : ")
    senr = input("Enter Student Enrollment Number : ")
    ob = dt.date.today()
    d = ob.day
    m = ob.month
    y = ob.year
    idate = str(d) + "/" + str(m) + "/" + str(y)

    fobj = open("all_issued.txt", "a")
    fobj.write(bnum + "," + senr + "," + idate + ",NA\n")
    fobj.close()
    print("Book Issued..!")

def return_book():
    book_found_flag = False
    ob = dt.date.today()
    d = ob.day
    m = ob.month
    y = ob.year
    rdate = str(d) + "/" + str(m) + "/" + str(y)
    bnum = input("Enter Book Number to Return : ")

    fobj = open("all_issued.txt","r")
    all_issues_ls = fobj.readlines()
    i=0
    while i<len(all_issues_ls):
        onedata_ls = all_issues_ls[i].split(",")
        if onedata_ls[0] == bnum and onedata_ls[3]=="NA\n":
            onedata_ls[3] = rdate + "\n"
            new_data = ",".join(onedata_ls)
            all_issues_ls[i] = new_data
            book_found_flag = True
            break
        i = i + 1
    fobj.close()

    if book_found_flag == True:
        fobj = open("all_issued.txt", "w")
        fobj.writelines(all_issues_ls)
        fobj.close()
        print("Book Returned..!")
    if book_found_flag == False:
        print("Invalid Book Number")

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
    bnum = input("Enter Book Number : ")

    fobj = open("all_issued.txt","r")
    for oneline in fobj:
        ls = oneline.split(",")
        if ls[0] == bnum:
            print(ls[1], "\t", ls[2], "\t", ls[3][0:len(ls[3])-1], "\n", end="")
    fobj.close()


def stud_history():
    senr = input("Enter Student's Enrollment Number : ")

    fobj = open("all_issued.txt","r")
    for oneline in fobj:
        ls = oneline.split(",")
        if ls[1] == senr:
            print(ls[0], "\t", ls[2], "\t", ls[3][0:len(ls[3])-1], "\n", end="")
    fobj.close()

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


