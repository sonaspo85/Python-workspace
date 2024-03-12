import pkgutil
from lxml import etree as et
from setExePath import *
from .echo3 import *

# __name__: 패키지 또는 모듈의 이름을 반환 한다.
print("__name__:", __name__)  # sampleDB

# __path__ : 현재 위치하고 있는 패키지 경로를 절대 경로로 반환하거나,
# 속성을 조작하여 다른곳에 위치한 패키지 경로를 찾도록 위치를 변경할 수 있다.
print(
    "init __path__:", __path__
)  # ['H:\\Python\\python-workspace\\pythonProject\\sampleDB']
print("init __package__:", __package__)  # sampleDB


def func():
    print("func 함수 시작")

    dbpath = resource_path1("")
    xmlpath = dbpath + __package__ + "/DB.xml"
    print("xmlpath:", xmlpath)
    parser = et.XMLParser(ns_clean=True, encoding="utf-8", recover=True)
    doc = et.parse(xmlpath, parser)
    #
    rootEle = doc.getroot()
    print("rootEle:", rootEle.tag)
    print("rootEle:", rootEle.get("StoryList"))
