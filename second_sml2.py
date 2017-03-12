# 0, 56, 42, 8, 13, 79, 5, 2, 18
# Python program to find smallest and min2nd smallest elements
def _2ndmin(Xlist):
    min1st = min2nd = max(Xlist)
    for i in range(len(Xlist)):
        if Xlist[i] < min1st:
            min2nd = min1st
            min1st = Xlist[i]
        elif Xlist[i] < min2nd and Xlist[i] != min1st:
            min2nd = Xlist[i]
    if min2nd == max(Xlist):
            print("No min2nd smallest element")
    else:
        print ('The second smallest element is',min2nd)

# Driver function to test above function
Xlist = [56, 42, 8, 13, 79, 5, 2, 18, 6]
_2ndmin(Xlist)

