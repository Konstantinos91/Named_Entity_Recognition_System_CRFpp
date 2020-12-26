
#Opens and reads the created txt file(output) after the testing phase
test_f = open("crf_wikigold_conll_testoutput.txt", 'r')

#Initializations of variables
c = 0 #Counter
t = 0 #True
f = 0 #False
sentence_counter = 0

#for loop used in order to count and print the true and false predicted NER values, the total words, and the sentences in the output file
for line in test_f:
    if line == '\n' or line.split()==[]:
        sentence_counter+=1
        continue
    c = c + 1
    x = line.strip().split()
    if(x[-1]==x[-2]):    #Checks if the two values are the same (if the prediction is true or false)
        t = t + 1
    else:
        f = f + 1

print ('\n')


print ('<Counted_True>', '<Counted_False>', '<Counted_Words>', '<Counted_Sentences>')
print ('    ', t, '         ', f, '         ', c, '            ', sentence_counter)
print ('\n---------------------------------->')

#Calculating and printing of the accuracy of the NER system
print ('The accuracy is', (100.0*t/c))

print ('---------------------------------->\n')

