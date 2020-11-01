def Pali(val):
    return val == val[::-1]
 
 

val =input("Enter name :")
val2 = Pali(val)
 
if val2:
    print("Yes")
else:
    print("No")