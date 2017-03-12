Urlist = input("Please enter your phrase: ").split()
print(Urlist)
new_list = []
while Urlist:
    minimum = Urlist[0]  # arbitrary number in list 
    for x in Urlist: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    Urlist.remove(minimum)    

print (new_list)