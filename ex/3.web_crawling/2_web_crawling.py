from bs4 import BeautifulSoup

print(" ===== 2, BeautifulSoup")
# BeautifulSoup  ==> HTML 파싱 라이브러리 => 파싱 : 구분문석, 문법해석, 구상성분 분해
# 사이트 : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# pip install BeautifulSoup4   (파이참, Terminal, 아나콘다, 커맨드 모두 가능)

_html = """
<html>
    <body>
        <h1>Hello</h1>
        <p> 웹페이지 분석 </p>
        <p> 웹 스크래핑 </p>
    <body>
<html>
"""

# BeautifulSoup => HTML 파싱 라이브러리
# html : 소스텍스트
# parser : HTML 분석기

soup = BeautifulSoup(_html, "html.parser")      # _html 내의 문장을 html.parser를 통해 분석(파싱)하겠다
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
p3 = p2.next_sibling

# .string : string으로 가져오기
print("h1 : ", h1.string)           # h1 :  Hello   
print("p1 : ", p1.string)           # p1 :   웹페이지 분석
print("p2 : ", p2.string)           # p2 :   웹 스크래핑
print("p3 : ", p3.string)           # p3 :          (공백)

"""
아래는 <body> 안의 자식 노드들을 순서대로 나타낸 것입니다:
'\n ' – 개행 및 공백 (무시하고 싶지만 존재함)
<h1>Hello</h1>
'\n ' – 또 개행 및 공백
<p> 웹페이지 분석 </p> ← 이것이 p1
'\n ' – 개행 및 공백
<p> 웹 스크래핑 </p> ← 이것이 p2
'\n ' – 개행 및 공백
(이후는 </body>, </html>로 끝남)          ==> 때문에 p2를 뽑을 때 next_sibling이 두 번 들어간 ㄴ것 즉, 공백인식(노드인식)
"""