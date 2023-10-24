tutor=input("Enter the name of the tutor")
numofstudents=int(input("Enter num of students"))
grade="empty"
studentnames=[]
studentgrades=[]
astar=0
a=0
b=0
c=0
d=0
fail=0
while numofstudents >0:
    student=input("enter the name of the student")
    studentnames.append(student)
    marks=int(input("How many marks did they get?"))
    if marks>=80 and marks<=100:
        print(student, " got an A*")
        astar=astar+1
        grade="A*"
    elif marks >=70 and marks <=79:
        print(student, " got an A")
        a=a+1
        grade="A"
    elif marks >=60 and marks <=69:
        print(student, " got a B")
        b=b+1
        grade="B"
    elif marks >=50 and marks <=59:
        print(student, "got a C")
        c=c+1
        grade="C"
    elif marks >=40 and marks <=49:
        print(student, " got a D")
        d=d+1
        grade="D"
    elif marks <40:
        print(student, " failed")
        fail=fail+1
    else:
        print("Invalid input")
        studentgrades.append(grade)
    numofstudents=numofstudents-1

print("In ",tutor,"'s class ", astar, " people got an A* ",a," people got an A ",b," people got a B ",c," people got a C ",d," people got a D and ", fail, " people failed" )
print(studentnames)
print(studentgrades)