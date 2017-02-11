def gottogo():
    uname = input('Hi, what is your name? ')
    print('Nice to meet you',uname)
    ucolor = input('What is your favorite color? ')
    print(ucolor+"? That's a nice color")
    ufood = input('What is your favorite food? ')
    print(ufood+" sound yummy")
gottogo()

havetogo = input('Do you have to go now? ')
if havetogo == 'no':
    gottogo()
else:
    print('Bye now')