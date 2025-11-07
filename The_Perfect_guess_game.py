import random

rand_num = random.randint(1,100)

print("Let's start the game")

for i in range(1,101):

    n = int(input("Enter any number from 1 to 100 to guess correct number: "))

    if(n <= 100 and n >= 1):

        if(n == rand_num):
            print(f"You guess correct number {rand_num}. After {i} attempts.")
            i+=1
            break

        elif(n < rand_num):
            print("You are guessing wrong number. Choose bigger number.")
            print()
            i+=1
    
        elif(n > rand_num):
            print("You are guessing wrong number. Choose small number.")
            print()
            i+=1
    
    else:
        print("Invalid number.")
        break

