from goto import goto, label
import os

label .start
os.system('cls')
print '''This script is Python 2.7.x compatible. The goto module has not been published for 3.6 yet. There is work being done on it.
"if then goto" is considered a joke and is implemented in Python as a jest.  To see what would happen if you use this for real in production
Please follow this url: https://imgs.xkcd.com/comics/goto.png

'''
uname = raw_input('Hi, what is your name? ')
print 'Nice to meet you',uname +"\n"
ucolor = raw_input('What is your favorite color? ')
print(ucolor+"? That's a nice color" + "\n")
ufood = raw_input('What is your favorite food? ')
print(ufood+" sound yummy" + "\n")
havetogo = raw_input('Do you have to go now? ')
print "\n"
if havetogo == 'no':
    goto .start
else:
    print ("Bye now")
