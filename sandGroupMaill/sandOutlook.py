# 아웃룩 인스턴스 생성
import re

import win32com.client as win32
from lxml import etree as et

from setExePath import *


class outlookController:
    def runOutlook(self, personL):
        print("runOutlook 시작")

        try:
            # 아웃룩 인스턴스 생성
            outlook = win32.gencache.EnsureDispatch("Outlook.Application")
            olmailitem = 0x0  # 새 이메일의 크기

            form = resource_path1("resource")
            # personItem = "G:/Test/test/mailto.xml"

            personItem = form + "/mailto.xml"
            # print('self.contentF:', self.contentF)

            for person in personL:
                # 1. html 파서전 파서 옵션 지정
                parser = et.HTMLParser(encoding="utf8", recover=True)
                # 2. html 문서 파서
                doc = et.parse(personItem, parser)
                # 3. 문서내 root 요소에 접근
                root = doc.getroot()

                for child in root.iter("item"):
                    getName = child.get("name")
                    getMailAdd = child.get("mail")

                    if person == getName:
                        print("person:", person)
                        # 새 메일 쓰기창 열기
                        new_mail = outlook.CreateItem(olmailitem)

                        getHtml = form + "/" + person + ".html"
                        if os.path.isfile(getHtml):
                            # 1. html 파서전 파서 옵션 지정
                            parser = et.HTMLParser(encoding="utf8", recover=True)
                            # 2. html 문서 파서
                            doc = et.parse(getHtml, parser)
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

                        # 제목
                        new_mail.Subject = f"{self.titleContent}"

                        # 수신자와 참조
                        new_mail.To = getMailAdd
                        new_mail.CC = getMailAdd

                        new_mail.Body = self.bodyContent

                        # 메일 송부
                        new_mail.Send()

                        # 아웃룩 종료
                        outlook.Quit()

        except Exception as e:
            print("error: ", e)
