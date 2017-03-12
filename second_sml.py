# 0, 56, 42, 8, 13, 79, 5, 2, 18
def sml2nd(Xlist):
    XArray = []
    for x in range(len(Xlist)):
        XArray.append(int(Xlist[x]))
    min1st = min2nd = max(XArray)
    for i in range(len(XArray)):
        if XArray[i] < min1st:
            min2nd = min1st
            min1st = XArray[i]
        else:
            min1st = min2nd
            print('condition not met', min2nd, XArray[i])
    print(min2nd)
    return min2nd

Xlist = input("Please enter all the numbers in your list separated by one space: ").split(',')
sml2nd(Xlist)
