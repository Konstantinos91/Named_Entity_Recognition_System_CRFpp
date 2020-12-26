
#Opening the initial wikigold.conll corpus file and the txt file for the preprocessed corpus 
inputCorpus = open("/home/konstantinos/PycharmProjects/CRF++Accuracy/wikigold.conll.txt", "r")
outputCorpus = open("/home/konstantinos/PycharmProjects/CRF++Accuracy/preprocessed_wikigold.conll.txt", "w")

#Replacing the backslash '\' from each line in the initial corpus file, with a whitespace ''
for j, line in enumerate(inputCorpus):
    line = line.replace("\\", "")
    outputCorpus.write(line)

#Closing both files
inputCorpus.close()
outputCorpus.close()
