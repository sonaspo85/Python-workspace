import re
from ssl import SSLEOFError

from setExePath import *
from pathlib import Path
from lxml import etree as et
from lxml.etree import ElementTree, Element, SubElement

class readCodeF:

    def __init__(self, filename):
        self.filename = filename


    def runReadCodes(self):
        print('runReadCodes 시작')

        codesF = resource_path1('libs/resource/codes.xml')
        codesP = Path(codesF).absolute().as_posix()

        parser = et.XMLParser(ns_clean=True, encoding='utf8', recover=True)
        doc = et.parse(codesP, parser)
        root = doc.getroot()



        regexpNS = "http://exslt.org/regular-expressions"
        find = et.XPath("//*[re:match(local-name(), '(item)$')]", namespaces={'re': regexpNS})

        result = find(root)

        for child in result:
            team = child.get('team')
            lang = child.getparent().get('lang')

            pattern = self.filename
            comp = re.compile(pattern)

            if comp.search()





        # for items in root.findall('items'):
        #     lang = items.get('lang')
        #     print('lang:', lang)

