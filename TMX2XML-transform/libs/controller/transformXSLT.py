from libs.controller.InOutPathClas import InOutPathClas
from setExePath import *
from pathlib import Path
from saxonche import *


class transformXSLT:

    def __init__(self, dic_map):
        self.list = []
        self.projectDir = Path(resource_path1('')).absolute().as_posix()
        self.dic_map = dic_map


    def set_sequence(self):
        print('set_sequence 시작')

        for items in self.dic_map.items():
            srcpath = Path(items[0]).absolute().as_posix()


            isocode = items[1]

            self.list.append(InOutPathClas(srcpath, self.projectDir + '/temp/' + '01_0a-tmx2xml_' + isocode + '.xml', self.projectDir + '/libs/xslt/0a-tmx2xml.xsl'))
            self.list.append(InOutPathClas(self.projectDir + '/temp/' + '01_0a-tmx2xml_' + isocode + '.xml', self.projectDir + '/json/' + isocode + '.JSON', self.projectDir + '/libs/xslt/0b-xml2json.xsl'))




    def runXSLT(self):
        print('runXSLT 시작')

        with PySaxonProcessor(license=False) as saxon:
            xsltpro = saxon.new_xslt30_processor()

            for x in self.list:
                iox = x

                inF = Path(iox.getinF()).absolute().as_posix()
                outF = Path(iox.getoutF()).absolute().as_posix()
                xsltF = Path(iox.getxsltF()).absolute().as_posix()

                # print(f'{inF=}')
                # print(f'{outF=}')
                print(f'{xsltF=}')

                xsltpro.transform_to_file(source_file=inF, output_file=outF, stylesheet_file=xsltF)
                xsltpro.clear_parameters()
