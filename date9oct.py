

# Keyword Argument


def empData(name,age,dept):
     print("Name = "+name +" Age ="+str(age)+" department = "+dept)
val1=input("input employee name : ")
val2=input("input employee department : ")
val3= int(input("input age of the employee: "))
empData(age=val3,name=val1,dept=val2)
