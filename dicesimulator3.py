import random
print("Dice Stimulator")
x=input("Press y to roll the dice or any key to exit:")
while x=="y" or x=="Y":
    d=random.randrange(1,7)
    if d==1:
        print(".............")
        print(".           .")
        print(".     0     .")
        print(".           .")
        print(".............")
    elif d==2:
        print(".............")
        print(".     0     .")
        print(".           .")
        print(".     0     .")
        print(".............")
    elif d==3:
        print(".............")
        print(".     0     .")
        print(".     0     .")
        print(".     0     .")
        print(".............")
    elif d==4:
        print(".............")
        print(".   0   0   .")
        print(".           .")
        print(".   0   0   .")
        print(".............")
    elif d==5:
        print(".............")
        print(".   0   0   .")
        print(".     0     .")
        print(".   0   0   .")
        print(".............")
    elif d==6:
        print(".............")
        print(".   0   0   .")
        print(".   0   0   .")
        print(".   0   0   .")
        print(".............")
    x=input("Press y to roll the dice or any key to exit:")
