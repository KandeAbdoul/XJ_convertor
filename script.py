import xml.etree.cElementTree as ET 
import sys 

datas = sys.argv[1]
files = ET.ElementTree(file = datas)
root = files.getroot()
#objet qui va recuperer les entitees et les attributs
entites = {}  
#objet qui va recuperer les classes heritieres
class_herit = {}    
#objet qui va recuperere les classes stereotypees
stereotype = {}     
for nodes in root.iter('complexType') : 
    for child in nodes:
        if child.tag == "sequence": # permet de verifier si c'est une classe
            print nodes.attrib['name'],'(' #afficher le nom de la classe
            entites.update({nodes.attrib['name']:{'attributs':{}}}) #inserer le nom dans entites en initialisants ses attibuts a vide
            for attribut in child:
                entites[nodes.attrib['name']]['attributs'].update({attribut.attrib['name']:attribut.attrib['type']}) #recupere l'ensemble de ses attributs
                print '\t',attribut.attrib['name'],':',attribut.attrib['type']
            print ')\n\n'
        elif child.tag == "complexContent": #verifier si c une classe heritiere
            print nodes.attrib['name'],'('
            for attribut in child:
                elem = attribut.find('element') #recuperer verifier s'il a un enfant de type <element>
                if elem != None: #si oui
                    class_herit.update({nodes.attrib['name']:{'attributs':{}}}) #inserer le nom dans class_herit{}
                    for element in attribut:
                        class_herit[nodes.attrib['name']]['attributs'].update({element.attrib['name']:element.attrib['type']}) #recuperer l'ensemble des ses attributs
                        print '\t',element.attrib['name'],':', element.attrib['type']
                else: #si non
                    print "\therite de", attribut.attrib['base'] #afficher de quelle classe elle herite
                print ')\n'
        elif child.tag == "simpleContent": #verifier si c'est une classe permet de declarer un type de donnees
            print '<<stereotype>> ',nodes.attrib['name'],'('
            stereotype.update({nodes.attrib['name']:{'attributs':{}}})
            for attributs in child:
                for attribut in attributs:
                    stereotype[nodes.attrib['name']]['attributs'].update({attribut.attrib['name']:attribut.attrib['type']}) #recuperer l'ensemble des ses attributs
                    print '\t',attribut.attrib['name'],':',attribut.attrib['type'] 
                print ')\n'
print entites,'\n\nclasse heritiere'
print class_herit,'\n\n stereotype'
print stereotype 
