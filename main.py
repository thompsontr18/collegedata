from bs4 import BeautifulSoup
import requests
import pandas as pd
from googlesearch import search
import spacy
import en_core_web_sm


def googlesearch(query):
    for j in search(query, tld="com", stop=1, pause=2):
        return j

'''
cname = input("Enter the name of a college: ")
cname = "petersons college search" + cname

collegewebsite = googlesearch(cname)
print(collegewebsite)


html = requests.get(collegewebsite)
soup = BeautifulSoup(html.text, "html.parser")
print(soup.text)
listofmajors = soup.findAll("th", attrs={"class": "top-level"})

for major in listofmajors:
    print(major.text)
'''



nlp = en_core_web_sm.load()
doc = nlp("This is a sentence.")
#Code below prints out each word in sentence, along with the part of speech they are
print([(w.text, w.pos_) for w in doc])
