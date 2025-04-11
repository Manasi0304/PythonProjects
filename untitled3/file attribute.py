#d={2:"two",1:"one",4:"four",5:"five",3:"three"}
fob=open("All_accounts.txt","a")
print(fob.tell())
print(fob.closed)
print(fob.encoding)
print(fob.mode)
print(fob.name)
fob.close()