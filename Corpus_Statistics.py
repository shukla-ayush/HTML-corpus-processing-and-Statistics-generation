from collections import Counter
import os
import glob
from operator import itemgetter

def indexer_corpus_stats ():
    new_dict_1gram = dict()    # unigram ductionary
    new_dict_2gram = dict()    # bigram dictionary
    new_dict_3gram = dict()    # trigram dictionary
    tft_dict1 = dict()         # TermFrequency dictionary for unigram
    tft_dict2 = dict()         # TermFrequency dictionary for bigram
    tft_dict3 = dict()         # TermFrequency dictionary for trigram
    dft_dict1 = dict()         # TermFrequency dictionary for unigram
    dft_dict2 = dict()         # TermFrequency dictionary for bigram
    dft_dict3 = dict()         # TermFrequency dictionary for trigram
    token_count_dict = dict()  # Dictionary for storing Tokens

    # to open every file in given directory
    for file in glob.glob("*.txt"):

        w = Counter()         # Counter for unigram
        w2 = Counter()        # Counter for bigram
        w3 = Counter()        # Counter for trigram
        temp = {}
        temp2 = {}
        temp3 = {}
        count = 0
        page = ""
        bigram_list = list()   # list for bigram
        trigram_list = list()  # list for trigram

        # opening file in read mode:
        with open(file, "r", encoding = 'UTF-8') as f:
            page = f.read()
            bigrm = page
            tigrm = page

            # Strings used
            s = ""
            r = ""
            t = ""
            d = ""
            e = ""
            g = ""

           ################################ For Indexer ############################################

            # unigram dictionary created
            for word in page.splitlines():
                w.update(word.split())
                temp = dict(w)
            print(temp)


            # bigram list created
            for j in range(len(bigrm.split()) - 1):
                bigram_list.append((bigrm.split()[j], bigrm.split()[j+1]))
            w2.update(bigram_list)
            temp2 = dict(w2)

            # trigram list created
            for k in range(len(tigrm.split()) - 2):
                trigram_list.append((tigrm.split()[k], tigrm.split()[k+1],  tigrm.split()[k+2]))
            w3.update(trigram_list)
            temp3 = dict(w3)


            # unigram dictionary updated for indexer
            for i in temp:

                count = count + 1      #Total number of tokens in each document

                if i in new_dict_1gram:
                    new_dict_1gram[i].append([file, temp[i]])
                else:
                    new_dict_1gram[i] = [[file, temp[i]]]

            # Dictionary for storing tokens, updated
            token_count_dict[file] = count


            # bigram dictionary updated for indexer
            for j in temp2:
                if j in new_dict_2gram:
                    new_dict_2gram[j].append([file, temp2[j]])
                else:
                    new_dict_2gram[j] = [[file, temp2[j]]]


            # trigram dictionary updated for indexer
            for k in temp3:
                if k in new_dict_3gram:
                    new_dict_3gram[k].append([file, temp3[k]])
                else:
                    new_dict_3gram[k] = [[file, temp3[k]]]


            ###################### For Term Frequency  #############################################

            # Term Frequency Dictionary for Unigram updated
            for i in temp:
                if i in tft_dict1:
                    tft_dict1[i] += temp[i]
                else:
                    tft_dict1[i] = temp[i]


            # Term Frequency Dictionary for Bigram updated
            for j in temp2:
                if j in tft_dict2:
                    tft_dict2[j] += temp2[j]
                else:
                    tft_dict2[j] = temp2[j]

            # Term Frequency Dictionary for Trigram updated
            for k in temp3:
                if k in tft_dict3:
                    tft_dict3[k] += temp3[k]
                else:
                    tft_dict3[k] = temp3[k]


            ####################### For Document Frequency  ########################################

            # Document frequency dictionary for unigram updated
            for i in temp:
                if i in dft_dict1:
                    dft_dict1[i] = [dft_dict1[i][0]+ "  "+file ,dft_dict1[i][1]+1]
                else:
                    dft_dict1[i] = [(file),1]


            # Document frequency dictionary for bigram updated
            for j in temp2:
                if j in dft_dict2:
                    dft_dict2[j] = [dft_dict2[j][0]+ "  "+file ,dft_dict2[j][1]+1]
                else:
                    dft_dict2[j] = [(file), 1]


            # Document frequency dictionary for trigram updated
            for k in temp3:
                if k in dft_dict3:
                    dft_dict3[k] = [dft_dict3[k][0]+ "  "+file ,dft_dict3[k][1]+1]
                else:
                    dft_dict3[k] = [(file), 1]



    ##################  Writing Index to the text files ########################

    #write the new_dict_1gram in unigram file
    with open("...Enter location here...", "a") as f:
        for key,value in new_dict_1gram.items():
            f.write('%s:%s' % (key, value))


    #write the new_dict_2gram in bigram file
    with open("...Enter location here...", "a") as f:
        for key,value in new_dict_2gram.items():
            f.write('%s:%s\n' % (key, value))

    #write the new_dict_3gram in trigram file
    with open("...Enter location here...", "a") as f:
        for key,value in new_dict_3gram.items():
            f.write('%s:%s\n' % (key, value))



    #################  Writing Term Frequency to the text files ####################

    s = sorted (tft_dict1.items(), key = itemgetter(1), reverse = True)
    with open("...Enter location here...", "a") as f:
        for key,value in s:
            f.write('%s:%s\n' % (key, value))

    r = sorted (tft_dict2.items(), key = itemgetter(1), reverse = True)
    with open("...Enter location here...", "a") as f:
        for key,value in r:
            f.write('%s:%s\n' % (key, value))

    t = sorted (tft_dict3.items(), key = itemgetter(1), reverse = True)
    with open("...Enter location here...", "a") as f:
        for key,value in t:
            f.write('%s:%s\n' % (key, value))



   #################  Writing Document Frequency to the text files ####################

    d = sorted(dft_dict1.items())
    with open("...Enter location here...", "a") as f:
        for key, value in d:
            f.write('%s:%s\n' % (key, value))

    e = sorted(dft_dict2.items())
    with open("...Enter location here...", "a") as f:
        for key, value in e:
            f.write('%s:%s\n' % (key, value))

    g = sorted(dft_dict3.items())
    with open("...Enter location here...", "a") as f:
        for key, value in g:
            f.write('%s:%s\n' % (key, value))

# Calling the function
indexer_corpus_stats()
