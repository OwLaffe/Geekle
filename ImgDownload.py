import urllib.request
import os

def downloadImg(link, dest, fileName):
    '''
    link의 이미지를 dest/fileName 으로  다운로드.
    ARGS:
        - link : 다운 받을 사진 링크.
        - dest : 다운 될 사진의 디렉토리.
        - fileName : 사진의 이름.
    RAISE:
        - nothing
    RETURN:
        - 만약 디렉토리가 없거나 파일이 이미 있으면 False return.
        - else True
    '''
    if not os.path.isdir(dest):
        return False
    if os.path.exsts(dest + "/" + fileName):
        return False
    urllib.request.urlretrieve(link, dest + "/" + fileName)
    return True

def showLink(link, dec="utf-8"):
    '''
    '''
    html = urllib.request.urlopen(link).read().decode(dec)
    token = divToken(html)
    for l in token:
        if "img" in l or "image" in l:
            if "src=" in l:
                print(l.split("src=\"")[1].split("\"")[0])

def divToken(html):
    '''
    '''
    token = html.split('<')
    for i in range(0, len(token)):
        token[i] = token[i].split('>')[0]
    return token

showLink("http://pguin.tistory.com/559?category=639235")
