import os
import sys
import json
from pathlib import Path
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from glob import glob

print('Bonjour ! Bienvenue')

# DEBUT Fonction de validation du fichier JSON
def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("Le fichier JSON n'est pas valide: %s" % error)
        return False
# FIN Fonction de validation du fichier JSON

# DEBUT Fonction de validation du fichier XML
def xml_validator(file):
    try:
        parsefile(file)
        print ("Le fichier %s est bien formatté" % myfile)
        return True
    except Exception as e:
        print ("---Erreur: Le fichier %s n'est pas bien formatté ! " % myfile)
        print("Voici l'erreur: %s" % e)
        return False
# FIN Fonction de validation du fichier XML

# DEBUT fonction
def parsefile(file):
    parser = make_parser(  )
    parser.setContentHandler(ContentHandler(  ))
    parser.parse(file)
# FIN fonction

fileType = sys.argv[2]
inputType = sys.argv[3]
myfile = sys.argv[4]
fileName, fileExt = os.path.splitext(myfile)
fileExt = fileExt.lower()

# Verification si le fichier en entree existe
if not(os.path.exists(myfile)):
    print('---Erreur: Ce fichier n\'existe pas !')
else:
    if inputType == '-f':
        file = open(myfile)
        data = file.read()
        if fileType == 'json':
            # Verification de l'extention du fichier en input
            if (fileExt != '.json'):
                print('---Erreur: Veuillez entrer un fichier JSON')
            else:
                print(json_validator(data))
        elif fileType == "xml":
            if (fileExt != '.xml'):
                print('---Erreur: Veuillez entrer un fichier XML')
            else:
                xml_validator(myfile)
        else:
            print("---Erreur: Veuillez specifier un type de fichier correct.")
            print("---Votre choix: "+fileType)
    elif inputType == '-h':
        print('Methode http')
    else:
        print("---Erreur: Veuillez specifier un type d'acquisition de fichier correct.")
        print("---Votre choix: "+inputType)
