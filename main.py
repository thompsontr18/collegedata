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
text = ("When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously. I can tell you very senior CEOs of major American car companies would shake my hand and turn away because I wasn’t worth talking to, said Thrun, in an interview with Recode earlier this week.")
doc = nlp(text)

#gets parts of speech
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("\n")
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
print("\n")

#understands people, places, things, etc
for entity in doc.ents:
    print(entity.text, entity.label_)
