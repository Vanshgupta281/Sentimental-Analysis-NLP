#DATA ANALYSIS#
import numpy as np
import pandas as pd
import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize

stop_words = []
positive_words = []
negative_words = []

vowels = ['a','e','i','o','u']
punct = ["'",'!','.','?',';']
pronouns = r'\b(I|me|my|mine|we|us|our|ours|you|your|yours|he|him|his|she|her|hers|it|its|they|them|their|theirs)\b'

POSITIVESCORE = []
NEGATIVESCORE  = []
POLARITYSCORE = []
SUBJECTIVITYSCORE = []
AVGSENTENCELENGTH = []
PERCENTCOMPLEX = []
FOGINDEX = []
AVGNUMWORDS_SENTENCE = []
COMPLEXWORDS = []
WORDCOUNT = []
SYLLABLEPERWORD = []
PRONOUNCOUNT = []
AVGWORDLENGTH = []


Output_file = pd.read_excel('/Users/vanshgupta/Downloads/Output Data Structure.xlsx')
df=pd.DataFrame({'URL_ID':[],	'URL':[],	'POSITIVE SCORE':[],	'NEGATIVE SCORE':[],	'POLARITY SCORE':[],	'SUBJECTIVITY SCORE':[],	'AVG SENTENCE LENGTH':[],	'PERCENTAGE OF COMPLEX WORDS':[],	'FOG INDEX':[],	'AVG NUMBER OF WORDS PER SENTENCE':[], 'COMPLEX WORD COUNT':[],	'WORD COUNT':[], 'SYLLABLE PER WORD':[],	'PERSONAL PRONOUNS':[],	'AVG WORD LENGTH':[]})
df=Output_file.copy()

with open('/Users/vanshgupta/Downloads/MasterDictionary/negative-words.txt','r', encoding='Windows-1252') as file:
    for line in file:
        line = line.strip()
        negative_words.append(line) 
with open('/Users/vanshgupta/Downloads/MasterDictionary/positive-words.txt','r', encoding='Windows-1252') as file:
    for line in file:
        line = line.strip()
        positive_words.append(line)   
with open('/Users/vanshgupta/Downloads/StopWords/StopWords_Auditor.txt','r', encoding='Windows-1252') as file:
     for line in file:
        line = line.strip()
        stop_words.append(line)
with open('/Users/vanshgupta/Downloads/StopWords/StopWords_Currencies.txt','r', encoding='Windows-1252') as file:
     for line in file:
        line = line.strip()
        stop_words.append(line)  
with open('/Users/vanshgupta/Downloads/StopWords/StopWords_DatesandNumbers.txt','r', encoding='Windows-1252') as file:
     for line in file:
        line = line.strip()
        stop_words.append(line)    
with open('/Users/vanshgupta/Downloads/StopWords/StopWords_Generic.txt','r', encoding='Windows-1252') as file:
     for line in file:
        line = line.strip()
        stop_words.append(line)    
with open('/Users/vanshgupta/Downloads/StopWords/StopWords_GenericLong.txt','r', encoding='Windows-1252') as file:
     for line in file:
        line = line.strip()
        stop_words.append(line)
with open('/Users/vanshgupta/Downloads/StopWords/StopWords_Geographic.txt','r', encoding='Windows-1252') as file:
     for line in file:
        line = line.strip()
        stop_words.append(line)    
with open('/Users/vanshgupta/Downloads/StopWords/StopWords_Names.txt','r', encoding='Windows-1252') as file:
     for line in file:
        line = line.strip()
        stop_words.append(line)   

input_files = pd.read_excel('/Users/vanshgupta/Downloads/Input.xlsx')
urls = input_files['URL']
for i in range(len(urls)):
   file_name = input_files['URL_ID'][i]
   file_path = '/Users/vanshgupta/Documents/TEXTFILES/{}.txt'.format(file_name)
   with open(file_path,'r') as file:
     text = file.read()
     matches = re.findall(pronouns, text)
     sentences_of_article = sent_tokenize(text)
     words_of_article = word_tokenize(text)
   pronoun_count = len(matches)
   total_char = 0
   for i in range(len(words_of_article)):
     total_char = total_char + len(words_of_article[i])    
   Clean_article = [word for word in words_of_article if word.lower() not in stop_words]
   Cleaned_words = [word for word in Clean_article if word not in punct]
   Syllable_per_word = 0
   PositiveScore = 0
   NegativeScore = 0
   ComplexWords = 0
   for word in words_of_article:
       WordLetters = []
       for letter in word:
           WordLetters.append(letter)
       Syllable = 0
       for letter in WordLetters:
         if letter in vowels:
            Syllable = Syllable + 1
       reverseword = word[::-1]
       
       if ((reverseword[0]=='d'or reverseword[0]=='s') and len(word)>1 and reverseword[1]=='e'):
        Syllable = Syllable - 1
       Syllable_per_word = Syllable_per_word+(Syllable)
       if Syllable > 2:
        ComplexWords = ComplexWords+1
   for word in Clean_article:
       if word in positive_words:
           PositiveScore = PositiveScore + 1
       if word in negative_words:
           NegativeScore = NegativeScore + 1
           
   POSITIVESCORE.append(PositiveScore)
   NEGATIVESCORE.append(NegativeScore)
   
   PolarityScore = (PositiveScore-NegativeScore)/((PositiveScore+NegativeScore)+0.000001)
   POLARITYSCORE.append(PolarityScore)
   
   SubjectivityScore = (PositiveScore+NegativeScore)/((len(Cleaned_words))+0.000001)
   SUBJECTIVITYSCORE.append(SubjectivityScore)
   
   AverageSentenceLength = len(words_of_article)/len(sentences_of_article)
   AVGSENTENCELENGTH.append(AverageSentenceLength)
   
   PercentComplex = ComplexWords/len(words_of_article)
   PERCENTCOMPLEX.append(PercentComplex)
   
   FogIndex = 0.4*(PercentComplex+AverageSentenceLength)
   FOGINDEX.append(FogIndex)
   
   COMPLEXWORDS.append(ComplexWords)
   
   AvgNumWordsperSentence = len(words_of_article)/len(sentences_of_article)
   AVGNUMWORDS_SENTENCE.append(AvgNumWordsperSentence)
   
   AverageWordLength = total_char/len(words_of_article)
   AVGWORDLENGTH.append(AverageWordLength)
   
   WORDCOUNT.append(len(Cleaned_words))
   
   PRONOUNCOUNT.append(pronoun_count)
   
   SYLLABLEPERWORD.append(Syllable_per_word/len(Cleaned_words))
   
df['POSITIVE SCORE']=POSITIVESCORE
df['NEGATIVE SCORE']=NEGATIVESCORE
df['POLARITY SCORE']=POLARITYSCORE
df['SUBJECTIVITY SCORE']=SUBJECTIVITYSCORE
df['AVG SENTENCE LENGTH']=AVGSENTENCELENGTH
df['PERCENTAGE OF COMPLEX WORDS']=PERCENTCOMPLEX
df['FOG INDEX']=FOGINDEX
df['AVG NUMBER OF WORDS PER SENTENCE']=AVGNUMWORDS_SENTENCE
df['COMPLEX WORD COUNT']=COMPLEXWORDS
df['WORD COUNT']=WORDCOUNT
df['SYLLABLE PER WORD']=SYLLABLEPERWORD
df['PERSONAL PRONOUNS']=PRONOUNCOUNT
df['AVG WORD LENGTH']=AVGWORDLENGTH

path = '/Users/vanshgupta/Downloads/Output.xlsx'
df.to_excel(path,index=False)
####################