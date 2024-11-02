import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
currency_dict = {}

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'NumCode':
                if child.firstChild.nodeType == 3:
                    numcode = child.firstChild.data
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    charcode = child.firstChild.data
    currency_dict[numcode] = charcode

    if node.getAttribute('id') == 'bk106':
        print(node.getElementsByTagName('NumCode')[0].firstChild.data)

for key in currency_dict.keys():
    print(key, currency_dict[key])


xml_file.close()