import pip
import svgwrite
import XJ_Convertor

myJsonData = XJ_Convertor.parseJSON(XJ_Convertor.myfile)

listEntites = []
for i in range(len(myJsonData)):
    for key in myJsonData[i].keys():
        listEntites.append(key)


svg_document = svgwrite.Drawing(filename = "test-svgwrite.svg",
                                debug = True)


for i in range(len(listEntites)):
    listAttributs = []
    nbAttributs = len(myJsonData[i][listEntites[i]]['attributs'])
    for j in range(nbAttributs):
        for key in myJsonData[i][listEntites[i]]['attributs'][j].keys():
            listAttributs.append(key)

    if (i % 2 == 0):

        svg_document.add(svg_document.rect(insert = (10, i*150 + 10),
                                           size = ("150px", "100px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))

        svg_document.add(svg_document.text(listEntites[i],
                                           insert = (20, i*150 + 30)))

        for k in range(len(listAttributs)):
            svg_document.add(svg_document.text(listAttributs[k],
                                               insert = (20, i*150 + 30 + (k+1)*20)))
    else:
        svg_document.add(svg_document.rect(insert = (400, (i - 1)*150 + 10),
                                           size = ("150px", "100px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))

        svg_document.add(svg_document.text(listEntites[i],
                                           insert = (410, (i - 1)*150 + 30)))

        for k in range(len(listAttributs)):
            svg_document.add(svg_document.text(listAttributs[k],
                                               insert = (410, (i - 1)*150 + 30 + (k+1)*20)))

# ---------------


# print(svg_document.tostring())

svg_document.save()
