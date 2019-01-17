import xml.etree.cElementTree as ET 
import sys 

#Debut fonction qui va recupere les entitees
def getEntites(fichier):
    files = ET.ElementTree(file = fichier)
    root = files.getroot()
    entites = {}
    for nodes in root.iter('complexType') : 
        for child in nodes:
            if child.tag == "sequence": # permet de verifier si c'est une classe
                print (nodes.attrib['name'],'(') #afficher le nom de la classe
                entites.update({nodes.attrib['name']:{'attributs':{}}}) #inserer le nom dans entites en initialisants ses attibuts a vide
                for attribut in child:
                    entites[nodes.attrib['name']]['attributs'].update({attribut.attrib['name']:attribut.attrib['type']}) #recupere l'ensemble de ses attributs
                    print ('\t',attribut.attrib['name'],':',attribut.attrib['type'])
                print (')\n\n')
    return entites
#Fin de la fonction 

#Debut de la fonction qu va recuperer les entitees heritieres
def getHeritEntites(fichier):
    files = ET.ElementTree(file = fichier)
    root = files.getroot()
    class_herit = {}
    for nodes in root.iter('complexType') : 
        for child in nodes:
            for nodes in root.iter('complexType') : 
                for child in nodes:
                    if child.tag == "complexContent": #verifier si c une classe heritiere
                        print (nodes.attrib['name'],'(')
                        for attribut in child:
                            elem = attribut.find('element') #recuperer verifier s'il a un enfant de type <element>
                            if elem != None: #si oui
                                class_herit.update({nodes.attrib['name']:{'attributs':{}}}) #inserer le nom dans class_herit{}
                                for element in attribut:
                                    class_herit[nodes.attrib['name']]['attributs'].update({element.attrib['name']:element.attrib['type']}) #recuperer l'ensemble des ses attributs
                                    print ('\t',element.attrib['name'],':', element.attrib['type'])
                            else: #si non
                                print ("\therite de", attribut.attrib['base']) #afficher de quelle classe elle herite
                            print (')\n')
    return class_herit
#Fin de la fonction 

#Debut de la fonction qui va recuperer les classes stereotypes
def FunctionName(fichier):
    files = ET.ElementTree(file = fichier)
    root = files.getroot()
    stereotypes = {}
    for nodes in root.iter('complexType') : 
        for child in nodes:
            if child.tag == "simpleContent": #verifier si c'est une classe permet de declarer un type de donnees
                print ('<<stereotype>> ',nodes.attrib['name'],'(')
                stereotypes.update({nodes.attrib['name']:{'attributs':{}}})
                for attributs in child:
                    for attribut in attributs:
                        stereotypes[nodes.attrib['name']]['attributs'].update({attribut.attrib['name']:attribut.attrib['type']}) #recuperer l'ensemble des ses attributs
                        print ('\t',attribut.attrib['name'],':',attribut.attrib['type']) 
                    print(')\n')
    return stereotypes

#Fin de la fonction

#Debut de la fonction qui va recuperer les relations et leurs multiplicites
def getRelations(fichier):
    files = ET.ElementTree(file = fichier)
    root = files.getroot()
    relations = {}
    for nodes in root.iter('complexType') :
        for child in nodes:
            if child.tag == "relation": # permet de verifier si c'est une classe
                relations.update({child.attrib['name']:{'multiplicite':{}}}) #inserer le nom dans entites en initialisants ses attibuts a vide
                for attribut in child:
                    for seq in attribut:
                        relations[child.attrib['name']]['multiplicite'].update({seq.attrib['name']:(seq.attrib['minOccurs'],seq.attrib['maxOccurs'])})
    return relations

#fin de la fonction