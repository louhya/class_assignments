#C:\Users\Student_06-PT\PycharmProjects\class_assignments\aslcSample2.txt
#C:\Users\Student_06-PT\PycharmProjects\class_assignments\out_aslc.txt
import os
import os.path
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

in_file = input("Please enter the report file name: ")

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

while True:
    output_mode = input ("Do you want to: S) Display the result on the screen? B) Display the result on the screen and save it to a file?  F) save the result to a file? Q) To Quit?[S/B/F/Q]? : ")
    if output_mode == "S":
        print ("Display Only")
        break
    elif output_mode == "B":
        print ("Display and Save.")
        out_file = input("Please enter output file name: ")
        if os.path.isfile(out_file) and os.access(out_file, os.R_OK):
            output_mode = output_mode+input("File exists do you want to: A) Append to it? O)Overwrite it?[A/O]? : ")
            print(output_mode)
        else:
            pass
        break
    elif output_mode == "F":
        print ("Save only.")
        out_file = input("Please enter output file name: ")
        if os.path.isfile(out_file) and os.access(out_file, os.R_OK):
            output_mode = output_mode+input("File exists do you want to: A) Append to it? O)Overwrite it?[A/O]? : ")
            print(output_mode)
        else:
            pass
        break
    elif output_mode == "Q":
        import sys
        sys.exit(0)

if output_mode == "S":
    print("\n")
    print ("Report file name:", in_file)
    print ('-'*75 + "\n")
    print ("Lines:", lines)
    print ("blank lines:",blanklines)
    print ("sentences:",sentences)
    print ("words:",unadj_words)
    print ("Average Sentence Length:",unadj_words/sentences)
    print('-' * 75 + "\n")
    print('Below all words whith less than 4 characters, and sentences containing less than 7 words are ignored')
    print ("Adjusted sentences:",s_count)
    print ("Adjusted words:",w_count)
    print ("Adjusted Average Sentence Length:",w_count/s_count)

elif output_mode == "BO":
    print("\n")
    print("Report file name:", in_file)
    print('-' * 75 + "\n")
    print("Lines:", lines)
    print("blank lines:", blanklines)
    print("sentences:", sentences)
    print("words:", unadj_words)
    print("Average Sentence Length:", unadj_words / sentences)
    print('-' * 75 + "\n")
    print('Below all words whith less than 4 characters, and sentences containing less than 7 words are ignored')
    print("Adjusted sentences:", s_count)
    print("Adjusted words:", w_count)
    print("Adjusted Average Sentence Length:", w_count / s_count)
    print("Save only / overwrite.")
    with open(out_file, "w") as out_f:
            out_f.write("\n" * 1)
            out_f.write("Report file name: %s " %(in_file) + "\n" *1)
            out_f.write('-' * 75 + "\n")
            out_f.write("Lines: %d " %(lines)+ "\n")
            out_f.write("blank lines: %d" %(blanklines) + "\n")
            out_f.write("sentences: %d" %(sentences) + "\n")
            out_f.write("words: %d" %(unadj_words) + "\n")
            out_f.write("Average Sentence Length: %d" %(unadj_words / sentences) + "\n")
            out_f.write('-' * 75 + "\n")
            out_f.write('Below all words whith less than 4 characters, and sentences containing less than 7 words are ignored' + "\n")
            out_f.write("Adjusted sentences: %d" %(s_count) + "\n")
            out_f.write("Adjusted words: %d" %(w_count) + "\n")
            out_f.write("Adjusted Average Sentence Length: %d" %(w_count / s_count) + "\n")

elif output_mode == "BA":
    print("\n")
    print("Report file name:", in_file)
    print('-' * 75 + "\n")
    print("Lines:", lines)
    print("blank lines:", blanklines)
    print("sentences:", sentences)
    print("words:", unadj_words)
    print("Average Sentence Length:", unadj_words / sentences)
    print('-' * 75 + "\n")
    print('Below all words whith less than 4 characters, and sentences containing less than 7 words are ignored')
    print("Adjusted sentences:", s_count)
    print("Adjusted words:", w_count)
    print("Adjusted Average Sentence Length:", w_count / s_count)
    print("Save only / overwrite.")
    with open(out_file, "w") as out_f:
        out_f.write("\n" * 1)
        out_f.write("Report file name: %s " % (in_file) + "\n" * 1)
        out_f.write('-' * 75 + "\n")
        out_f.write("Lines: %d " % (lines) + "\n")
        out_f.write("blank lines: %d" % (blanklines) + "\n")
        out_f.write("sentences: %d" % (sentences) + "\n")
        out_f.write("words: %d" % (unadj_words) + "\n")
        out_f.write("Average Sentence Length: %d" % (unadj_words / sentences) + "\n")
        out_f.write('-' * 75 + "\n")
        out_f.write(
            'Below all words whith less than 4 characters, and sentences containing less than 7 words are ignored' + "\n")
        out_f.write("Adjusted sentences: %d" % (s_count) + "\n")
        out_f.write("Adjusted words: %d" % (w_count) + "\n")
        out_f.write("Adjusted Average Sentence Length: %d" % (w_count / s_count) + "\n")

elif output_mode == "FA":
    with open(out_file,"a") as out_f:
        out_f.write("\n" * 1)
        out_f.write("\n" * 1)
        out_f.write("Report file name: %s " % (in_file) + "\n" * 1)
        out_f.write('-' * 75 + "\n")
        out_f.write("Lines: %d " % (lines) + "\n")
        out_f.write("blank lines: %d" % (blanklines) + "\n")
        out_f.write("sentences: %d" % (sentences) + "\n")
        out_f.write("words: %d" % (unadj_words) + "\n")
        out_f.write("Average Sentence Length: %d" % (unadj_words / sentences) + "\n")
        out_f.write('-' * 75 + "\n")
        out_f.write('Below all words whith less than 4 characters, and sentences containing less than 7 words are ignored' + "\n")
        out_f.write("Adjusted sentences: %d" % (s_count) + "\n")
        out_f.write("Adjusted words: %d" % (w_count) + "\n")
        out_f.write("Adjusted Average Sentence Length: %d" % (w_count / s_count) + "\n")

elif output_mode == "FO":
        with open(out_file, "w") as out_f:
            out_f.write("\n" * 1)
            out_f.write("Report file name: %s " %(in_file) + "\n" *1)
            out_f.write('-' * 75 + "\n")
            out_f.write("Lines: %d " %(lines)+ "\n")
            out_f.write("blank lines: %d" %(blanklines) + "\n")
            out_f.write("sentences: %d" %(sentences) + "\n")
            out_f.write("words: %d" %(unadj_words) + "\n")
            out_f.write("Average Sentence Length: %d" %(unadj_words / sentences) + "\n")
            out_f.write('-' * 75 + "\n")
            out_f.write('Below all words whith less than 4 characters, and sentences containing less than 7 words are ignored' + "\n")
            out_f.write("Adjusted sentences: %d" %(s_count) + "\n")
            out_f.write("Adjusted words: %d" %(w_count) + "\n")
            out_f.write("Adjusted Average Sentence Length: %d" %(w_count / s_count) + "\n")
