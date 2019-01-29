import urllib.request
import os
import uuid

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
    if os.path.exists(dest + "/" + fileName):
        return False
    urllib.request.urlretrieve(link, dest + "/" + fileName)
    return True

def getLink(link, dec="utf-8"):
    '''
    이미지 링크를 수집.
    ARGS:
        - link : html 다운로드 받을 이미지가 있는 링크.
        - dec : decoding Type ( 한글은 기본 utf-8 )
    RAISE:
    RETURN:
        - imgLink : 이미지 다운받을 링크의 배열.
    '''
    html = urllib.request.urlopen(link).read().decode(dec)
    f = open("ss.html", "w")
    f.write(html)
    f.close
    token = divToken(html)
    imgLink = []
    for t in token:
        if "img" in t or "image" in t and "src=" in t:
                imgLink.append(divSrc(t))
    return imgLink

def divToken(html):
    '''
    html 에서 <> 기준으로 토큰 분리.
    ARGS:
        - html : html source
    RAISE:
    RETURN:
        - token : <> 기준으로 나뉜 토큰들.
    '''
    token = html.split('<')
    for i in range(0, len(token)):
        token[i] = token[i].split('>')[0]
    return token

def divSrc(token):
    '''
    src="" 기준으로 토큰 분리.
    ARGS:
        - token : HTML Source 에서 <> 기준으로 나뉜 토큰 값들.
    RAISE:
    RETURN:
        - src : token 에서 "src=...." 으로 된 값들의 real value.
    '''
    return token.split("src=\"")[1].split("\"")[0]

# 사용 예시
downName = 1
imgLink = getLink("http://pguin.tistory.com/559?category=639235")
fileName = []

for _ in range(0, len(imgLink)):
    while True:
        randomString = str(uuid.uuid4()).replace("-", "")
        if randomString not in fileName:
            fileName.append(randomString + ".png")
            break

for i in range(0, len(imgLink)):
    print(imgLink[i])
    if not downloadImg(imgLink[i], "/home/chj/workspace/PYTHON/Geekle/IMGEX", fileName[i]) :
        print("Download Fail....")
