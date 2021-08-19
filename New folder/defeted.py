import pymysql

value = input("ENTER Pname : ")
con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
cur = con.cursor()
cur.execute("select * from products where Pname=%s",(value))
defrow = cur.fetchall()

for r in defrow:
    print(r[5])
    print(int(r[5]) + dNames.get())