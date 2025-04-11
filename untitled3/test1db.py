import sqlite3

con=sqlite3.connect("my_test_db1.bd")
print("enter student id")
id=input()
print("enter student name ")
sn=input()
print("enter student paid fees")
sf=input()
#(80000,'manasi bharati',9000)

query="insert into student_info(student_id,student_name,student_paid_fees )values ("+ id +" ,'" + sn +"', " + sf+" )"
con.execute(query)
con.commit()
con.close()

print("data saved...")