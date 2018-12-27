import xml.etree.cElementTree as ET 
import sys 

datas = sys.argv[1]
files = ET.ElementTree(file = datas)
root = files.getroot()
for nodes in root.iter('complexType') : 
    for child in nodes:
        if child.tag == "sequence":  
            print nodes.attrib['name'],'('
            for attribut in child:
                print '\t',attribut.attrib['name'],':',attribut.attrib['type']
            print ')\n\n'
        elif child.tag == "complexContent":
            print nodes.attrib['name'],'('
            for attribut in child:
                elem = attribut.find('element')
                if elem != None:
                    for element in attribut:
                        print '\t',element.attrib['name'],':', element.attrib['type']
                else:
                    print "\therite de", attribut.attrib['base']
                print ')\n'
        elif child.tag == "simpleContent":
            print '<<stereotype>> ',nodes.attrib['name'],'('
            for attributs in child:
                for attribut in attributs:
                    print '\t',attribut.attrib['name'],':',attribut.attrib['type']
                print ')\n'