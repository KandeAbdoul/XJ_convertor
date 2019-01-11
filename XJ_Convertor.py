import os
import sys
import json
import validation


# DEBUT Fonction permettant d'extraire les donnees du fichier json en respectant le format
def parseJSON(filePath):
    file = open(filePath)
    data = file.read()
    j = json.loads(data)
    return j
# FIN Fonction permettant d'extraire les donnees du fichier json en respectant le format

if len(sys.argv) == 7:

    fileType = sys.argv[2]
    inputType = sys.argv[3]
    
    if inputType == '-h':
        url = sys.argv[4]
    elif inputType == '-f':
        myfile = sys.argv[4]
        fileName, fileExt = os.path.splitext(myfile)
        fileExt = fileExt.lower()

    svgFile = sys.argv[6]    

    if __name__ == "__main__":
        if inputType == '-f':
            # Verification si le fichier en entree existe
            if not(os.path.exists(myfile)):
                print('---Erreur: Ce fichier n\'existe pas !')
            else:
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
                            print('Traitement du fichier XML')
                        else:
                            validation.xml_validator(myfile)
                else:
                    print("---Erreur: Veuillez specifier un type de fichier correct.")
                    print("---Votre choix: "+fileType)
                
        elif inputType == '-h':
                    url = sys.argv[4]
                    print(url)
                    if fileType == 'json':                      
                        import create_svg_json
        else:
                    print("---Erreur: Veuillez specifier un type d'acquisition de fichier correct.")
                    print("---Votre choix: "+inputType)
else:
    print('---Erreur: Nombre d\'arguments incorrect')
