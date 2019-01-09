import json
from xml.sax.handler import ContentHandler
from xml.sax import make_parser

# DEBUT Fonction de validation du fichier JSON
def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("Le fichier JSON n'est pas valide: %s" % error)
        return False
# FIN Fonction de validation du fichier JSON


# DEBUT fonction d'analyse du fichier XML
def parsefile(file):
    parser = make_parser(  )
    parser.setContentHandler(ContentHandler(  ))
    parser.parse(file)
# FIN fonction d'analyse du fichier XML

# DEBUT Fonction de validation du fichier XML
def xml_validator(file):
    try:
        parsefile(file)
        return True
    except Exception as e:
        print "le fichier ", file, "n'est pas bien formate"
        print("Voici l'erreur: %s" % e)
        return False
# FIN Fonction de validation du fichier XML