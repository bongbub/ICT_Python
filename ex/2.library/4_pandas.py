# Series(key, value) : 1차원 배열
# DataFrame(테이블 형식) : 2차원 배열

import numpy as np
import pandas as pd

print(" ===== 1. 1차원 배열 - Series 자료형 생성(인덱스없이) =====")
# 1차원 배열 - Series 자료형 생성
# 인덱스와 값 출력
# 인덱스 : 생략시 0,1,2,3, ...  이며, 숫자, 문자 모두 가능하다
series_data = pd.Series([2,4,6,8,10])
print(series_data)
# 0     2
# 1     4
# 2     6
# 3     8
# 4    10
# dtype: int64


print(" ===== 2. 1차원 배열 - Series 자료형 생성(인덱스 부여) =====")
# 1차원 배열 - Series 자료형 생성
series_data = pd.Series([2,4,6,8,10], index=['a','b','c','d','e'])
print(series_data)
# a     2
# b     4
# c     6
# d     8
# e    10
# dtype: int64



print(" ===== 3. 2차원 배열 - 데이터 프레임 사용(표현식) =====")
# 2차원 배열 - 데이터프레임 사용(표현식)
df = pd.DataFrame([[10,20,30], [40,50,60], [70,80,90]])
print(df)
#     0   1   2
# 0  10  20  30
# 1  40  50  60
# 2  70  80  90



print(" ===== 4-1. 전체 데이터 추출하기  =====")
# 원하는 데이터를 추출하기
# Dictionary를 데이터 프레임으로 변환
# Dictionary {}로 감싸고, key-value 쌍으로 되어 있다
# 5명의 키, 몸무게, 성별유형 데이터프레임 생성하기
tbl = pd.DataFrame({
  "체중" : [50,60,70,80,90],
  "신장" : [150,160,170,180,190],
  "성별" : ["여","여","여","남","남"]
})
print(tbl)

#    체중   신장 성별
# 0  50  150  여
# 1  60  160  여
# 2  70  170  여
# 3  80  180  남
# 4  90  190  남

print(" ===== 4-2. 원하는 데이터 추출하기  =====")
# 키 값으로 서치
print(tbl["체중"])
# 0    50
# 1    60
# 2    70
# 3    80
# 4    90
# Name: 체중, dtype: int64

print(tbl["신장"])
# 0    150
# 1    160
# 2    170
# 3    180
# 4    190
# Name: 신장, dtype: int64

print(tbl["성별"])
# 0    여
# 1    여
# 2    여
# 3    남
# 4    남
# Name: 성별, dtype: object


print(" ===== 4-3. 원하는 데이터 추출하기  =====")
# 복수개의 열
# 2개 이상의 컬럼일때는 안에 []대괄호를 추가로 넣어야 한다.  []가 1개이면 리스트이므로 에러가 발생한다

# 데이터 프레임 중 "체중", "신장" 출력
print(tbl[["체중", "신장"]])
#    체중   신장
# 0  50  150
# 1  60  160
# 2  70  170
# 3  80  180
# 4  90  190

print(" ===== 4-4. 원하는 데이터 추출하기  =====")
print(tbl[tbl.성별 == "여"])
#    체중   신장 성별
# 0  50  150  여
# 1  60  160  여
# 2  70  170  여

print(" ===== 5. Dictionary를 데이터프레임으로 변환  =====")
# Dictionary => {key:value, key:value}
dic_data = {"names" : ["마이멜로디","쿠로미","피카츄","꼬부기","마자용"],
            "years" : [2021,2022,2023,2024,2025],
            "points" : [1.5,2.0,2.5,3.0,3.5]}
df = pd.DataFrame(dic_data)
print(df)
#    names  years  points
# 0  마이멜로디   2021     1.5
# 1    쿠로미   2022     2.0
# 2    피카츄   2023     2.5
# 3    꼬부기   2024     3.0
# 4    마자용   2025     3.5


print(" ==== 6-1. 데이터프레임의 기본 통계 데이터 ====")
print(df.describe())
#              years    points
# count     5.000000  5.000000      # 갯수
# mean   2023.000000  2.500000      # 평균
# std       1.581139  0.790569      # 표준편차
# min    2021.000000  1.500000      # 최소
# 25%    2022.000000  2.000000
# 50%    2023.000000  2.500000
# 75%    2024.000000  3.000000
# max    2025.000000  3.500000      # 최대

# std(표준편차) : 분산의 제곱근
# 값이 클수록 데이터가 떨어져있다.
# 분산 : 평균값에서 얼마나 떨어져 있는지의 값
# 사분위수 : 4등급 .. 왼쪽 25%, 가운데 50%, 오른쪽 75%


print(" ==== 6-2. 데이터프레임의 값(인덱스, 컬럼값을 제외한 내용만 출력 ====")
print(df.values)
# [['마이멜로디' 2021 1.5]
#  ['쿠로미' 2022 2.0]
#  ['피카츄' 2023 2.5]
#  ['꼬부기' 2024 3.0]
#  ['마자용' 2025 3.5]]

print(" ==== 6-3. 인덱스명, 컬럼명 바꾸기 ====")
# 인덱스명 바꾸기
df.index.name = "Num"

# 컬럼명 바꾸기
df.columns.name="Info"
print(df)
# Info  names  years  points
# Num
# 0     마이멜로디   2021     1.5
# 1       쿠로미   2022     2.0
# 2       피카츄   2023     2.5
# 3       꼬부기   2024     3.0
# 4       마자용   2025     3.5


print(" ==== 7. Dictionary를 데이터프레임으로 변환 ====")
# Dictionary => {key:value, key:value}
# index : 인덱스 목록
# columns : 컬럼 목록
df2 = pd.DataFrame(dic_data, columns=["names","years","points", "penalty"], index=["A","B","C","D","E"])       # penalty 컬럼 추가

# 표 형태의 데이터 출력
print(df2)
#    names  years  points penalty
# A  마이멜로디   2021     1.5     NaN
# B    쿠로미   2022     2.0     NaN
# C    피카츄   2023     2.5     NaN
# D    꼬부기   2024     3.0     NaN
# E    마자용   2025     3.5     NaN

print(" ==== 7-1. 값, 인덱스 목록, 컬럼 목록 출력 ====")
print(df2.values)       # 값
# [['마이멜로디' 2021 1.5 nan]
#  ['쿠로미' 2022 2.0 nan]
#  ['피카츄' 2023 2.5 nan]
#  ['꼬부기' 2024 3.0 nan]
#  ['마자용' 2025 3.5 nan]]


print("df2.index => ", df2.index)
# df2.index =>  Index(['A', 'B', 'C', 'D', 'E'], dtype='object')
print("df2.columns => ", df2.columns)
# df2.columns =>  Index(['names', 'years', 'points', 'penalty'], dtype='object')




print(" ==== 7-2. 데이터프레임의 일부 컬럼만 출력 ====")
# 연도만 가져오기
print(df2["years"])
print(df2.years)
# A    2021
# B    2022
# C    2023
# D    2024
# E    2025
# Name: years, dtype: int64


print(" ==== 7-3. 복수개의 열 ====")
# 2개 이상의 컬럼일 때는 안에 []를 추가로 넣어야 한다.
# []가 1개이면 리스트로 처리되므로 에러가 발생한다
print(df2[["points", "years"]])
#    points  years
# A     1.5   2021
# B     2.0   2022
# C     2.5   2023
# D     3.0   2024
# E     3.5   2025


print(" ==== 7-4. Nan 필드에 값 대입 ====")
df2["penalty"] = 0.8
print(df2)
#    names  years  points  penalty
# A  마이멜로디   2021     1.5      0.8
# B    쿠로미   2022     2.0      0.8
# C    피카츄   2023     2.5      0.8
# D    꼬부기   2024     3.0      0.8
# E    마자용   2025     3.5      0.8



print(" ==== 7-5. Nan 필드에 각각 다른 값 대입(우변에 리스트로) ====")
df2["penalty"] = [0.8,0.6,0.7,0.2,0.5]
print(df2)
#    names  years  points  penalty
# A  마이멜로디   2021     1.5      0.8
# B    쿠로미   2022     2.0      0.6
# C    피카츄   2023     2.5      0.7
# D    꼬부기   2024     3.0      0.2
# E    마자용   2025     3.5      0.5

print(" ==== 7-6. 새로운 컬럼 추가 및 할당 ====")
df2["ages"] = np.arange(20, 25)        # 파이썬의 range(범위)와 비슷 => 20~24가 들어가게 됨
print(df2)
#    names  years  points  penalty  ages
# A  마이멜로디   2021     1.5      0.8    20
# B    쿠로미   2022     2.0      0.6    21
# C    피카츄   2023     2.5      0.7    22
# D    꼬부기   2024     3.0      0.2    23
# E    마자용   2025     3.5      0.5    24




print(" ==== 7-7. 컬럼 삭제 - del ====")
del df2["ages"]
print(df2)
#    names  years  points  penalty
# A  마이멜로디   2021     1.5      0.8
# B    쿠로미   2022     2.0      0.6
# C    피카츄   2023     2.5      0.7
# D    꼬부기   2024     3.0      0.2
# E    마자용   2025     3.5      0.5



print(" ==== 8-1. 특정행 조회 - loc[문자인덱스] / iloc[숫자인덱스] ====")
print(df2.loc["E"])
# names       마자용
# years      2025
# points      3.5
# penalty     0.5
# Name: E, dtype: object

print()
print(df2.iloc[2])      # 인덱스는 0부터 시작
# names       피카츄
# years      2023
# points      2.5
# penalty     0.7
# Name: C, dtype: object


print(" ==== 8-2. 특정행 조회 - loc[문자인덱스]  ====")
print(df2.loc["A" : "C"])        # A부터 C 까지 조회
#    names  years  points  penalty
# A  마이멜로디   2021     1.5      0.8
# B    쿠로미   2022     2.0      0.6
# C    피카츄   2023     2.5      0.7

print(" ==== 8-3. loc[행범위, 열범위]  ====")
# loc[start : end, start : end]  => 전체행, 전체 열

# 전체 행 중에서 "names", "years" 필드만 추출
print(df2.loc[ : , ["names" ,"years"]])
#    names  years
# A  마이멜로디   2021
# B    쿠로미   2022
# C    피카츄   2023
# D    꼬부기   2024
# E    마자용   2025


print(" ==== 8-4. 모든 행의 1~3열  ====")
print(df2.iloc[  :  , 1:4])   # n-1열까지  -> 4-1 ==> 3열까지
#    years  points  penalty
# A   2021     1.5      0.8
# B   2022     2.0      0.6
# C   2023     2.5      0.7
# D   2024     3.0      0.2
# E   2025     3.5      0.5


print()
print(" ==== 8-5. boolean 인덱싱  ====")
# 거짓 = False  /  참 = True           ※ 첫 글자가 대문자임!
# years가 2021보다 큰 데이터 추출하기
print(df2["years"] > 2021)

# A    False
# B     True
# C     True
# D     True
# E     True
# Name: years, dtype: bool

print(" ==== 8-6. True가 나온 행들만 추출  ====")
# years가 2021보다 클 때의 모든 열을 가져오기
# loc[행범위, 열범위]

print(df2.loc[df2.years > 2021, :])
#   names  years  points  penalty
# B   쿠로미   2022     2.0      0.6
# C   피카츄   2023     2.5      0.7
# D   꼬부기   2024     3.0      0.2
# E   마자용   2025     3.5      0.5


print(" ==== 9. 컬럼과 인덱스 설정 후 시작일로부터 5일간 추출  ====")
# 컬럼명 지정
df2.columns = ["A","B","C","D"]
# 인덱스명 지정
df2.index = pd.date_range("20250819", periods=5)      # 시작일로부터 5일간 출력
print(df2.index)
# DatetimeIndex(['2025-08-19', '2025-08-20', '2025-08-21', '2025-08-22',
#                '2025-08-23'],
#               dtype='datetime64[ns]', freq='D')

print()
print(df2)
#                 A     B    C    D
# 2025-08-19  마이멜로디  2021  1.5  0.8
# 2025-08-20    쿠로미  2022  2.0  0.6
# 2025-08-21    피카츄  2023  2.5  0.7
# 2025-08-22    꼬부기  2024  3.0  0.2
# 2025-08-23    마자용  2025  3.5  0.5

