# -*- coding: utf8 -*-
import os
import traceback
from pathlib import Path

from lxml import etree as et
from lxml.etree import ElementTree, Element, SubElement
from libs.Common.commonVar import common


class stepThree(common):
    eachSrcMap = {}

    def __init__(self, pbar1, lb4):
        super().__init__()
        self.pbar1 = pbar1
        self.lb4 = lb4

    def runStepThree(self):
        print("runStepThree 시작")

        # 1. 압축 해제된 각 폴더내 접근
        try:
            dirs = os.listdir(self.zipDir)

            # 1. 압축 해제된 zipDir 폴더내 각각의 폴더에 접근
            for dir in dirs:
                # 2. 절대 경로 생성

                self.abpath = Path(self.zipDir, dir)

                # 3. zipDir 폴더내 폴더 타입인 경우
                if os.path.isdir(self.abpath):
                    # 4. 각 폴더내 진입하여 하위 파일, 디렉토리 등을 리스트로 수집
                    self.dir2 = os.listdir(self.abpath)
                    # 5. designmap.xml 파일이 있는지 확인
                    if "designmap.xml" in self.dir2:
                        # 6. designmap.xml 파일의 절대 경로 생성
                        self.designmapF = os.path.join(self.abpath, "designmap.xml")
                        # 7. designmap.xml 파일 읽고, @StoryList 속성의 값을 절대 경로로 변환, hyperlink 태그 리스트 객체로 수집
                        self.readXml()

            # 8. {'챕터이름': ([linktag], [story.xml])} 수집한 self.eachSrcMap 딕셔너리 모으기
            self.recursDirs2()
            # 9. eachSrc 디렉토리내 파일들을 하나의 파일로 병합하기
            # self.finalMerged()

        except Exception as e:
            raise

    def finalMerged(self):
        print("finalMerged 시작")

        # 1. listdir() 함수로 디렉토리내 모든 파일 및 폴더를 리스트 객체로 추출
        files = os.listdir(self.tarpath)
        self.doc = None
        # 2. 새로운 root 태그 생성
        self.root = Element("root")
        # 3. 리스트 객체로 수집한 디렉토리 하위 탐색
        for file in files:
            # 4. 절대 경로 추출
            self.abpath = os.path.join(self.tarpath, file)

            # 5. 이름 추출
            self.filename = os.path.basename(file)
            # 6. xml 파일인 경우 문서내 접근 하기
            if os.path.isfile(self.abpath) and self.filename.endswith(".xml"):
                # 7. xml 파서 방법 설정
                self.parser = et.XMLParser(ns_clean=True, encoding="utf8", recover=True)
                # 8. xml 파싱
                self.doc = et.parse(self.abpath, self.parser)
                # 9. xml 문서내 root 태그 접근
                self.rootEle = self.doc.getroot()
                # 10. 루트 태그 이름 변경
                self.rootEle.tag = "docs"
                self.rootEle.set("filename", self.filename)
                # 11. 새롭게 생성한 root 태그에 자식 노드로 추가 하기
                self.root.append(self.rootEle)

        # 12. dom 트리 구조로 변환
        self.doc = ElementTree(self.root)

        # 13. merged 로 병합된 하나의 파일로 저장하기
        self.mergedPath = Path(self.tempDir, "finalmerged.xml")
        self.doc.write(
            self.mergedPath, pretty_print=True, encoding="utf8", method="xml"
        )

    def recursDirs2(self):
        print("recursDirs2 시작")

        try:
            self.doc = None
            # 1. {'챕터이름': ([linktag], [story.xml])} 형태의 딕셔너리 객체 반복
            for map in stepThree.eachSrcMap.items():
                self.foldername = Path(map[0]).as_posix()
                self.linkNode = map[1][0]
                self.storylistL = map[1][1]

                # 2. 새로운 root 태그 생성
                self.root = Element("root")
                self.root.set("filename", self.foldername)
                self.root.set("isocode", self.nameNiso[self.foldername])

                # 3. root 태그의 자식으로 linkcollect, body 태그 생성
                self.linkvar = SubElement(self.root, "linkcollect")
                self.bodyvar = SubElement(self.root, "body")

                # 4. link 태그를 모은 linkNode 리스트 객체를 리스트 표현식으로 반복하여 linkcollect 태그내로 삽입
                [self.linkvar.append(linktag) for linktag in self.linkNode]

                # 5. story.xml 반복하기
                for storyF in self.storylistL:
                    # 6. 파일이 존재 하는지 확인하기
                    if not os.path.isfile(storyF):
                        # print(f'{storyF} 파일이 존재 하지 않습니다.')
                        pass

                    else:  # 파일이 존재하는 경우 etree로 xml 파일 파싱하여 문서내 접근하기
                        self.parser = et.XMLParser(
                            ns_clean=True, recover=True, encoding="utf8"
                        )
                        self.newDoc = et.parse(storyF, self.parser)
                        # 7. xml 문서내 root 태그 접근
                        self.rootEle = self.newDoc.getroot()
                        # 8. CDATA 를 감싸고 있는 태그를 찾아 다른 텍스트로 변경
                        for child in self.rootEle.iter("Contents"):
                            child.text = ""

                        # 9. body 태그내 각 파일의 rootEle를 삽입하기
                        self.bodyvar.append(self.rootEle)

                # 10. 각 xml 파일들이 저장될 경로 설정
                # self.tarpath = os.path.abspath(os.path.relpath(os.path.join(self.zipDir, '../'))) + '/eachSrc/'
                self.tarpath = os.path.abspath(os.path.join(self.tempDir, "eachSrc"))

                if not os.path.isdir(self.tarpath):
                    os.makedirs(self.tarpath)

                # self.newTargetF = self.tarpath + '/' + self.foldername + '.xml'
                self.newTargetF = os.path.abspath(
                    os.path.join(self.tarpath, self.foldername + ".xml")
                )

                # 11. 각각의 파일로 저장
                self.saveEachXML()

        except Exception as e:
            msg = "Story.xml 로드 실패"
            print(traceback.format_exc())
            raise Exception(msg)

    def saveEachXML(self):
        print("saveEachXML 시작")
        try:
            # 1. Doc 트리 구조로 변환
            self.newDoc = ElementTree(self.root)
            # 2. 저장될 파일 경로 생성
            self.newDoc.write(
                self.newTargetF, pretty_print=True, encoding="utf-8", method="xml"
            )

        except Exception as e:
            raise Exception(e)

        else:
            self.pbar1.setValue(50)
            self.lb4.setText("eachSrc폴더내 xml 추출 완료")

    def readXml(self):
        print("readXml 시작")

        try:
            # 1. designmap.xml 파일이 위치한 폴더 이름 추출
            # self.foldername = os.path.dirname(self.designmapF).split('/')[-1]
            self.foldername = Path(self.designmapF).parent.name
            print("self.foldername:", self.foldername)

            # 2. designmap.xml 파일 읽기
            # 2. xml 파서 방법 지정
            self.parser = et.XMLParser(ns_clean=True, recover=True, encoding="utf8")
            # 3. xml 문서 파싱하기
            self.doc = et.parse(self.designmapF, self.parser)
            # 3. xml 문서내 루트 태그 접근
            self.rootEle = self.doc.getroot()

            # 4. @StoryList 속성의 값 추출
            self.storylistS = self.rootEle.get("StoryList")
            # 5. split() 함수로 문자열 분리후 list 타입으로 반환
            self.storylistL = self.storylistS.split()

            self.pos = 0
            for token in self.storylistL:
                # 6. story.xml 파일의 절대 경로 생성
                # self.fullpath = os.path.join(self.abpath, 'Stories', 'Story_' + token + '.xml')
                self.fullpath = Path(
                    self.abpath, "Stories", "Story_" + token + ".xml"
                ).as_posix()

                # 7. 기존 self.storylistL의 각 인덱스 위치에 절대 경로로 덮어씌우기
                self.storylistL[self.pos] = self.fullpath
                self.pos += 1

            # 7. Hyperlink, HyperlinkURLDestination 찾기
            # lxml 모듈은 EXSLT 를 활용하여 정규식 패턴을 파악할 수 있다.
            self.regexpNS = "http://exslt.org/regular-expressions"
            find = et.XPath(
                "//*[re:match(local-name(), '(^Hyperlink$|HyperlinkURLDestination)')]",
                namespaces={"re": self.regexpNS},
            )

            # self.rootEle Element 노드를 tostring() 함수로 텍스트로 변환
            xml2 = et.tostring(self.rootEle, method="xml", encoding="utf-8")
            # xml2 속성의 결과값은 바이트 문자열 이기 때문에, 유니코드 문자열로 디코딩 해야 한다.
            xml3 = xml2.decode("utf-8")

            root = et.XML(xml3)
            self.linktag = find(root)

            # 8. ([linktag], [story.xml]) 튜플 형태로 수집
            self.tuple = (self.linktag, self.storylistL)
            # 9. {'챕터이름': ([linktag], [story.xml])} 형태로 수집
            stepThree.eachSrcMap[self.foldername] = self.tuple

        except Exception as e:
            msg = "designmap.xml 로드 실패"
            raise Exception(msg)
