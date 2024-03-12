# -*- coding: utf8 -*-
import os.path
import traceback
from pathlib import Path
from lxml.etree import Element, ElementTree, SubElement

from libs.Common.commonVar import common


class docInfo(common):
    def runExtractXML(self):
        try:
            print("runExtractXML 시작")

            # docInfo.xml 절대 경로 생성
            self.docInfoS = Path(self.resourceDir, "docInfo.xml")
            # 파일이 존재 한다면 삭제
            if os.path.isfile(self.docInfoS):
                os.remove(self.docInfoS)

            self.writeDB()

        except Exception as e:
            print("eee:", e)
            raise

    def writeDB(self):
        print("writeDB 시작")

        try:
            self.dataL = []
            for lang, iso in self.langMap.items():
                self.dataL.append(f"{lang}={iso}")

            # self.dataL2 = '{' + ', '.join(self.dataL) + '}'
            self.dataL2 = ", ".join(self.dataL)

            self.root = Element("root")

            self.root.set("type", self.typeTxt)
            self.root.set("videoSwitch", self.radioTxt)
            self.root.set("modelNumber", self.modelNum)

            self.item = SubElement(
                self.root,
                "item",
                {"id": "projectDir", "path": Path(self.projectDir).as_posix()},
            )
            self.item = SubElement(
                self.root,
                "item",
                {"id": "srcDir", "path": Path(self.srcPath).as_posix()},
            )
            self.item = SubElement(
                self.root,
                "item",
                {"id": "resourceDir", "path": Path(self.resourceDir).as_posix()},
            )
            self.item = SubElement(
                self.root,
                "item",
                {"id": "tempDir", "path": Path(self.tempDir).as_posix()},
            )
            self.item = SubElement(
                self.root,
                "item",
                {"id": "xslsDir", "path": Path(self.xslsDir).as_posix()},
            )
            self.item = SubElement(
                self.root,
                "item",
                {"id": "excelTemplsDir", "path": Path(self.excelTemplsDir).as_posix()},
            )
            self.item = SubElement(
                self.root, "item", {"id": "langsMap", "sequence": f"{self.dataL2}"}
            )

            self.doc = ElementTree(self.root)

            # 저장될 폴더 생성
            self.saveInfoF = os.path.join(self.resourceDir, "docInfo.xml")
            self.doc.write(
                self.saveInfoF,
                pretty_print=True,
                encoding="utf8",
                method="xml",
                xml_declaration=True,
            )

        except Exception as e:
            msg = "docInfo.xml 파일 생성 실패"
            raise Exception(msg)
