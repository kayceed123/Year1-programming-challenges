teams=["Ferrari", "Williams", "Haas", "Racing Point"]
print("Current bonus payment:", teams[0])
print("There rival is:", teams[1])
teams[3]="Aston Martin"
teams.append("Red Bull Racing")
teams.append("Mercedes")
print(teams)

replace=int(input("What member do you want to replace? (number between 0 and 5)"))
if replace <0 or replace >5:
    print("error")
else:
    replacedname=input("Who do you want to replace this member with?")
    teams[replace]=replacedname
print(teams)

drivers=["Sebastian Vettel","Charles Leclerc", "Kevin Magnussen", "Lando Norris"]
wages=[21,17,3,5]
for driver in drivers:
    print(driver)

totalwage=0
for wage in wages:
    totalwage= totalwage + wage
    print(wage)
print("Total wages:", totalwage)