from openpyxl import load_workbook
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

doc = nlp('The random guy took Tilly and Daisy on a walk to Andrew Jones College. After that, John Smith went shopping')
print([(X.text, X.label_) for X in doc.ents])