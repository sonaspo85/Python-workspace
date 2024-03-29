import time

from libs.controller.InOutPathClas import InOutPathClas
from setExePath import *
from pathlib import Path
from saxonche import *


class transformXSLT:

    def __init__(self, dic_map, pbar1, lb2):
        self.list = []
        self.projectDir = Path(resource_path2('')).absolute().as_posix()
        self.xslDir = Path(resource_path1('')).absolute().as_posix()
        print('self.xslDir:', self.xslDir)

        self.dic_map = dic_map
        self.pbar1 = pbar1
        self.lb2 = lb2

        self.initcnt = self.pbar1.value()




    def set_sequence(self):
        print('set_sequence 시작')


        for items in self.dic_map.items():
            srcpath = Path(items[0]).absolute().as_posix()

            isocode = items[1]

            self.list.append(InOutPathClas(srcpath, self.projectDir + '/temp/' + '01_0a-tmx2xml_' + isocode + '.xml', self.xslDir + '/libs/xslt/0a-tmx2xml.xsl'))
            self.list.append(InOutPathClas(self.projectDir + '/temp/' + '01_0a-tmx2xml_' + isocode + '.xml', self.projectDir + '/json/' + isocode + '.JSON', self.xslDir + '/libs/xslt/0b-xml2json.xsl'))

            self.runXSLT()
            self.list.clear()



    def runXSLT(self):
        print('runXSLT 시작')

        try:
            with PySaxonProcessor(license=False) as saxon:
                xsltpro = saxon.new_xslt30_processor()

                self.cnt = int(self.initcnt)
                for x in self.list:
                    try:

                        iox = x

                        inF = Path(iox.getinF()).absolute().as_posix()
                        outF = Path(iox.getoutF()).absolute().as_posix()
                        xsltF = Path(iox.getxsltF()).absolute().as_posix()
                        xslname = Path(iox.getxsltF()).stem

                        # print(f'{inF=}')
                        # print(f'{outF=}')
                        print(f'{xsltF=}')

                        xsltpro.transform_to_file(source_file=inF, output_file=outF, stylesheet_file=xsltF)
                        xsltpro.clear_parameters()


                        self.cnt += 5
                        self.pbar1.setValue(self.cnt)
                        self.lb2.setText(xslname)


                    except Exception as e:
                        raise



        except Exception as e:
            raise
