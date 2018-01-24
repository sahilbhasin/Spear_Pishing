
import re
import numpy as np
matrix=[]
import string
import re
import os
f=open("output_Table","r+")

def load(filename):
    file= open(filename, "r+")
    return file

def count_sentences_and_words(path):
    Tot_Len_of_Words = 0
    sentencecounter1 = 0
    sentencecounter = 0
    ToTal_Legit_Words = 0
    counter=0
    extra_word_counter = 0
    wordcount={}
    file=load(path)
    for line in file:
        if "Original Message" in line:
            break
            #print("line is : ", line)
            #print("counter : ", counter)
        counter += 1
        wordcounter = 0
        flag = 0
        if counter > 15:
            for word in line.split():
                wordcounter += 1;
                if word not in wordcount:       #WORD COUNTER
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
                if "." in word:  # SENTENCE COUNTER
                    flag = 1        # FLAG FOR WORD COUNTER
                    sentencecounter += 1
                    #print("counting - ",sentencecounter)
                if "?" in word:
                    extra_word_counter += 1  # FLAG FOR EXTRA WORDS
                    flag = 1
                    sentencecounter1 += 1
                if ".com" in word:
                    sentencecounter -= 1
            if flag == 1:
                #print("words in line ", wordcounter)
                ToTal_Legit_Words += wordcounter
                for word in line.split():
                    Tot_Len_of_Words += word.__len__()
                    # print("no of words for this line : ",wordcounter)
    file.close()
    return sentencecounter+sentencecounter1, ToTal_Legit_Words-extra_word_counter, Tot_Len_of_Words-sentencecounter


def time_and_date(path):
    file=load(path)
    counter=0
    for line in file:
        counter += 1
        if counter == 2:
            for word in line.split():
                if ':' in word and word.__len__()>6:
                    time=word[0:2]
            day = line[6:9]
    file.close()
    return time,day


def Average(sentencecounter, ToTal_Legit_Words, Tot_Len_of_Words,nop ):
    sentencecounter, ToTal_Legit_Words, Tot_Len_of_Words
    if sentencecounter == 0:
        AvgWordPerSentence = 0
    else:
        AvgWordPerSentence = (ToTal_Legit_Words) / sentencecounter

    if nop == 0:
        AvgSentPerParagraph = 0
    else:
        AvgSentPerParagraph = sentencecounter / nop

    if ToTal_Legit_Words == 0:
        AvgCharPerWord = 0
    else:
        AvgCharPerWord = (Tot_Len_of_Words) / (ToTal_Legit_Words)

    return AvgSentPerParagraph, AvgCharPerWord, AvgWordPerSentence


def Flesch_Scores_calculator(AvgCharPerWord, AvgWordPerSentence):

    Flesch_Reading_Ease = 206.835 - (1.015 * AvgWordPerSentence) - (84.6 * AvgCharPerWord)
    Flesch_Kinkaid_grade_level = (0.39 * AvgWordPerSentence) + (11.8 * AvgCharPerWord) - 15.59

    return Flesch_Reading_Ease,Flesch_Kinkaid_grade_level

def paraCounter(path):
    nop=0
    counter=0
    file=load(path)
    for line in file:
        counter+=1
        wordcounter=0
        if counter>15:
            if "Original Message" in line:
                break
            for words in line:
                wordcounter+=1
            if '\n' in line and wordcounter > 10:
                nop += 1
            #print("line with count", line)
            # print("count : ", line.__len__())
    file.close()
    return nop

def day_convertor(day):
    if day=="Mon":
        day_value=1
    if day=="Tue":
        day_value=2
    if day=="Wed":
        day_value=3
    if day=="Thu":
        day_value=4
    if day=="Fri":
        day_value=5
    if day=="Sat":
        day_value=6
    if day=="Sun":
        day_value=7
    return day_value




def main(path,classifier):
    time,day = time_and_date(path)
    nop=paraCounter(path)
    sentencecounter, ToTal_Legit_Words, Tot_Len_of_Words = count_sentences_and_words(path)
    AvgSentPerParagraph, AvgCharPerWord, AvgWordPerSentence = Average(sentencecounter, ToTal_Legit_Words, Tot_Len_of_Words,nop)
    Flesch_Reading_Ease,Flesch_Kinkaid_grade_level=Flesch_Scores_calculator(AvgCharPerWord, AvgWordPerSentence)
    day_val=day_convertor(day)
    #print("no of paras : ", nop)
    #print("total no of sentences : ", sentencecounter)
    #print("total no of words in legit sentences : ", ToTal_Legit_Words)
    #print("total length of words :  ", Tot_Len_of_Words)

    #print("Time is : ", time)
    #print("day is : ", day)
    #print("Avg Sentences Per Paragraph : ", AvgSentPerParagraph, "Avg Word Per Sentence : ", AvgWordPerSentence,"Avg Char Per Word :", AvgCharPerWord)
    #print("FIESCAL SCORE : ", fiscal, " Readability : ", idk)
    entry = time, day_val, sentencecounter, ToTal_Legit_Words, Tot_Len_of_Words, nop, AvgSentPerParagraph, AvgCharPerWord, AvgWordPerSentence, Flesch_Reading_Ease, Flesch_Kinkaid_grade_level, classifier
    entry2 = str(time)+','+ str(day_val)+','+ str(sentencecounter)+','+str(ToTal_Legit_Words)+','+str(Tot_Len_of_Words)+','+str(nop)+','+str(AvgSentPerParagraph)+','+ str(AvgCharPerWord)+','+str(AvgWordPerSentence)+','+str(Flesch_Reading_Ease)+','+str(Flesch_Kinkaid_grade_level)+','+str(classifier)+'\n'
    f.write(entry2)
    #Cl_Table(entry)
    return entry

def Cl_Table(entry):
    matrix.append(entry)


#for k, v in wordcount.items():
    #print(k, v)

def fcount(path):
    #os.listdir(path)
    paths= []
    files=[]

    for f in os.listdir(path):
        # print(f)
        #print('----------------------------------------------------------------------------')
        path1 = os.path.join(path, f)
        for child in os.listdir(path1):
            count = 0
            if child == "sent_items" or child == "sent":

                # print(child)
                path2 = os.path.join(path1, child)
                #print(path2)
                paths.append(path2)
                i=0
                for gc in os.listdir(path2):
                    files.append(path2+'\\'+gc)
                    # files[count][i]=gc
                    #print(gc)
                count += 1
    #print(files)
    #print(length)
    return files

def main_call():

    files = fcount("C:/Users/sahil/Downloads/Compressed/maildir")
    counter=0
    for i in files:
        counter+=1
        if 'allen' in i:
            classifier =1
        else:
            classifier =0
        main(i,classifier)
        print(counter)

main_call()
#main("3",0)
#print(matrix)
#print(matrix.__len__())
f.close()
