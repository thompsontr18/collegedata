from bs4 import BeautifulSoup
import requests
import pandas as pd
from googlesearch import search
import re


def googlesearch(query):
    for j in search(query, tld="com", stop=1, pause=2):
        return j



df = pd.read_excel('data.xlsx', usecols='A,B,C')


for i in range(len(df)):
    srch = str(df.iloc[i, 0]) + " " + str(df.iloc[i, 1]) + " " + str(df.iloc[i, 2]) 
    link = googlesearch(srch)
    print(df.iloc[i, 1])
    html = requests.get(link)
    soup = BeautifulSoup(html.text, "html.parser")
    text = soup.text

    email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emailmatches = []
    emailmatches = re.findall(email, text)


    for em in emailmatches:
        print(em)
    print('-----------------------------------')
