from bs4 import BeautifulSoup
import requests
import pandas as pd
from googlesearch import search
import re


def googlesearch(query):
    for j in search(query, tld="com", stop=1, pause=2):
        return j


cname = input("Enter the name of a college: ")


df = pd.read_excel('data.xlsx', usecols='A,B,C')


for i in range(len(df)):
    if str(df.iloc[i, 0]) == cname.title():

        srch = str(df.iloc[i, 0]) + " " + str(df.iloc[i, 1]) + " " + str(df.iloc[i, 2]) 
        #print(srch)


        link = googlesearch(srch)
        print(link)
        html = requests.get(link)
        soup = BeautifulSoup(html.text, "html.parser")
        text = soup.text


        email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        emailmatches = []
        emailmatches = re.findall(email, text)


        for em in emailmatches:
            print(em)
