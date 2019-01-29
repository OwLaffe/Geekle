import mimetypes as mt

def getFileType(fileName):
    '''
    ARGS:
        fileName : 찾고싶은 file의 이름.
    RAISE:
    RETURN:
        Contents-Type 헤더      : MIME Type.
        Contents-Encoding 값    : 프로그램이 보는 Type.
    '''
    ty = mt.guess_type(fileName)
    return ty[0], ty[1]

import os

fileLoc = "./IMGEX"
fileList = os.listdir(fileLoc)

for f in fileList:
    ft1, ft2 = getFileType(os.path.join(fileLoc, f))
    print(str(ft1))
