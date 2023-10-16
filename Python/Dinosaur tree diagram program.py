carnivore=input("Is this dinosaur a carnivore")
if carnivore=="No" or carnivore=="no":
    neck=input("Does this dinosaur have a long neck?")
    if neck=="Yes" or neck=="yes":
        tail=input("Does this dinosaur have a long, whip like tail?")
        if tail=="Yes" or tail=="yes":
            print("This dinosaur is a Diplodocus")
        elif tail=="No" or tail=="no":
            print("This dinosaur is a Brachiosaurus")
        else:
            print("This is an invalid answer")
    elif neck=="No" or neck=="no":
        print("This dinosaur is a Triceratops")
    else:
        print("This is an invalid answer")
elif carnivore=="Yes" or carnivore=="yes":
    big=input("Is this dinosaur big?")
    if big=="Yes" or big=="yes":
        print("This dinosaur is a T-rex, RUN")
    elif big=="No" or big=="no":
        mammal=input("Is this dinosaur a mammal?")
        if mammal=="Yes" or mammal=="yes":
            print("This dinosaur is a Velociraptor, RUN")
        elif mammal=="No" or mammal=="no":
            print("This dinsoaur is an Archaeopteryx, RUN")
        else:
            print("This is an invalid answer")
else:
    print("This is an invalid answer")