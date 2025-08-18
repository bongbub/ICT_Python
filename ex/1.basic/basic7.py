print(" =========== <<< 리스트 >>> =========== ")


# 매우중요
# 리스트는 대괄호[]로 감싼다
# 리스트는 추가, 수정, 삭제가 가능하다. 따라서 변경이 자주 일어날 경우 많이 사용한다. 


# 1. 리스트 출력
# 선언부
list = [2,4,6,8,10]
print("list =>" , list)


# 2. 리스트 추가 - append() => 리스트 맨 끝에 추가됨
list.append(12)
print("list =>" , list)             # list => [2, 4, 6, 8, 10, 12]


# 3. 리스트 생성하기
food = []       # 생성  -> 명란 비빔밥 레시피
food.append("명란")
food.append("밥")
food.append("명란명란명란란명란명란")
food.append("아보카도")
food.append("김가루")
food.append("후라이")
food.append("고추장")

print("명란비빔밥 레시피 : " , food)
print()


# 4. 리스트 요소 접근하기( 매우중요!! )  => 리스트(인덱스)로 접근
# 인덱스는 앞에서부터 0으로 시작, 뒤에서부터는 -1부터 시작 
# 리스트명 = [요소1, 요소2, ... 요소n ]
# 리스트 안에서 어떠한 자료형도 포함시킬 수 있다.

subject = ['국어', '영어', '수학']
# 국어
print(subject[0])
# 영어
print(subject[1])
# 수학
print(subject[2])
print()

# 5. 리스트 연산
list1 = [1,2,3]     # 선언
print("list => ", list1)

print("list1 합 : ", list1[0]+list1[1]+list1[2])     # list1 합 :  6
print("뒤에서 첫번째 : " , list1[-1])     # 뒤에서 첫번째 :  3
print()


print(" ==== <<< 이중 리스트 >>> ====")
# 6. 이중 리스트
list2 = [1,2,3,['x', 'y', 'z']]

print("list2[0] : ", list2[0])      # 1
print("list2[1] : ", list2[1])      # 2
print("list2[2] : ", list2[2])      # 3
print("list2[3] : ", list2[3])      # ['x', 'y', 'z']

print("list2[-1] : ", list2[-1])            # ['x', 'y', 'z']
print("list2[-1][0] : ", list2[-1][0])      # x
print("list2[-1][1] : ", list2[-1][1])      # y
print("list2[-1][2] : ", list2[-1][2])      # z