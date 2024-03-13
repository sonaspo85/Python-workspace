from ssl import SSLEOFError

from setExePath import *
from pathlib import Path
from lxml import etree as et
from lxml.etree import ElementTree, Element, SubElement

class readCodeF:

    def __init__(self):
        pass

    def runReadCodes(self):
        print('runReadCodes 시작')

        codesF = resource_path1('libs/resource/codes.xml')
        codesP = Path(codesF).absolute().as_posix()

        parser = et.XMLParser(ns_clean=True, encoding='utf8', recover=True)
        doc = et.parse(codesP, parser)
        root = doc.getroot()


        for child in root.iter():
            lang = child.get('lang')



