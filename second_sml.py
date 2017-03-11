# 0, 42, 8, 13, 79, 5, 2, 18
Xlist = input("Please enter all the numbers in your list separated by one space: ").split(',')
print(Xlist)
XArray = []
Xlist_size = len(Xlist)
print(Xlist_size)
print('max_Xlist', max(Xlist))
for x in range(Xlist_size):
    Xlval = int(Xlist[x])
    XArray.append(Xlval)
    print(max(XArray))
    print(XArray)
x += 1
#min1st = min2nd = 0
#print(min1st, min2nd)
#minimum = Xlist[0]  # arbitrary number in list
#    for x in Xlist:
 #       if x < minimum:
  #          minimum = x
   # new_list.append(minimum)
    #Xlist.remove(minimum)

