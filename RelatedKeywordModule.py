# 사용하는 라이브러리
# requests
# bs4

# 초기에 입력받은 여러개의 키워드의 연관 검색어를 조사해서
# 키워드 수를 늘려주는 모듈입니다.

from bs4 import BeautifulSoup
import urllib.request
from urllib  import parse

def findRelatedKeywordsOfOne(keyword):
    '''
    주어진 키워드 하나의 연관 검색어를 반환해주는 함수입니다.
    ARGS :
        - keyword : 연관 검색어를 알고 싶은 문자열
    RAISE :
        - nothing.
    RETURN :
        - founded_keywords : 연관 검색어 리스트
    '''
    founded_keywords = []
    base_url = "https://search.naver.com/search.naver?&query="
    url = base_url + parse.quote(keyword)

    html = urllib.request.urlopen(url)
    doc = html.read()
    soup = BeautifulSoup(doc, "html.parser")

    attributes = {"class" : "_related_keyword_ul"}
    soup_related_keyword_ul = soup.find("ul", attributes)
    soup_lis = []
    if soup_related_keyword_ul is not None:
        soup_lis = soup_related_keyword_ul.select("li")

    for li in soup_lis :
        keyword = li.find("a").string
        founded_keywords.append(keyword)
    return founded_keywords

def findRelatedKeywordsOfMany(keywords):

    '''
    주어진 키워드들의 연관 검색어를 반환해주는 함수입니다.
    ARGS :
        - keywords : 연관 검색어를 알고 싶은 문자열 리스트
    RAISE :
        - nothing.
    RETURN :
        - founded_keywords : 연관 검색어 리스트
    '''

    result_keywords = []
    for keyword in keywords:
        print("==== " + keyword + " 연관 검색어 결과 ====")
        temp_keywords = findRelatedKeywordsOfOne(keyword)
        print(temp_keywords)
        result_keywords += temp_keywords
    return result_keywords

init_keywords = ["트와이스", "다현"]
print(findRelatedKeywordsOfMany(init_keywords))
