from bs4 import BeautifulSoup
import requests
import pandas as pd
from googlesearch import search
import re


def googlesearch(query):
    for j in search(query, tld="com", stop=1, pause=2):
        return j



df = pd.read_excel('data.xlsx', usecols='A,B,C')


major = ""
collegeandmajor = {}
for i in range(len(df)):
    srch = str(df.iloc[i, 0]) + " " + str(df.iloc[i, 1])
    if df.iloc[i,0]=="Albany Technical College" or df.iloc[i,0]=="Andrew College":
        continue
    if (df.iloc[i, 0], df.iloc[i, 1]) in collegeandmajor:
        continue
    srch += " program contact"
    link = googlesearch(srch)
    if major != df.iloc[i, 1]:
        print('-----------------------------------')
        print(df.iloc[i, 1])
        major = df.iloc[i, 1]
        collegeandmajor[(df.iloc[i, 0], df.iloc[i, 1])] = 1


    html = requests.get(link)
    soup = BeautifulSoup(html.text, "html.parser")
    text = soup.text

    emailre = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emailmatches = []
    emailmatches = re.findall(emailre, text)


    if len(emailmatches) == 0:
        print("N/A")
        print("No Contact Details")
        continue
    printedtext = ""
    for i in range(0,len(emailmatches)):
        if i != len(emailmatches)-1:
            printedtext += emailmatches[i] + ", "
        else:
            printedtext += emailmatches[i]
    print(printedtext)
    for i in range(0,len(emailmatches)):
        details=text.split(emailmatches[i])[0]
        print(details[-150:])
