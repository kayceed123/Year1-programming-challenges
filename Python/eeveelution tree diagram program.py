#eeveelution thing

#Base evolution
base=input("Is this pokemon a base evolution?")
if base=="Yes" or base=="yes":
    print("Your pokemon is eevee")
elif base=="No" or base=="no":
    stone=input("Does your pokemon evolve via a stone?")
    #Stone evolution
    if stone=="Yes" or stone=="yes":
        #gen1
        gen1=input("Is your pokemon from generation 1?")
        if gen1=="Yes" or gen1=="yes":
            #water type
            watertype=input("Is your pokemon a water type?")
            if watertype=="Yes" or watertype=="yes":
                print("Your pokemon is vaporion")
            elif watertype=="No" or watertype=="no":
                #fire type
                firetype=input("Is your pokemon a fire type?")
                if firetype=="Yes" or firetype=="yes":
                    print("Your pokemon is flareon")
                elif firetype=="No" or firetype=="no":
                    print("Your pokemon is Jolteon")
                else:
                    print("Invalid answer")
            else:
                print("Invalid answer")
        elif gen1=="No" or gen1=="no":
            #ice type
            icetype=input("Is your pokemon an ice type?")
            if icetype=="Yes" or icetype=="yes":
                print("Your pokemon is Glaceon")
            elif icetype=="No" or icetype=="no":
                print("Your pokemon is leafeon")
            else:
                print("Invalid answer")
        else:
            print("Invalid answer")
    elif stone=="No" or stone=="no":
        #gen6
        gen6=input("Is your pokemon from generation 6?")
        if gen6=="Yes" or gen6=="yes":
            print("Your pokemon is Sylveon")
        elif gen6=="No" or gen6=="no":
            #dark type
            darktype=input("Is your pokemon a dark type?")
            if darktype=="Yes" or darktype=="yes":
                print("Your pokemon is umbreon")
            elif darktype=="No" or darktype=="no":
                print("Your pokemon is Espeon")
            else:
                print("Invalid answer")
        else:
            print("Invalid Answer")
    else:
        print("Invalid answer")
else:
    print("Invalid answer")