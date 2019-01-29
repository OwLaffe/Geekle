import mimetypes as mt
from PIL import Image

def getFileType(fileName):
    '''
    파일의 2가지 Type return. ( 뒤의 type은 gzip 같이 사용된다. )
    ARGS:
        fileName : 찾고싶은 file의 이름.
    RAISE:
    RETURN:
        Contents-Type 헤더      : MIME Type.
        Contents-Encoding 값    : 프로그램이 보는 Type.
    '''
    ty = mt.guess_type(fileName)
    return ty[0], ty[1]

def getFileSize(fileName):
    '''
    파일 Size를 tuple 로 return.
    ARGS:
        fileName : 찾고싶은 file의 이름
    RAISE:
        OSError : 파일이 png로 끝나고, mimetype이 png 이지만 사실 이미지가 아닌 파일일때.
    RETURN:
        retVal : 파일 size tuple
    '''
    try:
        img = Image.open(fileName)
        retVal = img.size
        img.close()
    except OSError:
        retVal = (-1, -1)
    
    return retVal

import os

fileLoc = "./IMGEX"
fileList = os.listdir(fileLoc)

for f in fileList:
    fName = os.path.join(fileLoc, f)
    ft1, ft2 = getFileType(fName)
    if str(ft1) == 'image/png':
        if getFileSize(fName) != (-1, -1):
            print(fName + " : " + str(getFileSize(fName)))
        else :
            print(fName + " : non-image File.")



