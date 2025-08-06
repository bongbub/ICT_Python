from bs4 import BeautifulSoup

# BeautifulSoup : HTML 파싱 라이브러리

_html = '''
<html>
    <body>
        <div id="main">
        <h1>도서목록</h1>
        <ul class = "items">
            <li> 자바프로그래밍 입문</li>
            <li> JSP</li>
            <li> 스프링</li>
            <li> 파이썬</li>
        </ul>
    </body>    
</html>'''

# BeautifulSoup으로 구문 분석
soup = BeautifulSoup(_html, "html.parser")

# 도서목록 출력
h1 = soup.html.body.h1
print("h1 : ", h1.string)       # string으로 가져오기     # h1 :  도서목록

# select_one
# : 중복없는 1개의 태그가 갖고 있는 값을 출력
h2 = soup.select_one("div#main > h1")
print("h2 : ", h2.string)           # h2 :  도서목록

print()

# select
# : 여러개의 태그가 갖고 있는 값을 출력
li_list = soup.select("div#main > ul.items > li")     # id가 main인 div 태그 내, class 가 items인 ul 내의 li들을 갖고 와라

# 값이 여러개이므로 for문을 통해 출력
for li in li_list:
    print("li :", li.string)
# li :   자바프로그래밍 입문
# li :   JSP
# li :   스프링
# li :   파이썬






