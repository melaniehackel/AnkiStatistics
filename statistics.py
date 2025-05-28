# spacy, nltk
import spacy
import nltk
import matplotlib.pyplot as plt
import numpy as np


words = ["I", "9", "Boy", "Bitter"]
words_with_pos = {}

# POS tagging
nlp = spacy.load('en_core_web_sm')
for word in words:
    tag = nlp(word)
    for token in tag:
        # print(token.text, token.pos_)
        words_with_pos[token.text] = token.pos_

print(words_with_pos)

# Statistics
# Pie chart