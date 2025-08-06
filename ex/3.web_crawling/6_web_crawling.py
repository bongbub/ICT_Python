

# https://www.weather.go.kr/w/resources/jsp/life/imgdata_popup.jsp?CODE=N07_2&point=0&nowchk=Y

from bs4 import BeautifulSoup
from urllib.request import urlopen      # 자동 임포트
import pandas as pd

# 기상청 날씨누리 - 생활기상지수

html = urlopen('https://www.weather.go.kr/w/resources/jsp/life/imgdata_popup.jsp?CODE=N07_2&point=0&nowchk=Y')       # 지점값 보기

# url접속 -> F12키 개발자도구모드 진입 -> Sources -> jsp/file > imgdata_popup.jsp?CODE=NO7_2&point=0&nowchk=Y 파일 클릭

bsObject = BeautifulSoup(html, 'html.parser')
df = pd.DataFrame(columns=['Region','Level'])        # [지점, 지수단계]

# 여러개의 viewDataT라는 테이블이 있음
# <table class="viewDataT">  => table의 하위 모든 정보를 검색  -->>>>> find_all("table", {class : "viewDataT"} )


table = bsObject.body.find_all("table", {"class" : "viewDataT"})
index = table[0]
trs = index.find_all("tr")

# 3행(0행 : 날짜정보 / 1행 : 타이틀 => 제외) 부터 tr 행의 길이
# <th scope='row'>서울시</th>
# <td>낮음</td>

for i in range(2, len(trs)) :
    region = trs[i]
    ths = region.find_all("th",{"scope" : 'row'})
    tds = region.find_all('td')

    for j in range(0, len(ths)):
        df2 = pd.DataFrame({'Region' : [ths[j].text], 'Level' : [tds[j].text]})
        df = df._append(df2, ignore_index=True)
print(df)

#     Region Level
# 0      서울시    낮음
# 1      부산시    보통
# 2      기장군    보통
# 3      대구시    보통
# 4      달성군    보통
# ..     ...   ...
# 163    함양군    보통
# 164    거창군    보통
# 165    합천군    보통
# 166    제주시    높음
# 167   서귀포시    보통
#
# [168 rows x 2 columns]