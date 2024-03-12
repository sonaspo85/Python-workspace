from pathlib import Path

p = Path("G:/MS-Drive/OneDrive - UOU/WORK/Workspace/WORK/TEST")
p = p / "dom구조.webp"

print(p)  # G:\MS-Drive\OneDrive - UOU\WORK\Workspace\WORK\TEST\dom구조.webp

# with_name() : 상위 경로는 그대로 두고 파일 이름만 변경한 새 경로를 반환
print(p.with_name("aaa.png"))
# 파일일 경우 : G:\MS-Drive\OneDrive - UOU\WORK\Workspace\WORK\TEST\aaa.png
# 폴더일 경우 : G:\MS-Drive\OneDrive - UOU\WORK\Workspace\WORK\aaa.png

# with_stem() : 파일 이름 부분만 변경 한다.
print(p.with_stem("qqq"))
# 파일일 경우 : G:\MS-Drive\OneDrive - UOU\WORK\Workspace\WORK\TEST\qqq.webp
# 폴더일 경우 : G:\MS-Drive\OneDrive - UOU\WORK\Workspace\WORK\qqq

# with_suffix() : 확장자만 변경한 새 경로
print(p.with_suffix(".xml"))
# 파일일 경우 : G:\MS-Drive\OneDrive - UOU\WORK\Workspace\WORK\TEST\dom구조.xml
# 폴더일 경우 : G:\MS-Drive\OneDrive - UOU\WORK\Workspace\WORK\TEST.xml
