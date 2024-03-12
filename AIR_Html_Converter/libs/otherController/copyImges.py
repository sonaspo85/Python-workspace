import os
import shutil

from libs.Common.commonVar import common


class copyImages(common):
    def __init__(self):
        pass

    def runCopyImg(self):
        print("runCopyImg 시작")

        try:
            for item in self.workingLngsL:
                srcimgpath = item.get("srcimgpath")
                outimgpath = item.get("outputpath")
                outimgpath = outimgpath + "/contents/images"

                # print('srcimgpath:', srcimgpath)
                # print('outimgpath:', outimgpath)

                if not os.path.exists(outimgpath):
                    print("폴더가 없습니다. 폴더를 생성 합니다.")
                    os.makedirs(outimgpath)

                # 파일 복사
                files = os.listdir(srcimgpath)

                for file in files:
                    srcabspath = srcimgpath + "/" + file
                    tarabspath = outimgpath + "/" + file

                    shutil.copy(srcabspath, tarabspath)

                print(f"이미지 복사완료!")

        except Exception as e:
            msg = "src/images 폴더내 이미지 파일 복사 실패"
            raise Exception(msg)
