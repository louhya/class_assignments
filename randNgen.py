import random
y = random.randint(1,10)
print(y)
for x in range(0, 3):
    num = int(input('Please enter a number?'))
    if y== num:
        print( "Congratulation you guessed the right number")
    elif y== num-1 or y== num+1:
        print("You are Hot")
    elif y== num-2 or y== num+2:
        print("You are Warm")
    else:
        print("You are Cold")

