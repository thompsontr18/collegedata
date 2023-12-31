from bs4 import BeautifulSoup
import requests
import pandas as pd
from googlesearch import search
import re



def googlesearch(query):
    for j in search(query, tld="com", stop=1, pause=2):
        return j


cname = input("Enter the name of a college: ")
altcname = cname + " faculty and staff"
cname += " faculty and staff directory"


alternatecollegewebsite = googlesearch(altcname)
althtml = requests.get(alternatecollegewebsite)
altsoup = BeautifulSoup(althtml.text, "html.parser")
alttext = altsoup.text


collegewebsite = googlesearch(cname)
html = requests.get(collegewebsite)
soup = BeautifulSoup(html.text, "html.parser")
text = soup.text

phonenumber = r'\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}'
phonenumbermatches = []
email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
emailmatches = []

phonenumbermatches = re.findall(phonenumber, text)
emailmatches = re.findall(email, text)


altpmatches = re.findall(phonenumber, alttext)
altematches = re.findall(email, alttext)



if len(altematches) + len(altpmatches) > len(emailmatches) + len(phonenumbermatches):
    print(alternatecollegewebsite, " alternate")
    for pnm, em in zip(altpmatches, altematches):
        print(pnm, em)
else:
    print(collegewebsite, " original")
    for pnm, em in zip(phonenumbermatches, emailmatches):
        print(pnm,em)
