# 1. for문
# for 변수 in 리스트(또는 튜플, 문자열):
# ....수행할 문장1
# ....수행할 문장2

print("===== for문 : 횟수 제어 반복 ===")
print(" === 1. for문 ====")

for i in [1,2,3,4,5,6,7,8,9]:
    print(i, "교시 수업 시작!")

print()

test=['one','two','three', 'four', 'five']
for i in test:
    print(i, end=" ")       # 한행에 출력
print()

print("===== 2. range문 : 반복 횟수가 큰 경우 =====")
# 2-1. for문 range() : 반복횟수가 큰 경우
# for 변수 in range(start, end, step):        # start 생략시, 0부터 시작 end-1, step 생략시 1씩 증가
# ....수행할 문장1
# ....수행할 문장2
for i in range(1, 10, 1):
    print(i, "교시 수업 시작~!!!!~!")

# 2-2 for문 range() : 10~1까지 값을 한 줄로 출력
for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("===== 3. 2중 for문 =====")
# for문 range()를 이용해서 구구단을 출력
for i in range(2, 10, 1):
    print(i, "단")
    for j in range(1, 10, 1):
        print(i,"x",j,"=",i*j)
    print()


print()

print("===== 4. while문  =====")
# 4. while문
# while 조건문:
# ....수행할 문장1
# ....수행할 문장2

# 1-1. while문을 이용해서 1부터 10까지의 합계를 구하시오
i = 0
j = 0
while i < 11:
    j += i
    i += 1

print(j)

# 1-2 while 로그인
# password가 "python"이면 로그인 성공, 그렇지 않으면 계속 입력
pwd = ""
while pwd != "python" :
    pwd = input("비밀번호를 입력하세요 :")
print("로그인 성공!")


# 1-3 while - break 문
# 구구단 출력 원하는 단까지 출력하기 (종료:0), 빠져나갈땐 break
# True (Python의 true T는 대문자)
firdan = int(input("첫 번째 단 입력 : "))
lastdan = int(input("마지막 단 입력 : "))
for i in range(firdan, lastdan+1, 1):
    print( "== ",i,"단 ==")
    for j in range(1,10,1):
        print(i,"x",j,"=",i*j)
    print()


while True:
    dan = int(input("원하는 단은? (종료 : 0) : "))
    if dan == 0:
        print("종료")
        break
    for k in range(1,dan+1,1):
        print(dan,"x",k,"=",dan*k)



# 1-4 while - skip(continue)
# 1~10까지의 홀수값 출력
num = 0
while num <= 10:
    num = num + 1
    if num %2 ==0:    #짝수이면 스킵후 step으로 이동
     continue
    print("홀수 :",num)