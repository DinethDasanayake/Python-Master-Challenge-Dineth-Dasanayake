print("You will be given some question and you have to answer yes or no")
a = str(input("Does it have legs? "))
if a == "yes":
    a = str(input("Does it have wings? "))
    if a == "yes":
        print("It's a bird")
    elif a == "no":
        a = str(input("Does it bark? "))
        if a=="yes":
            print("It's a dog")
        elif a=="no":
            print("It's a cat")
        else:
            print("Please enter true information.")
    else:
        print("Please enter true information.")
elif a == "no":
    print("It's a snake")
else:
    print("Please enter true information.")

