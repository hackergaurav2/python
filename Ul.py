n=input("Enter the String : ")
def ula():
   count1=0
   count2=0
   for i in n:
       if(i.islower()):
          count1=count1+1
       elif(i.isupper()):
           count2=count2+1
   print("upper case letter",count2)
   print("lower case letter ",count1)
ula()

