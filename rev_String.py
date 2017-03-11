urStr = input('Please enter your string: ')
x = len(urStr) - 1
revStr = ""
while x >= 0:
    revStr = revStr+urStr[x]
    x -= 1
print(revStr)


