#DATA EXTRACTION#
import pandas as pd
from bs4 import BeautifulSoup
import requests
input_files = pd.read_excel('/Users/vanshgupta/Downloads/Input.xlsx')          #openpyxl required#
urls = input_files['URL']
for i in range(len(urls)):  
   file_name = input_files['URL_ID'][i]
   file_path = '/Users/vanshgupta/Documents/TEXTFILES/{}.txt'.format(file_name)
   response = requests.get(urls[i])
   soup = BeautifulSoup(response.content, 'html.parser')  
   article_title = soup.title.string
   article_text = soup.find_all('p')
   with open(file_path, 'w') as file:
      file.write('{}'.format(article_title))
      for i in range(16,len(article_text)-3):
       file.write('{}'.format(article_text[i].get_text()))
###################
