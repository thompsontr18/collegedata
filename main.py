from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import load_workbook
from googlesearch import search


#---------------------------------------------------------------------------------
def namechange(colname):
    name = colname.replace(" - ","-")
    name = name.replace(" -- ", "-")
    name = name.replace("- ", "-")
    name = name.replace(", ", "-")
    name = name.replace("/", "-")
    name = name.replace(" ", "-")
    name = "https://waf.collegedata.com/college-search/"+name+"/academics"
    r = requests.get(name)
    if r.status_code != 404:
        return name
    else:
        return None
#---------------------------------------------------------------------------------
def googlesearch(query):
    for j in search(query, tld="com", stop=1, pause=2):
        return j
#---------------------------------------------------------------------------------

cname = input("Enter the name of a college: ")

url = namechange(cname)
print("URL we are scraping from")
print(url)

collegewebsite = googlesearch(cname)
print("College's official URL")
print(collegewebsite)

html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
listofmajors = soup.findAll("div", attrs={"class":"SubscreenNavigator_modalData__1xYUK"})
for major in listofmajors:
    print(major.text)

li = soup.findAll("div", attrs={"class":"TitleValue_value__1JT0d"})
for l in li:
    print(l.text)

