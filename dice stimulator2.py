import random
print("Dice Stimulator")
x=input("Press y to roll the dice or any key to exit:")
while x=="y" or x=="Y":
    d=random.randrange(1,7)
    print(".............")
    print(".           .")
    print(f".     {d}     .")
    print(".           .")
    print(".............")
    print("\n\n")
    x=input("Press y to roll the dice or any key to exit:")
exit()