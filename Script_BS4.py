#!/usr/bin/python3
# -*- coding: utf-8 -*

import spacy
from spacy.lang.en import English
import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
import sys
import codecs


List_data=[]
response = requests.get("http://www.sport-histoire.fr/Geographie/Ordre_alphabetique.php") 
#encodedText = response.text.encode("latin-1")
soup = BeautifulSoup(response.text, "html.parser") #l'extraction des données a l'aide de la bibiothèque BeautifulSoup

for item in soup.find_all("tr"):
	text=item.get_text("td").split("td")
	List_data.append(text)
	#print(text)
	
f = codecs.open("test.txt","w", encoding="utf-8")

for line in List_data:
	line=str(line)
	f.write(line)	
	print(line)
