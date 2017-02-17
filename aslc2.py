lines,blanklines,sentences,words=0,0,0,0
num_chars=0
from colorama import init, Fore, Back, Style
init(autoreset=True)
print ('-'*50)
in_file = input("Please enter the report file name: ")

try:
    #filename = 'F:\Python36-32\sample.txt'
    filename = in_file
    textf = open(filename,'r')
except IOError:
    print (Fore.RED + Style.BRIGHT + 'cannot open file %s for reading' % filename)
    import sys
    sys.exit(0)

for line in textf:
    print (line)
    lines += 1
#    if line.startswith('\n'):
#        blanklines += 1
#    else:

#        sentences += line.count('.')+ line.count ('!')+ line.count('?')

    tempwords = line.split(None)
    #print (tempwords) 
    words += len(tempwords)


textf.close()

#print ('-'*50)
#print ("Lines:", lines)
#print ("blank lines:",blanklines)
#print ("sentences:",sentences)
#print ("words:",words)
#print ("Average Sentence Length:",words/sentences)
#print ("Report file name:", in_file)
#print (Fore.RED + " This is Red Text!")
