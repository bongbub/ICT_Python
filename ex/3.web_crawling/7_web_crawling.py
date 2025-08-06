# 인증 key 복사
accessToken = "6565634a4d7768673337664d664c65"     # open api key -> 부정확하면 추후 (response error)응답 에러 발생

pageSize = 1000     # 데이터 양이 많아서 쪼개기 위함

import pandas as pd
import requests             # pip install requests      => http 요청에 대해서 처리 해주는 라이브러리
from itertools import count

totallist = list()

# 리스트 결과 읽어와, totallist에 담기
for pageNumber in count():          # 데이터가 몇 페이지까지 있는지 모를 때 count() 매서드를 돌린 뒤 예외처리해서 빠져나가기
    beginRow = str(1+(pageNumber * pageSize))
    endRow = str(pageSize * (pageNumber + 1))

    url = 'http://openapi.seoul.go.kr:8088/'
    url += accessToken
    url += '/json/bikeList/'
    url += beginRow + "/"
    url += endRow + "/"
    print(url)

    # get(url)
    response = requests.get(url)
    #print("response => ", response)
    jsondata = response.json()

    try:
        datalist = jsondata['rentBikeStatus']['row']
        for data in datalist:
            totallist.append(data)
    except Exception as err:
        print('Read end...')
        break



# xml 공공데이터 -> csv로 변환
# xml 공공데이터를 읽어서 아래 2025_bikeList.csv 폴더에 새로 저장 (이미 존재하는 경우는 삭제)
filename = "D:/DEV05/workspace_python_ict05/data/bike/2025_bikeList.csv"
myFrame = pd.DataFrame(totallist)
myFrame.to_csv(filename, index=False)
myFrame.to_csv(filename)

print("저장 -> ", filename)


# 한글 깨지는 문제
# # -> 만들어진 csv 파일 우클릭
# 메모장으로 열기 -> 다른 이름으로 저장 -> 인코딩 형식(UTF-8(BOM) 형식으로 저장
# -> 다시 엑셀로 열어보면 안 깨져있음!