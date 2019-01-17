import os
import sys
import json
import validation
from pathlib import Path
from glob import glob
import urllib2


# DEBUT Fonction permettant d'extraire les donnees du fichier json en respectant le format
def parseJSON(filePath):
    file = open(filePath)
    data = file.read()
    j = json.loads(data)
    return j
# FIN Fonction permettant d'extraire les donnees du fichier json en respectant le format


if len(sys.argv) >= 7:

    fileType = sys.argv[2]
    inputType = sys.argv[4]
    svgFile = sys.argv[7]
    myfile = sys.argv[5]

    if __name__ == "__main__":
        # Verification si le fichier en entree existe
        if inputType == '-f':
            fileName, fileExt = os.path.splitext(myfile)
            fileExt = fileExt.lower()
            if not(os.path.exists(myfile)):
                print('---Erreur: Ce fichier n\'existe pas !')
            else:
                file = open(myfile)
                data = file.read()
                if fileType == 'json':
                    # Verification de l'extention du fichier en input
                    if (fileExt != '.json'):
                        print('---Erreur: Veuillez entrer un fichier JSON')
                    else:
                        if validation.json_validator(myfile):
                            import create_svg_json
                        else:
                            print(validation.json_validator(myfile))

                elif fileType == "xml":
                    if (fileExt != '.xml'):
                        print('---Erreur: Veuillez entrer un fichier XML')
                    else:
                        if validation.xml_validator(myfile):
                            import create_svg_xml
                        else:
                            validation.xml_validator(myfile)
                else:
                    print("---Erreur: Veuillez specifier un type de fichier correct.")
                    print("---Votre choix: "+fileType)
        elif inputType == '-h':
            import create_svg_xml
        else:
            print("---Erreur: Veuillez specifier un type d'acquisition de fichier correct.")
            print("---Votre choix: "+inputType)
else:
    print('---Erreur: Nombre d\'arguments incorrect')
