from setExePath import *
from pathlib import Path
from lxml import etree as et
from lxml.etree import ElementTree, Element, SubElement


class readTeam:

    def __init__(self):
        self.teamL = []


    def runRead(self):
        print('runRead 시작')

        teamF = resource_path1('libs/resource/team.xml')
        teamP = Path(teamF).absolute().as_posix()

        # 1. xml 파서 방법 지정
        parser = et.XMLParser(ns_clean=True, encoding='utf8', recover=True)
        # 2. xml 문서 파싱
        doc = et.parse(teamP, parser)
        # 3. xml 문서내 root 태그 접근
        root = doc.getroot()

        for child in root.iter('item'):
            team_vals = child.get('team')
            # print(f'{team_vals=}')

            self.teamL.append(team_vals)

        return self.teamL


