import xml.etree.cElementTree as ET 
import pip
import svgwrite
import parsingXml
import XJ_Convertor
from lxml import html, etree
from shutil import copyfile
import requests

myJsonData = {}
relations = {}
if (XJ_Convertor.inputType=='-f'):
    myJsonData = parsingXml.getEntites(XJ_Convertor.myfile)
    relations = parsingXml.getRelations(XJ_Convertor.myfile)
elif (XJ_Convertor.inputType == "-h"):
    adress = requests.get(XJ_Convertor.myfile)
    fichier = open("flux.xml", "w")
    fichier.write(adress.text)
    fichier.close()
    relations = parsingXml.getRelations("flux.xml")
    myJsonData = parsingXml.getEntites("flux.xml")

listEntites = []
# Recuperation de la liste des entites
for entite in myJsonData:
    listEntites.append(entite)

# Initiation du fichier SVG
svg_document = svgwrite.Drawing(filename = XJ_Convertor.svgFile,
                                debug = True)

# Recuperation des noms des entites que l'on enregistre dans la variable "listEntites"
i=0
entityCoordsList = []
for entite in myJsonData:
    listAttributs = []
    for key in myJsonData[entite]['attributs']:
        listAttributs.append(key)
    if (i % 2 == 0):
        # Creation du rectangle contenant les infos de l'entite
        svg_document.add(svg_document.rect(insert = (10, i*150 + 10),
                                           size = ("150px", "130px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))
        entityCoords = {
            "nomEntite": listEntites[i],
            "coordX": 10,
            "coordY": i*150 + 10
        }
        entityCoordsList.append(entityCoords)  

        svg_document.add(svg_document.rect(insert = (10, i*150 + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))
  

        # Affichage du nom de l'entite
        svg_document.add(svg_document.text(listEntites[i],
            insert=(20, i*150 + 30),
            stroke='none',
            fill="rgb(42, 42, 42)",
            font_size='15px',
            font_weight="bold")
        )

        # Affichage de la liste des attributs
        for k in range(len(listAttributs)):
            svg_document.add(svg_document.text(listAttributs[k],
                insert=(20, i*150 + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )
    else:
        # Creation du rectangle contenant les infos de l'entite
        svg_document.add(svg_document.rect(insert = (400, (i - 1)*150 + 10),
                                           size = ("150px", "130px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))

        entityCoords = {
            "nomEntite": listEntites[i],
            "coordX": 400,
            "coordY": (i - 1)*150 + 10
        }
        entityCoordsList.append(entityCoords)

        svg_document.add(svg_document.rect(insert = (400, (i - 1)*150 + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))

        # Affichage du nom de l'entite
        svg_document.add(svg_document.text(listEntites[i],
            insert=(410, (i - 1)*150 + 30),
            stroke='none',
            fill="rgb(15, 15, 15)",
            font_size='15px',
            font_weight="bold")
        )

        # Affichage de la liste des attributs
        for k in range(len(listAttributs)):
            svg_document.add(svg_document.text(listAttributs[k],
                insert=(410, (i - 1)*150 + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )
    i+=1
#--------------------------------
print listEntites
participants = []
for relation in relations:
    nomAssoc = relation
    for k in range(len(listEntites)):
        if listEntites[k] in relations[relation]['multiplicite']:
            cardDeb = relations[relation]['multiplicite'][listEntites[k]]
            firstEntity = listEntites[k]
            break
    for enfant in relations[relation]['multiplicite']:
        cardFin = relations[relation]['multiplicite'][enfant]
        secondEntity = enfant
# print entityCoordsList
    debNameAssocX = 0
    debNameAssocY = 0
    for k in range(len(entityCoordsList)):
        if entityCoordsList[k]['nomEntite'] == firstEntity:
            debutLigneX = entityCoordsList[k]['coordX'] + 150
            debutLigneY = entityCoordsList[k]['coordY'] + 65
            debNameAssocX = debutLigneX + 25
            debNameAssocY = debutLigneY + 50
        if entityCoordsList[k]['nomEntite'] == secondEntity:
            finLigneX = entityCoordsList[k]['coordX'] 
            finLigneY = entityCoordsList[k]['coordY'] + 65

            svg_document.add(svg_document.line(
                (debutLigneX, debutLigneY),
                (finLigneX, finLigneY),
                stroke_width = "2", 
                stroke="rgb(15, 15, 15)"))
            
            # Affichage de la cardinalite depart
            svg_document.add(svg_document.text(cardDeb,
                insert=(debutLigneX, debutLigneY - 10),
                stroke='none',  
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )

            # Affichage de la cardinalite arrivee
            svg_document.add(svg_document.text(cardFin,
                insert=(finLigneX - 50, finLigneY - 10),
                stroke='none',  
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )

            # Affichage du nom de l'association
            svg_document.add(svg_document.text(nomAssoc,
                insert=((finLigneX - debutLigneX) / 2 + debutLigneX - 40 , finLigneY - 10),
                stroke='none',  
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )
# # ---------------
svg_document.save()

