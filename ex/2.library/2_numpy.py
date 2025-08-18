print(" ==== <<< numpy >>> ====")

# 가. numpy 기본
# 1) 벡터 및 행렬 연산에 특화된 라이브러리
# 2) array 단위로 데이터를 관리함, 행렬(matrix)과 비슷함
# 3) pandas와 함께 데이터 분석에 많이 사용됨

import numpy as np

# 파이썬 리스트
data1 = [1,2,3,4,5]
print("data1 => ", data1)       # data1 =>  [1, 2, 3, 4, 5]

# 리스트를 넘파이 배열로 변환
arr1 = np.array(data1)
print("arr1 => ", arr1)         # arr1 =>  [1 2 3 4 5]

# 넘파이 배열의 크기
print("arr1.shape => ", arr1.shape)     # arr1.shape =>  (5,)

print()
# 2차원 리스트
data2 = [[1,2,3],[4,5,6]]
print("data2 => ", data2)       # data2 =>  [[1, 2, 3], [4, 5, 6]]

# 2차원 리스트를 넘파이 >배열<로 변환
arr2 = np.array(data2)
print("arr2 => ", arr2)         # arr2 =>  [[1 2 3]
                                #           [4 5 6]]

print("==== <<< 5행 4열의 넘파이 배열의 전체 합계, 평균 >>> ====")
arr = np.random.rand(5,4)
print("arr => ", arr)

# 전체 합계
print("전체 합계 : ", arr.sum())        # 전체 합계 :  9.676302483957278
# 전체 평균
print("전체 평균 :" , arr.mean())       # 전체 평균 : 0.4838151241978639


# 각 열(컬럼)의 합계  => axis=0 -> 열 | axis=1  -> 행
print("열 합계 : " , arr.sum(axis=0))  # 열의 합계
# 열 합계 :  [3.57597564 2.99410908 2.03697147 2.27627236]
print("행 합계 : ", arr.sum(axis=1))
# 행 합계 :  [2.24992217 1.96842732 2.07525208 2.13558698 2.02125719]



