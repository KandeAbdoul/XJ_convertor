import pip
import svgwrite
import XJ_Convertor

svg_document = svgwrite.Drawing(filename = "test-svgwrite.svg",
                                size = ("800px", "600px"))

svg_document.add(svg_document.rect(insert = (0, 0),
                                   size = ("200px", "100px"),
                                   stroke_width = "1",
                                   stroke = "black",
                                   fill = "rgb(255,255,0)"))

svg_document.add(svg_document.text("Hello World",
                                   insert = (210, 110)))

print(svg_document.tostring())

svg_document.save()
