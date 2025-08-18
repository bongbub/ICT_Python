print(" ==== <<< 튜플 >>> ====")

# 1. 튜플이란?
# 리스트는 대괄호[]로 감싸고, 튜플은 소괄호()로 감싼다.
# 리스트는 수정, 삭제가 가능하지만, 튜플은 수정, 삭제가 불가능하다. 즉, 변경하지 않을 경우에 사용된다.
# 튜플은 tuple1 = (1, )처럼, 한 개의 요소만을 가질 경우, 요소 뒤에 콤마(,)를 반드시 붙여야 한다.
# 튜플은 tuple2= 1,2,3 처럼 괄호()를 생략해도 무방하다.

tuple1 = ()     # 튜플 생성
tuple2 = (1,)   # 값 1개 전달 ** 콤마 중요!
tuple3 = (1,2,3)
tuple4 = ('a', 'b', ('ab'),('cd'))
tuple5 = (1,2,'a','b')
tuple6 = 1,2,3

print("tuple1 : ", tuple1)
print("tuple2 : ", tuple2)
print("tuple3 : ", tuple3)
print("tuple4 : ", tuple4)
print("tuple5 : ", tuple5)
print("tuple6 : ", tuple6)

# 튜플은 수정, 삭제가 되지 않으므로 변경 하지 않을 경우에 사용하낟
 # tuple3[0] = 5
 # ("tuple3[0] : " , tuple3[0])
# Traceback (most recent call last):
# TypeError: 'tuple' object does not support item assignment

print()


# 2. 리스트의 요소가 튜플인 경우
list = [(1,2), (3,4), (5,6), (7,8), (9,10)]
print("list : ", list)
for(first, second) in list:
    print("두 수의 합 :", first + second)
# 두 수의 합 : 3
# 두 수의 합 : 7
# 두 수의 합 : 11
# 두 수의 합 : 15
# 두 수의 합 : 19


    print("{0} + {1} + {2}".format(first, second, first+second))
print()

# 3. 튜플 인덱싱
tuple7=(1,2,'a','b')
print("tuple7 : ", tuple7)      # tuple7 :  (1, 2, 'a', 'b')
print("tuple7[1:] : ", tuple7[1:])      # 인덱스 1번째부터 끝까지

tuple8=(3,4)
print("tuple7 + tuple8 : ", tuple7 + tuple8)        # tuple7 + tuple8 :  (1, 2, 'a', 'b', 3, 4)

print("tuple8 * 3 : ", tuple8 * 3)      # tuple8 * 3 :  (3, 4, 3, 4, 3, 4)

