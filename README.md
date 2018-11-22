@creators: 
° Mohammed BENAOU
° Anass Abdellaoui

Description d'ontologie:

La première étape de l'écriture de l'ontologie OWL, on apprend que la propriété habite a pour domaine la classe 
personne et pour image la classe ville : elle relie des instances de la classe personne à des
instances de la classe Pays. Une ville se localise dans un pays et cette dernière appartient à un continent.
La population que l'on souhaite décrire est composée de personnes, divisés en deux sous-classes
Homme et Femme, et habitant dans une certaine ville. Un homme et une femme peuvent être mariés.

Pour aller loin dans le scraping qu'on souhaité faire, on est basé sur la bibliothèque BeautifulSoup écrite en Python, que j’ai personnalisé pour l’adapter à nos besoins.
Cette bibliothèque logicielle peut aussi être utilisée pour traiter du XML.
La bibliothèque Beautiful Soup permet de naviguer au sein de l’arbre créé
par le parser, de chercher des éléments dans cet arbre ou les modifier.
Lorsque le document XML/HTML soumis est mal formé, Beautiful Soup propose une approche à base d’heuristiques afin de reconstituer automatiquement l’arbre sans générer d’erreur. 
J’ai choisi les quatre sources d’information en ligne suivantes :

- https://www.eguens.com/v2/capitales/liste-capitales-afrique.php
- http://www.sport-histoire.fr/Geographie/Ordre_alphabetique.php
- https://simple.wikipedia.org/wiki/Algeria (exemple Algerie)



Notre stratégie est de partir sur les deux senses en utilisant à la fois Beautiful Soup pour une partie de l'ontologie et Spacy pour l'autre parie. 

#Réalisation:
- Avec Spacy(Script_Spacy.py): On récupére le texte de page en multi-paragraphes et on localise les entités nommées dans du texte en catégories prédéfinies en appliquant la tokénisation des mots.

- Avec Beautiful Soup(Script_BS4.py): Aprés la prise de connaissance des sources de données, on a  pu déterminer pour chaqu'une de nos sources, un moyen pour récupérer ses informations. Les données sont présentées sous forme d'une tableau alors que la sortie est un fichier text qui se repose sur la même strécture. 

#Perspective: 
- On a du mal a récupérer les informations pour peupler la partie de la classe personne de notre ontologie.




# web3-ner-MohammedBenaou
