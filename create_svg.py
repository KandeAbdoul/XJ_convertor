import pip
import svgwrite
import XJ_Convertor

myJsonData = XJ_Convertor.parseJSON(XJ_Convertor.myfile)

listEntites = []
# Recuperation de la liste des entités

for i in range(len(myJsonData)):
    for key in myJsonData[i].keys():
        listEntites.append(key)


# Initiation du fichier SVG
svg_document = svgwrite.Drawing(filename = XJ_Convertor.svgFile,
                                debug = True)

entityCoordsList = []
# Recuperation des noms des entités que l'on enregistre dans la variable "listEntites"
print('Liste des entites et leurs attributs: ')
for i in range(len(listEntites)):
    listAttributs = []
    listAssocs = []

    # Recuperation des noms des attributs que l'on enregistre dans la variable "listAttributs"
    nbAttributs = len(myJsonData[i][listEntites[i]]['attributs'])
    print('\t' + listEntites[i])
    for j in range(nbAttributs):
        for key in myJsonData[i][listEntites[i]]['attributs'][j].keys():
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

        svg_document.add(svg_document.line(
            (550,  (i - 1)*150 + 10),
            (100, 100),
            stroke_width = "2",
            stroke="rgb(15, 15, 15)"))

    # Recuperations des differentes associations
    nbAssocs = len(myJsonData[i][listEntites[i]]['relations']['associations'])
    for j in range(nbAssocs):
        # for key in myJsonData[i][listEntites[i]]['relations']['associations'][j].keys():
        #     listAssocs.append(key)
        #     print(key)
        nomAutreEntite = myJsonData[i][listEntites[i]]['relations']['associations'][j]["nomAutreEntite"]
        for k in range(len(entityCoordsList)):
            if entityCoordsList[k]['nomEntite'] == nomAutreEntite:
                print('Yeeeeeeeaah')
# ---------------

# print(entityCoordsList)
# print(svg_document.tostring())

svg_document.save()
