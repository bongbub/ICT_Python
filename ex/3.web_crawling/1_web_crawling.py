import urllib.request as req        # 자동 임포트
from bs4 import BeautifulSoup       # 수동으로 아래 방법을 통해 임포트

# 1. BeautifulSoup 설치 -> 방법1로 설치, 실패시 방법2로 설치
# 방법1. 터미널탭(왼쪽 아래 다섯번째 아이콘) : pip install 라이브러리명 => pip install BeautifulSoup4
#       => 1) python.exe -m pip install --upgrade pip    # 23.2.1 -> 25.0.1
#       => 2) pip install BeautifulSoup4    # 재실행
## 방법2. import문의 라이브러리명 위에 커서 위치하고 ALT+ENTER -> install package 라이브러리명 -> 성공하면 맨아래 Packages installed SuccessFully!! 출력


# BeautifulSoup => HTML 및 XML 파일에서 데이터를 추출하기 위해 사용하는 파이썬 라이브러리
#                   사용하기 위해서는 터미널에서 pip install BeautifulSoup4 로 다운


print(" ================  구글 이미지 읽어서 저장 ================")
# 구글 사이트(http://www.google.com") 방문 -> 구글 로고 우클릭 -> [이미지 주소 복사] 선택 -> 아래 url 변수에 붙여넣기
readurl = "https://images.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png"     # input
savename = "D:\DEV05\workspace_python_ict05\data\images/googlelogo.png"         # output


# 다운로드
# 다운로드 받은 이미지 파일을 메모리에 저장
# 1) read : 구글 로고를 읽는다.  input
g_image = req.urlopen(readurl).read()

# 2) 파일로 저장
# wb : write binary : 바이나리로 저장하겠다
with open(savename, mode = "wb") as f:      # 문장 자체에 f라는 별칭을 줌
    f.write(g_image)                        # write : 메모리의 이미지를 파일로 저장
    print("구글 이미지가 저장되었습니다")


# " ================  구글 이미지 읽어서 저장 ================"
