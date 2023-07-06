from openpyxl import load_workbook
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

nlp = en_core_web_sm.load()

doc = nlp('Trevor Thompson and Mohith Jothi work at Cloudera Inc and they both have $500 in their wallet with a 23% chance of rain today')
print("Spacy ---")
print([(X.text, X.label_) for X in doc.ents])

#-------------------------------------------------------------------------------------------------------------------
import nltk

'''
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
'''

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

text = 'Trevor Thompson and Mohith Jothi work at Cloudera Inc and they both have $500 in their wallet with a 23% chance of rain today'
print("NLTK ---")


nltk_results = ne_chunk(pos_tag(word_tokenize(text)))
for nltk_result in nltk_results:
    if type(nltk_result) == Tree:
        name = ''
        for nltk_result_leaf in nltk_result.leaves():
            name += nltk_result_leaf[0] + ' '
        print ([(name, nltk_result.label())], end = " ")
print()