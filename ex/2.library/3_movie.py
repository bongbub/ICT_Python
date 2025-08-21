from time import process_time_ns

print(" ==== <<< 영화 평점 데이터 >>> ====")

# 데이터 분석 실습 - 영화 평점 데이터
# 영화평점 데이터셋 로딩
# https://grouplens.org/datasets/movielens/
# older datasets > MovieLens 1M Dataset > ml-1m.zip 다운로드해서 data 폴더에 붙여넣고 압축해제
# D:\Dev\workspace_python_ict05\data\3.movie\ml-1m\ratings.dat

# 노트패드 다운로드 : 구글에서 노트패드 검색 > [notepad++ 다운로드] 클릭 > v8.7.6선택 해서
# Download 64-bit x64 > installer 클릭 > exe 파일 디폴트 설치

# ratings.dat 구조 => 노트패드 실행 > drag and drop
# ratings.dat 구조 => 6040::1097::4::956715569 => 사용자ID::영화번호::평점::시간


import numpy as np

# 방법1)
# np.loadTxt(파일명...)  ==> 아나콘다에서만 작동 (파이참은 안댐!)

# 방법2)
movieData = np.genfromtxt("D:/DEV05/workspace_python_ict05/data/movie/ml-1m/ratings.dat",
              delimiter="::", dtype=np.int64, encoding="utf-8")     # 폴더 사이가  \ -> 에러

# print(movieData)

print("===== 데이터의 첫 5행, 모든 열 조회하기 =====")
# 넘파이 배열 [행번호, 열범위]
# [start:end, start:end]

print(movieData[:5, :])  # 0부터 4행까지, 모든 열 가져오기
# [[        1      1193         5 978300760]
#  [        1       661         3 978302109]
#  [        1       914         3 978301968]
#  [        1      3408         4 978300275]
#  [        1      2355         5 978824291]]

print("===== 데이터의 형태 확인 =====")
print(movieData.shape)          # (1000209, 4)  => (행갯수, 열갯수)



print("===== 전체 평점에 대한 평균 계산 =====")
mean_rating = movieData[ : , 2].mean()      # [모든행, 2번째 열]  # 열은 0번째부터 시작
print(mean_rating)
# 3.581564453029317

print("===== 사용자 아이디 수집 =====")
# 중복값 제거 : unique(대표값)
user_ids = np.unique(movieData[ : , 0])
#          movieData의 모든행기준, 0열 기준(사용자아이디) 유니크를 구하겟다
print(user_ids)
# [   1    2    3 ... 6038 6039 6040]

print("===== 사용자별 평점에 대한 평균 집계 =====")
# 사용자별 평점 평균값을 저장할 배열
mean_values =[]
for user_id in user_ids:        # 중복값 제거한 6040건의 아이디를 하나씩 읽음
    # movieData 중에서 모든행, 0번 필드 == 중복값 제거한 user_id(현재아이디)와 일치한 행의 모든 컬럼을 가져와라
    data_for_user = movieData[movieData[:, 0] == user_id, : ]   # user_id와 일치한 행의 모든 데이터

    # 2번째 인덱스(평점)에 해당하는 값의 평균값
    mean_rating = data_for_user[ : , 2].mean()      # data_for_user --> 현재 읽어온 행의 모든 컬럼 중, 2열 --> 평점

    # 사용자 아이디와 평점평균을 배열에 추가
    mean_values.append([user_id, mean_rating])      # 현재 아이디와 구한 평점을 mean_values 배열에 저장

    # --> 6040번 반복

print("===== 사용자 아이디별 별점 평균[id, 평점] =====")
print(mean_values[ : 5])    # 인덱스 0~4행, 5건만 가져오기
# [[np.int64(1), np.float64(4.188679245283019)],
# [np.int64(2), np.float64(3.7131782945736433)],
# [np.int64(3), np.float64(3.9019607843137254)],
# [np.int64(4), np.float64(4.190476190476191)],
# [np.int64(5), np.float64(3.1464646464646466)]]


# 리스트를 넘파이 배열로 변환
mean_array = np.array(mean_values, dtype=np.float32)     # 실수
print(mean_array[ : 5])
# [[1.        4.188679 ]
#  [2.        3.7131784]
#  [3.        3.9019608]
#  [4.        4.1904764]
#  [5.        3.1464646]]


print(" ==== 마지막 id인 6040행, 2열(id, 평점평균]의 넘파이 배열 ====")
print(mean_array.shape)


print(" ==== 넘파이 배열을 CSV 파일로 저장하기 => result 폴더 생성 > 6040건의 확인 ====")
np.savetxt("D:/DEV05/workspace_python_ict05/data/movie/ml-1m/result/ratings_result.csv",
           mean_array, fmt="%.1f", delimiter=",")       # result 폴더에 결과파일 자동생성, 결과확인 : 파일 우클릭 notePad로 읽기