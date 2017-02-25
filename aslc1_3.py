#F:\Users\Lhyacinthe\PycharmProjects\class_assignments\aslcSample2.txt
lines,blanklines,sentences,unadj_words,w_count,s_count=0,0,0,0,0,0
f2lines= []
s2list = []
punctuations = ['.', '?', '!', ',',';', ':']
print ('-'*65)
print('''Thank you for using ASLC Written By Acme Corp.

The Average Sentence Length Calculator (ASLC) will calculate the
average length of sentences in text formatted reports.
The calculator will not check whether the sentences are
grammatically correct nor will it check for spelling errors.

To send us your comments please email us at aslc.dev@acme.com
''')
while True:
    output_mode = input ("Do you want to: S) Display the result on the screen? B) Display the result on the screen and save it to a file?  F) save the result to a file? Q) To Quit?[S/B/F/Q]? : ")
    if output_mode == "S":
        print ("Display Only")
        break
    elif output_mode == "B":
        print ("Display and Save.")
        out_file = input("Please enter utput file name: ")
        break
    elif output_mode == "F":
        print ("Save only.")
        out_file = input("Please enter utput file name: ")
        break
    elif output_mode == "Q":
        import sys
        sys.exit(0)
    #break
in_file = input("Please enter the report file name: ")

#import subprocess
#import platform


#def clear():

#    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)

#clear()

try:

    filename = in_file
    textf = open(filename,'r')
except IOError:
    print ('cannot open file %s for reading' %filename)
    import sys
    sys.exit(0)

for line in textf:
    if line.startswith('\n'):
        blanklines += 1
    else:
        sentences += line.count('.') + line.count('!') + line.count('?')
        unadj_tempwords = line.split(None)
        unadj_words += len(unadj_tempwords)
        lines += 1 # Adjuested logic starts
        f2lines.append(" " + line.rstrip('\n\r'))
l2string = ''.join(f2lines)

while len(punctuations) > 0:
    if l2string.count(punctuations[0]) > 0:
        s2list.extend(l2string.split(punctuations[0]))
        l2string = str(s2list)
        s2list = []
        del punctuations[0]
    else:
        del punctuations[0]

l2string = l2string.replace('[', '').replace(']','').replace("\\",'').replace("'",'').replace('"','').replace('  ',' ')
s2list = []
s2list.extend(l2string.split(','))
s_count = len(s2list)
for i in range((len(s2list))):
    tempwords = s2list[i].split(None)
    temp_sentence_len = len(tempwords)
    if temp_sentence_len < 7:
        s_count -= 1
    else:
        for words in tempwords:
            if len(words) < 4:
                temp_sentence_len -=1

            else:
                pass
        if temp_sentence_len < 7:
            s_count -= 1
        else:
            w_count += temp_sentence_len


textf.close()

if output_mode == "S":
    print ("Report file name:", in_file)
    print ('-'*50)
    print ("Lines:", lines)
    print ("blank lines:",blanklines)
    print ("sentences:",sentences)
    print ("words:",unadj_words)
    print ("Average Sentence Length:",unadj_words/sentences)
    print ('-'*50)
    print('Below all words whith less than 4 characters, and sentences containing less than 7 words are ignored')
    print ("Adjusted sentences:",s_count)
    print ("Adjusted words:",w_count)
    print ("Adjusted Average Sentence Length:",w_count/s_count)
elif output_mode == "B":
    print ("Display and Save.")

elif output_mode == "F":
    print ("Save only.")
