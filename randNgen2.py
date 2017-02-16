import random
y = random.randint(1,10)
print(y)
num = 0
count = 0
while (num != y and count < 3):
    try:
        num = int(input('Please enter a number between 1 - 10: '))
        if y== num:
            print( "Congratulation you guessed the right number")
        elif abs(y-num) == 1:
            print("You are Hot")
            count+=1
            print("count = ", count)
        elif abs(y-num) == 2:
            print("You are Warm")
            count += 1
            print("count = ", count)
        else:
            print("You are Cold")
            count += 1
            print("count = ", count)
    except:
        print("Invalid input, ", end=" ")

