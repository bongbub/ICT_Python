print(" === 자료형 ===")

# 출력 -> print
# 주석 : 블록 지정 후, ctrl + /  => # 이 자동으로 붙는다
# 코딩 : 1컬럼부터 시작한다. 문장끝에 세미콜론(;)을 붙이지 않는다.
# 실행 : 맨 위, Current file(현재 파일)로 바꾸고 run 버튼 (단축키 : Shift F10)
# 파이썬은 대 소문자를 구분한다
# 변수 앞에 자료형을 붙이지 않는다
# 처음부터 실행이 쭈륵 되는 인터프리터 언어임


a = 10
print("a =", a)


# 자료형
# 정수, 실수, 문자열, 복소수, 8진수, 16진수
# 복소수 : 실수부 + 허수부 => 실수부(실수 또는 정수) + 허수부(정수에 j 또는 J)
# 오른쪽의 값이 왼쪽 변수에 대입시점에 자료형 결정

x = 100
print("x =", x)

y=3.14
print("y =", y)

z="파이썬"
print("z =", z)

# 문자열 출력
greeting = "Hello"
print("인사 =", greeting)


# 사용자로부터 정수 입력
# input() 함수는 기본적으로 문자열을 입력받음
# 숫자로 바꾸려면 int(), eval() 사용
x= input("첫 번째 정수 : " )
y = input("두 번째 정수 : ")

sum = x + y
print(x, "+", y, "=", sum)

x= int(input("첫 번째 정수 : " ))
y = eval(input("두 번째 정수 : "))

sum2 = x + y
print(x, "+", y, "=", sum2)


# 빈 줄 삽입
print()

print("카페 매출 계산하기")
# 카페 매출 계산하기
americano_price = 4000
cafelatte_price = 5000
hongsii_price = 6000

ame = int(input(" 아메리카노 판매 갯수 : "))
latte = int(input("라떼 판매 갯수 : "))
hong = int(input("홍시 판매 갯수 : "))

total = americano_price * ame + cafelatte_price * latte + hongsii_price * hong

print("총 매출액 : ", total)








