'''
#"r" puts the file in read mode
file=open("gamerscore.csv","r")
#When "line" is called it will read a line within the file
line=file.readline()
#searchname=input("Please enter a name:")
#searchgamerscore=int(input("Enter a gamerscore: "))

#Loops through each line
while(line):
    data=line.split(",")
    #if data[0]==searchname:
    if int(data[1])<6000:
        print("Handle: ",data[0])
        #print("Gamerscore: ",data[1])
    #else:
        #print("Not chosen handle")
    line=file.readline()

file.close '''

addressfile=open("addressbook.csv","r")
line=addressfile.readline()
while(line):
    data=line.split(",")
    print("Name: ",data[0])
    print("Address: ", data[1])
    print("They live in: ", data[2])
    print("Phone number: ", data[3])
    line=addressfile.readline()

addressfile.close