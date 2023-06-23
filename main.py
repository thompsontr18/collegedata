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



collegewebsite = googlesearch(cname)
print(collegewebsite)


alternatecollegewebsite = googlesearch(altcname)
althtml = requests.get(alternatecollegewebsite)
altsoup = BeautifulSoup(althtml.text, "html.parser")
alttext = altsoup.text


html = requests.get(collegewebsite)
soup = BeautifulSoup(html.text, "html.parser")
text = soup.text

phonenumber = r'\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}'
phonenumbermatches = []
email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
emailmatches = []

phonematch = re.findall(phonenumber, text)
if phonematch:
    phonenumbermatches.extend(phonematch)
emailmatch = re.findall(email, text)
if emailmatch:
    emailmatches.extend(emailmatch)


altpmatches = []
altematches = []
altphonematch = re.findall(phonenumber, alttext)
if altphonematch:
    altpmatches.extend(altphonematch)
altemailmatch = re.findall(email, alttext)
if altemailmatch:
    altematches.extend(altemailmatch)


if len(altematches) + len(altpmatches) > len(emailmatches) + len(phonenumbermatches):
    print(alternatecollegewebsite)
    for pnm, em in zip(altematches, altpmatches):
        print(pnm, em)

else:
    print(collegewebsite)
    for pnm, em in zip(phonenumbermatches, emailmatches):
        print(pnm,em)
