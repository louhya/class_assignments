PrimeList = [2, 3, 5, 7,]
num = int(input('Please enter a number?'))
for i in range(3, num+1, 2):    
    if i >= 2:
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            PrimeList.append(i)

else:
    print (PrimeList) 