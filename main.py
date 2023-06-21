from googlesearch import search
from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import load_workbook



def googlesearch():
    query = input("What would you like to search for? ")
    for j in search(query, tld="co.in", stop=1, pause=2):
        return j


url = googlesearch()
print(url)
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
print(soup.text)



