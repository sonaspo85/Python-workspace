import os
import re

from lxml import etree as et


class readContent:
    def readHtmlF(self, contentF):
        print("readHtmlF 시작")

        print(f"{contentF=}")

        if os.path.isfile(contentF):
            print("파일이 존재 합니다.")
            # 1. html 파서전 파서 옵션 지정
            parser = et.HTMLParser(encoding="utf8", recover=True)
            # 2. html 문서 파서
            doc = et.parse(contentF, parser)
            # 3. 문서내 root 요소에 접근
            root = doc.getroot()

            for child in root.iter():
                if child.tag == "title":
                    self.titleContent = child.text

                elif child.tag == "body":
                    self.bodyContent = child.text

                    pattern = "(\w+.*)"
                    comp = re.compile(pattern)
                    self.result = comp.findall(self.bodyContent)
