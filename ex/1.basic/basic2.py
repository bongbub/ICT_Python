# 제곱근
# x의 y 제곱근을 나타내는 **연산자
x = 3
y = 2
print("x ** y :" , x ** y)   # 3의 2제곱 : 9


# 나눗셈
# /, //
# // => 소수점 이하 자리수를 무조건 버린다 (반올림 상관 x)
print("10/7 =", 10 / 7)         # 10/7 = 1.4285714285714286
print("10/6 =", 10 / 6)         # 10/6 = 1.6666666666666667
print("10/5 =", 10 / 5)         # 10/5 = 2.0

print("10 // 7 =", 10 // 7)     # 10 // 7 = 1
print("10 // 6 =", 10 // 6)     # 10 // 6 = 1
print("10 // 5 =", 10 // 5)     # 10 // 5 = 2

print()     # 빈 줄 삽입

print(" === 줄 바꾸기 ===")
# 줄 바꾸기
# \n , 또는 연속된 작은 따옴표 3개('''  '''), 연속된 큰 따옴표 3개("""   """)
multiline = "Life is too short. So you have study hard!!"
print(multiline)
print()

multiline2 = '''Life is too short
. 
So you have study hard!!'''         # 작성한 대로 줄 바꿈이 됨
print(multiline2)
print()


multiline3 = """Life is too 
short. So you have 
study hard!!"""                 # 작성한 대로 줄 바꿈이 됨
print(multiline3)
print()

multiline4 = "Life is too short. \n So you have study  \n!!!!!! hard!!"
print(multiline4)       # \n : 줄 바꿈
print()


print(" --- <<< 문자열 연산하기 >>> ---")
# 문자열 연산하기
    # 더하기
head = "python"
tail = " is fun"
print(head + tail)      # python is fun


    # 곱하기
str = "python "
print(str * 3)

li = "**"
print(li * 30)


print(" *** <<< 문자열 인덱싱과 슬라이딩 ( 중요! ) >>> *** ")
# 문자열 인덱싱과 슬라이싱
# 파이썬의 인덱싱 : 0 부터 시작
strs = "Life is too short. So you have study hard!!"
print("strs[3] :" , strs[3])        # 앞에서부터 4번째 출력 => e
print("strs[-3] :" , strs[-3])      # 뒤에서부터 3번째 출력 => d


# 슬라이싱 ( 중요! )
# strs[시작번호 : 끝번호]  ==> 시작번호부터 : 끝번호-1 까지
print("strs[0:7] : " , strs[0:7])       # strs[0:7] :  Life is
print()

# 끝 번호를 생략하면 시작번호부터 그 문자열의 끝까지 추출한다
print("strs[19:] -> ",strs[19:] )
















