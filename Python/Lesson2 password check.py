#TO BE FINSIHED

#Setting passwordlength to 0 so that it is an existing variable before the loop
passwordaccepted= 0
#While loop so that if passwordlength is less than 6 or greater than 12, it will loop the code until it isn't
while passwordaccepted==0:
    password= input("enter your password")
    if len(password) <6:
        print("Password has failed because your password is less than 6 digits long")
    elif len(password) >12:
        print("Password has failed because your password is over 12 digits long")
    else:
        print("Password has been accepted")
        
    passwordlength= len(password)

    lowercasepass= password.lower

    integercheck=0
    for y in range (len(password)):
        if y==0 or y==1 or y==2 or y==3 or y==4 or y==5 or y==6 or y==7 or y==8 or y==9:
            integercheck==1

    if password!=lowercasepass or integercheck!=1:
        print("Your password is not weak")
    else:
        print("Your password is weak")

    uppercasecheck=0
    for x in range(len(password)):
        if x==password.upper:
            uppercasecheck==1

    lowercasecheck=0
    for check in range(len(password)):
        if check==password.lower:
            lowercasecheck==1

    if lowercasecheck==1 and uppercasecheck==1 and integercheck==0:
        print("You have a medium password")
    elif lowercasecheck==1 and integercheck==1 and uppercasecheck==0:
        print("You have a medium password")
    elif uppercasecheck==1 and integercheck==1 and lowercasecheck==0:
        print("You have a medium password")
    elif uppercasecheck==1 and integercheck==1 and lowercasecheck==1:
        print("You have a strong password")

    passwordaccepted=1
