from pprint import pprint
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

from bs4 import BeautifulSoup
import requests
import re

#nlp = en_core_web_sm.load()
nlp = spacy.load('en')

def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')

    tab =  soup.find("body")
    #on recupere les paragraphes
    li = tab.find_all("p")
    chaine=""
    for s in li:
        chaine+=s.get_text()    
    #return (li[0].get_text())
    return chaine   
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))


ny_bb = url_to_string('https://simple.wikipedia.org/wiki/Algeria').split(".")
f=open("savedFile.txt","w")

deb=""
relation=""
last=""
for e in ny_bb:
        article = nlp(e)        
        # fitrage des mots par le type GPE
        store=([(X, X.ent_iob_, X.ent_type_) for X in article if X.ent_type_=='GPE' or ])
        if(len(store)==3):
                f.write(str(store))
                pprint(store)
f.close()