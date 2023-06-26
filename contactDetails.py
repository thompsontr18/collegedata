from bs4 import BeautifulSoup
import requests
from googlesearch import search
import re


def googlesearch(query):
    result = []
    for j in search(query, tld="com", stop=1, pause=2):
        result.append(j)
    return result


inputCname = input("Enter the name of a college: ")
inputCname += "faculty contact details list"
searchResults = googlesearch(inputCname)

for i in range(0, len(searchResults)):
    website = searchResults[i]
    html = requests.get(website)
    soup = BeautifulSoup(html.text, "html.parser")
    websiteText = soup.text
    # print(websiteText)
    phonenumber = r'\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}'
    email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    phonematch = re.findall(phonenumber, websiteText)
    emailmatch = re.findall(email, websiteText)
    print(website)
    for pno in phonematch:
        print(pno)
    for em in emailmatch:
        print(em)
        emailsearch = googlesearch(em)
        print(emailsearch)
    print('---------------------------------')
    break


# html = requests.get(collegewebsite)
# soup = BeautifulSoup(html.text, "html.parser")
# text = soup.text

# cname = input("Enter the name of a college: ")
# altcname = cname + " faculty and staff"
# cname += " faculty and staff directory"


# alternatecollegewebsite = googlesearch(altcname)
# althtml = requests.get(alternatecollegewebsite)
# altsoup = BeautifulSoup(althtml.text, "html.parser")
# alttext = altsoup.text


# collegewebsite = googlesearch(cname)
# html = requests.get(collegewebsite)
# soup = BeautifulSoup(html.text, "html.parser")
# text = soup.text

# phonenumber = r'\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}'
# phonenumbermatches = []
# email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
# emailmatches = []

# phonematch = re.findall(phonenumber, text)
# if phonematch:
#     phonenumbermatches.extend(phonematch)
# emailmatch = re.findall(email, text)
# if emailmatch:
#     emailmatches.extend(emailmatch)


# altpmatches = []
# altematches = []
# altphonematch = re.findall(phonenumber, alttext)
# if altphonematch:
#     altpmatches.extend(altphonematch)
# altemailmatch = re.findall(email, alttext)
# if altemailmatch:
#     altematches.extend(altemailmatch)


# if len(altematches) + len(altpmatches) > len(emailmatches) + len(phonenumbermatches):
#     print(alternatecollegewebsite, " alternate")
#     for pnm, em in zip(altpmatches, altematches):
#         print(pnm, em)

# else:
#     print(collegewebsite, " original")
#     for pnm, em in zip(phonenumbermatches, emailmatches):
#         print(pnm,em)
