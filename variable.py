#variable Length argument
def Student_Data(roll,name,couse, *sub)
    print("roll=", roll)
    print("name=",name)
    print("couse=",couse)
    print("sub=",sub)
Student_Data(1,"Aka","BCA","py","se","auto")
Student_Data(2,"Lka","BCA","py","sl")

