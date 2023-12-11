import csv
#add student details
def add_students():
    students=open("namebook.csv","a")
    ID=int(input("Enter a student ID"))
    forename=input("Enter the students forename")
    surname=input("Enter the students surname")
    writer=students.write(students)
    writer.writerow(ID,forename,surname)
    students.close()

#view students details

#Login system
access=False
while access==False:
    username=input("Please enter your username")
    password=input("Please enter your password")
    if username=="teacher123" and password=="pass123":
        print("\nAccess granted")
        access=True
    else:
        print("\nAccess denied")

menu=int(input("\nWelcome to the menu \n\n Press 1 to add student details \n 2 to view student details \n 3 to create a report \n 4 to log out"))

if menu==1:
    add_students()