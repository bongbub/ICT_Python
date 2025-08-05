# python 주요 데이터분석 라이브러리 .. 매우 중요(면접)
import matplotlib

# 1) 넘파이(Numpy)
    # - python 데이터 분석의 기본적인 기능을 제공
    # - 특히 백터 및 행렬 연산(2차원배열)과 관련된 편리한 기능들을 제공

# 2) 판다스(Pandas)
    # - Series(key, value) : 1차원 배열, DataFrame(테이블 형식, 2차원 배열) 등의 자료구조를 활용하여 데이터 분석시 우수한 성능을 발휘함
    # - 대량의 데이터를 더욱 빠른 속도로 처리할 수 있음

# 3) 맷플롯립(Matplotlib)
    # - 데이터 분석 결과에 대한 시각화를 빠르고 직관적으로 수행

print("*** 데이터 분석 시각화 ***")
# 1. 그래프 명령어
# 방법1. 터미널탭(왼쪽 아래 다섯번째 아이콘) : pip install 라이브러리명 => pip install numpy pandas matplotlib
#       => 1) python.exe -m pip install --upgrade pip    # 23.2.1 -> 25.0.1
#       => 2) pip install numpy pandas matplotlib    # 재실행
## 방법2. import문의 라이브러리명 위에 커서 위치하고 ALT+ENTER -> install package 라이브러리명 -> 성공하면 맨아래 Packages installed SuccessFully!! 출력
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("--------- 1. 50개의 난수로 이루어진 데이터 생성( 0.0 ~ 1.0 ) ---------")
npData = np.random.rand(50)
print("npData : " ,npData)


print("--------- 2. 넘파이 배열 50개를 판다스의 시리즈로 변환 ---------")
# Series(넘파이 배열)
# Series : 인덱스와 value로 구성된 자료형
seriesData = pd.Series(npData)
print("seriesData : " ,seriesData)


print("--------- 3. 데이터를 가지고 선형 그래프 그리기 ---------")
# 선형 그래프 그리기
# matplotlib => 그래프
# x축 : index (0~49)      y축 : value (난수 값)

plt.plot(seriesData)
plt.show()          # 파이참에서 차트 보여주기

plt.close()         # 이전 차트가 닫혀 있어야 다음 차트를 실행할 수 있다.

print("--------- 4. 넘파이로 랜덤값 생성, 10행 3열의 2차원 배열(=행렬) 생성 ---------")
# 넘파이로 랜덤값 생성, 10행 3열의 2차원 배열(=행렬)
npData2 = np.random.rand(10,3)
print("npData2 : " ,npData2)        # 주의! ) 이전 차트가 닫혀 있어야 다음 차트를 볼 수 있음!


print()
print("--------- 5. 판다스의 데이터프레임(테이블 형식) ---------")
# 판다스의 데이터프레임 (테이블 형식)
# DataFrame(데이터셋명, 컬럼이름)
df = pd.DataFrame(npData2, columns=['A','B','C'])
print(df)

print("--------- 5-1. 선형 그래프 출력 ---------")
# 선형 그래프 출력
df.plot()
plt.show()

print("--------- 5-2. 수직 막대 그래프 출력 ---------")
# 수직 막대 그래프 출력
df.plot(kind='bar')        # bar 수직 형태
plt.show()

print("--------- 5-3. 수평 막대 그래프 출력 ---------")
# 수평 막대 그래프 출력
df.plot(kind='barh')        # barh : 수평형태 bar+horizontal
plt.show()

print("--------- 5-4. 누적 영역 막대 그래프 출력 ---------")
# 누적 영역 막대 그래프 출력
# 가장 위쪽의 컬럼의 y축값은 a, b, c의 값을 더함
df.plot(kind='area')
plt.show()

print("--------- 5-5 누적하지 않는 영역 막대 그래프 출력 ---------")
# 누적하지 않는 영역 그래프 출력
# 반 투명 상태로 겹치는 영역이 표현됨
df.plot(kind='area' , stacked=False)        # false 대소문자 정확히 구분
plt.show()

print("--------- 5-6 파이 그래프를 위한 5개의 난수 발생 ---------")
seriesData2 = pd.Series(np.random.rand(5), index=["a","b","c","d","e"], name="series")
print("seriesData2 : " ,seriesData2)


print("--------- 5-7 파이 그래프를 출력 ---------")
# 파이그래프 출력
# kind = "pie" : 파이그래프
# autopct="%.2f" : 소수점 이하 둘째자리로 부여
# figsize = (x,y) : x축과 y축의 비율
seriesData2.plot(kind='pie', autopct="%.2f", fontsize = 13,  figsize=(4,5))    # 소수점 이하 둘째 자리로 주다
plt.show()


print("--------- 6 막대 그래프를 출력 ---------")
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
names = ["python", "java", "spring", "react"]
score = [95, 86, 69, 92]
ax1.plot(names, score, color="#f00")
ax1.bar(names, score)
ax1.set_title("sample")
ax1.set_xlabel("class")
ax1.set_ylabel("count")
plt.show()



