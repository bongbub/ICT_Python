print(" === <<< 2. 짝수 홀수 출력 >>> ===")
num = int(input("정수를 입력하세요 : "))
if num%2 == 0:
    print("짝수~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
else :
    print("홀수요~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

print("=== <<< 3. 다양한 조건을 판단하는 elif >>> ===")
pocket = ['cellphone', 'money','wallet']
# pocket에 cellphone이 있으면('핸드폰' in pocket) '카카오 택시탄다' 출력, card가 있으면 '카드내고 버스탄다' 출력, 그렇지않으면 '걸어간다' 출력
if 'cellphone' in pocket:
    print("카카오 택시 탄다.")
elif 'card' in pocket:
    print("카드 내고 버스 탄다 ")
else:
    print('걸어간다')
    
print()

print("=== <<< 4. 로그인 >>> ===")
# 아이디를 입력 받아 해당 아이디가 일치하면 '환영합니다' 출력 | 일치하지 않으면 '아이디 불일치'
id = 'hong1234'
result = input("아이디를 입력하세요 : ")
if id == result:
    print("환영합니다 고갱ㅇ님")
else :
    print("아이디 불일치 ㅡㅡ")