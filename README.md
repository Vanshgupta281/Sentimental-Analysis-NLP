# Sentimental-Analysis-NLP
DATA EXTRACTION
Instructions
● Firstly we need to have the required libraries and modules. Pandas being our main library for handling data, Beautiful Soup and requests for data extraction from URLs and Openpyxl for interacting with excel files using pandas.
● So we’ll start by reading the input excel file using pandas and then we’ll use requests to get the requested page. Then Beautiful Soup will be used to extract the title and then all the paragraph (p) tags. I noticed from inspecting the articles
that the main article texts have p tags along with some text in header and footer,
so I observed from inspecting that first 16 p tags and last 3 p tags are not from
main article text. Then I created a folder named TEXTFILES which will contain all
the text (title and main article) extracted from all articles and name of all these
text files will be URL id provided to us. This is achieved with this line of code
                      file_name = input_files['URL_ID'][i]
Now when we extract the text using beautifulsoup, we get that text and write it into the text file with title as URL id and save it.
DATA ANALYSIS
● For all the target variables, we create a list of vowels, punctuation, and personal pronouns
● Now we start with creating the lists which we need to fill the values with (POSITIVESCORE, NEGATIVESCORE etc.). We also create the stopwords empty list and then read from the text files the stopword given to us and append all these stopwords separated by Space/Line Break. Similarly we will create list of Positive and Negative words from the text file of those words provided to us.
● We also create a dataframe df which we’ll keep to store the variables which we will evaluate, it will have the same columns and data as the output file given to us.
● Now we’ll start reading the files in TEXTFILES with text of each article, convert it to list of tokens using nltk tokenize (both word and sentence tokenize) and then check how many of the words in that text are also found in Positive Words list and how many are found in Negative words list. This way we’ll get the positive and negative score.
● For checking the syllable count and complexity we break down each word to its characters and then check for vowels and ‘es’ and ‘ed’ cases as well.
