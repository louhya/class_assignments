num = int(input('How many numbers would you like to input'))
num2avg = 0
Lnum = []
for i in range(num):
    num2avg = int(input("Please enter number %d of %d: " %(i+1,num)))
    Lnum.append(num2avg)
print ('The average of', Lnum, 'is', sum(Lnum)/num)
