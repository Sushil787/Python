
import random
print("*************DICE SIMULATOR************")
n=int(input("\nEnter the number of dice rolling:  "))


for i in range(0,n):
    print(random.randrange(1,7))
    