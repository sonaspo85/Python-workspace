# -*- coding: utf-8 -*-
import itertools
import os
import time
import traceback
from os import getcwd
from saxonche import *
from libs.Common.commonVar import common
from pathlib import Path


class stepSix(common):
    def __init__(self, pbar1, lb4):
        super().__init__()
        self.pbar1 = pbar1
        self.lb4 = lb4

        self.initcnt = self.pbar1.value()
        # print(f'{self.initcnt=}')

    def runStepSix(self):
        print("runStepSix 시작")

        try:
            # 1. eachSrc 경로 찾기
            self.eachSrcDir = Path(self.tempDir, "eachSrc")

            self.runEahSrc()

        except Exception as e:
            raise

    def updateInfo(self):
        print("updateInfo 시작")

        try:
            self.inoutpath = list(
                itertools.zip_longest(self.inL, self.outL, self.xsltL)
            )

            with PySaxonProcessor(license=False) as saxon:
                xsltprocess = saxon.new_xslt30_processor()

                # self.inF = self.resourceDir / 'docInfo.xml'
                self.inF = Path(self.resourceDir, "docInfo.xml").absolute().as_uri()
                self.outF = Path(self.resourceDir, "docInfo.xml").as_posix()
                self.xsltF = Path(self.xslsDir, "25-set-docinfo.xsl").as_posix()

                print(f"{self.inF=}")
                # print(self.outF)
                # print(self.xsltF)

                # 변환 하고자할 파일 설정
                xsltprocess.transform_to_file(
                    source_file=self.inF,
                    output_file=self.outF,
                    stylesheet_file=self.xsltF,
                )

                # print(xsltprocess.error_code)
                # print(f'{xsltprocess.error_message=}')
                xsltprocess.clear_parameters()

                self.cnt += 1
                self.pbar1.setValue(self.cnt)

                self.lsstTxt = os.path.split(self.xsltF)[1]
                self.lb4.setText(f"{self.lsstTxt} 완료")

        except Exception as e:
            msg = "docInfo update 실패"
            raise Exception(msg)


    def runEahSrc(self):
        print("runEahSrc 시작")

        try:
            self.files = os.listdir(self.eachSrcDir)

            for file in self.files:
                self.cnt = int(self.initcnt)
                self.filename = file
                # self.abspath = os.path.join(self.eachSrcDir, self.filename)
                self.abspath = (
                    Path(self.eachSrcDir, self.filename).absolute().as_posix()
                )

                self.inL = [
                    self.abspath,
                    self.xslsDir / "dummy.xml",
                    self.abspath,
                    self.tempDir / "01-simplify.xml",
                    self.tempDir / "02-simplify.xml",
                    self.tempDir / "03-define-BrType.xml",
                    self.tempDir / "04-cleanAttrs.xml",
                    self.tempDir / "05-grouping-br.xml",
                    self.tempDir / "06-groupingTR.xml",
                    self.tempDir / "07-split-BR.xml",
                    self.tempDir / "08-grouping-indent.xml",
                    self.tempDir / "09-nested-indent.xml",
                    self.tempDir / "10-grouping-list.xml",
                    self.tempDir / "11-grouping-note.xml",
                    self.tempDir / "12-nested-tags.xml",
                    self.tempDir / "13-simplify.xml",
                    self.tempDir / "14-connect-link.xml",
                    self.tempDir / "15-simplify.xml",
                    self.tempDir / "16-grouping-heading.xml",
                    self.tempDir / "17-1-insert-videolink.xml",
                    self.tempDir / "17-2-data-preORnext.xml",
                    self.tempDir / "17-3-connect-href.xml",
                    self.tempDir / "17-4-strip-img.xml",
                    self.tempDir / "18-simplify.xml",
                    self.tempDir / "18-simplify.xml",
                    self.tempDir / "18-simplify.xml",
                    self.tempDir / "00-messageF-groupLang.xml",
                    self.tempDir / "18-simplify.xml",
                    self.tempDir / "18-simplify.xml",
                ]

                self.outL = [
                    self.tempDir / "00-messageF-groupLang.xml",
                    self.tempDir / "00-videolinkF-group.xml",
                    self.tempDir / "01-simplify.xml",
                    self.tempDir / "02-simplify.xml",
                    self.tempDir / "03-define-BrType.xml",
                    self.tempDir / "04-cleanAttrs.xml",
                    self.tempDir / "05-grouping-br.xml",
                    self.tempDir / "06-groupingTR.xml",
                    self.tempDir / "07-split-BR.xml",
                    self.tempDir / "08-grouping-indent.xml",
                    self.tempDir / "09-nested-indent.xml",
                    self.tempDir / "10-grouping-list.xml",
                    self.tempDir / "11-grouping-note.xml",
                    self.tempDir / "12-nested-tags.xml",
                    self.tempDir / "13-simplify.xml",
                    self.tempDir / "14-connect-link.xml",
                    self.tempDir / "15-simplify.xml",
                    self.tempDir / "16-grouping-heading.xml",
                    self.tempDir / "17-1-insert-videolink.xml",
                    self.tempDir / "17-2-data-preORnext.xml",
                    self.tempDir / "17-3-connect-href.xml",
                    self.tempDir / "17-4-strip-img.xml",
                    self.tempDir / "18-simplify.xml",
                    self.tempDir / "19-create-body-header.xml",
                    self.tempDir / "dummy.xml",
                    self.tempDir / "dummy.xml",
                    self.tempDir / "dummy.xml",
                    self.tempDir / "dummy.xml",
                    self.tempDir / "dummy.xml",
                ]

                self.xsltL = [
                    self.xslsDir / "01-messageF-groupLang.xsl",
                    self.xslsDir / "01-videolinkF-group.xsl",
                    self.xslsDir / "01-simplify.xsl",
                    self.xslsDir / "02-simplify.xsl",
                    self.xslsDir / "03-define-BrType.xsl",
                    self.xslsDir / "04-cleanAttrs.xsl",
                    self.xslsDir / "05-grouping-br.xsl",
                    self.xslsDir / "06-groupingTR.xsl",
                    self.xslsDir / "07-split-BR.xsl",
                    self.xslsDir / "08-grouping-indent.xsl",
                    self.xslsDir / "09-nested-indent.xsl",
                    self.xslsDir / "10-grouping-list.xsl",
                    self.xslsDir / "11-grouping-note.xsl",
                    self.xslsDir / "12-nested-tags.xsl",
                    self.xslsDir / "13-simplify.xsl",
                    self.xslsDir / "14-connect-link.xsl",
                    self.xslsDir / "15-simplify.xsl",
                    self.xslsDir / "16-grouping-heading.xsl",
                    self.xslsDir / "17-1-insert-videolink.xsl",
                    self.xslsDir / "17-2-data-preORnext.xsl",
                    self.xslsDir / "17-3-connect-href.xsl",
                    self.xslsDir / "17-4-strip-img.xsl",
                    self.xslsDir / "18-simplify.xsl",
                    self.xslsDir / "19-create-body-header.xsl",
                    self.xslsDir / "20-split-html.xsl",
                    self.xslsDir / "21-search-db.xsl",
                    self.xslsDir / "22-ui_text.xsl",
                    self.xslsDir / "23-search-html.xsl",
                    self.xslsDir / "24-start-here.xsl",
                ]

                self.inoutpath = list(
                    itertools.zip_longest(self.inL, self.outL, self.xsltL)
                )
                # print("inoutpath:", self.inoutpath)

                with PySaxonProcessor(license=False) as saxon:
                    xsltprocess = saxon.new_xslt30_processor()

                    for tuple in self.inoutpath:
                        # self.inF = tuple[0]
                        # self.outF = tuple[1]
                        # self.xsltF = tuple[2]

                        # print(f'{srcpath=}')

                        self.inF = Path(tuple[0]).absolute().as_uri()
                        self.outF = Path(tuple[1]).as_posix()
                        self.xsltF = Path(tuple[2]).as_posix()

                        print(f"{self.inF=}")
                        print(f"{self.outF=}")
                        # print(self.xsltF)

                        # 변환 하고자할 파일 설정
                        xsltprocess.transform_to_file(
                            source_file=self.inF,
                            output_file=self.outF,
                            stylesheet_file=self.xsltF,
                        )

                        # print(xsltprocess.error_code)
                        # print(f'{xsltprocess.error_message=}')
                        xsltprocess.clear_parameters()

                        self.cnt += 1
                        self.pbar1.setValue(self.cnt)

                        self.lsstTxt = os.path.split(self.xsltF)[1]
                        self.lb4.setText(f"{self.lsstTxt} 완료")

        except Exception as e:
            msg = xsltprocess.error_message
            # msg = e
            raise Exception(msg)
