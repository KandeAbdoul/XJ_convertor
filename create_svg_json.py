import pip
import svgwrite
import XJ_Convertor
import requests

if XJ_Convertor.inputType == '-f':
    myJsonData = XJ_Convertor.parseJSON(XJ_Convertor.myfile)
elif XJ_Convertor.inputType == '-h':
    response = requests.get(url = XJ_Convertor.url)
    myJsonData = response.json()  
    
listEntites = []
# Recuperation de la liste des entités

for i in range(len(myJsonData)):
    keys = myJsonData[i].keys()
    key = next(iter(keys))
    listEntites.append(key)
    print(key)


# Initiation du fichier SVG
svg_document = svgwrite.Drawing(filename = XJ_Convertor.svgFile,
                                debug = True)

entityCoordsList = []
# Recuperation des noms des entités que l'on enregistre dans la variable "listEntites"
print('Liste des entites et leurs attributs: ')
for i in range(len(listEntites)):
    listAttributs = []
    listAssocs = []

    print('\t' + listEntites[i])

    # Recuperation des noms des attributs que l'on enregistre dans la variable "listAttributs"
    nbAttributs = len(myJsonData[i][listEntites[i]][0].keys())
    
    for key in myJsonData[i][listEntites[i]][0].keys():
        listAttributs.append(key)
        print('\t\t' + key)

    
    if (i % 2 == 0):
        # Creation du rectangle contenant les infos de l'entité
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
        

        # Affichage du nom de l'entité
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
        # Creation du rectangle contenant les infos de l'entité
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

        

        # Affichage du nom de l'entité
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

# ---------------

# print(svg_document.tostring())

for i in range(len(listEntites)):
    # Recuperations des differentes associations
    nbAssocs = len(myJsonData[i]['relations']['associations'])
    
    for j in range(nbAssocs):
            # for key in myJsonData[i][listEntites[i]]['relations']['associations'][j].keys():
            #     listAssocs.append(key)
            #     print(key)
            nomAutreEntite = myJsonData[i]['relations']['associations'][j]["nomAutreEntite"]
            # cardDeb = myJsonData[i][listEntites[i]]['relations']['associations'][j]["cardDeb"]
            # cardFin = myJsonData[i][listEntites[i]]['relations']['associations'][j]["cardFin"]
            nomAssoc = myJsonData[i]['relations']['associations'][j]["nomAssoc"]

            for k in range(len(entityCoordsList)):
                if entityCoordsList[k]['nomEntite'] == listEntites[i]:
                    for p in range(len(entityCoordsList)):
                        if entityCoordsList[p]['nomEntite'] == nomAutreEntite:
                            if entityCoordsList[i]['coordX'] == entityCoordsList[p]['coordX']:                               
                                debutLigneX = entityCoordsList[k]['coordX'] + 75
                                debutLigneY = entityCoordsList[k]['coordY'] + 130
                            elif entityCoordsList[i]['coordY'] == entityCoordsList[p]['coordY']:
                                debutLigneX = entityCoordsList[k]['coordX'] + 150
                                debutLigneY = entityCoordsList[k]['coordY'] + 65


                if entityCoordsList[k]['nomEntite'] == nomAutreEntite:
                    for p in range(len(entityCoordsList)):
                        if entityCoordsList[p]['nomEntite'] == nomAutreEntite:
                            if entityCoordsList[i]['coordX'] == entityCoordsList[p]['coordX']:
                                finLigneX = entityCoordsList[k]['coordX'] + 5
                                finLigneY = entityCoordsList[k]['coordY']
                            elif entityCoordsList[i]['coordY'] == entityCoordsList[p]['coordY']:
                                finLigneX = entityCoordsList[k]['coordX']
                                finLigneY = entityCoordsList[k]['coordY'] + 65

                    svg_document.add(svg_document.line(
                        (debutLigneX, debutLigneY),
                        (finLigneX, finLigneY),
                        stroke_width = "2",
                        stroke="rgb(15, 15, 15)"))
                    
                    # # Affichage de la cardinalité depart
                    # svg_document.add(svg_document.text(cardDeb,
                    #     insert=(debutLigneX + 10, debutLigneY - 10),
                    #     stroke='none',  
                    #     fill="rgb(15, 15, 15)",
                    #     font_size='15px',
                    #     font_weight="bold")
                    # )

                    # # Affichage de la cardinalité arrivée
                    # svg_document.add(svg_document.text(cardFin,
                    #     insert=(finLigneX - 30, finLigneY - 10),
                    #     stroke='none',  
                    #     fill="rgb(15, 15, 15)",
                    #     font_size='15px',
                    #     font_weight="bold")
                    # )

                    # Affichage du nom de l'association
                    svg_document.add(svg_document.text(nomAssoc,
                        insert=((finLigneX - debutLigneX) / 2 + debutLigneX - 30, finLigneY - 10),
                        stroke='none',  
                        fill="rgb(15, 15, 15)",
                        font_size='15px',
                        font_weight="bold")
                    )

svg_document.save()
