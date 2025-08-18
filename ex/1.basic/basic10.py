print(" ==== <<< 함수 >>>  ====")

# 1. 문자열 삽입 - join()
str = ","
result = str.join('abcdefg')
print("result =", result)       # result = a,b,c,d,e,f,g

str2 = "ㅋ"
result2 = str2.join("안녕하세요")
print("result =", result2)      # result = 안ㅋ녕ㅋ하ㅋ세ㅋ요

# 2. 양쪽 공백 제거 - strip()
str = "               happy  "
print("str =" , str)        # str =                happy  <
result = str.strip()
print("result =", result)       # result = happy<

# 2-1. 왼쪽 공백 제거
l_result = str.lstrip()
print("l result =", l_result)       # l result = happy  <
# 2-2. 오른쪽 공백 제거
r_result = str.rstrip()
print("r result =", r_result)       # r result =                happy<


# 3. 대문자를 소문자로 - Lower()
str='HI'
result = str.lower()
print("result =", result)

# 4. 소문자를 대문자로 - upper()
str = 'hi'
result = str.upper()
print("result =", result)

# 5. 문장의 첫 번째 문자를 대문자로 - capitalize()
str = 'have a nice day'
result = str.capitalize()
print("result =", result)

print()


print(" ==== <<<< 함수 작성 및 호출 >>>> ====")
# 1. 함수 작성하고 호출하기
def print_info():
    print("이름 : ", "김태희")
    print("이메일 :", "kth@naver.com")
    print("나이 : ", 30)

# 호출 : 함수명()
print_info()
# 이름 :  김태희
# 이메일 : kth@naver.com
# 나이 :  30


print('----------------------------------')

# 2. 함수에 1개의 매개변수 전달하기
def print_info(name):
    print("이름 : ", name)
    print("이메일 :", "karina@naver.com")
    print("나이 : ", 25)

print_info("카리나")
print()

# 3. 함수에 여러개의 매개변수 전달하기
# 매개변수의 갯수는 값의 갯수와 정확히 일치해야 한다.
def print_info(name, email, age):
    print("이름 : ", name)
    print("이메일 :", email)
    print("나이 : ", age)

print_info("팜하니", "hani@naver.com", 22)
print()

# 1~10까지의 합계 구하기
def cal_sum(start, end):
    sum = 0
    for i in range(start, end+1)  :    # range(start, end-1) 이므로 넘겨주는 값 +1
        sum += i
    return sum

# 호출 : 함수명(값)
print(cal_sum(1, 10))

print()


print(" ==== <<< 객체 생성하기 >>> ====")

# 1. 객체의 설계도 작성
class Car :
    def drive(self):        # 메서드(함수) - 메서드 첫 번째 매개변수는 항상 self로서, 현재 객체를 가리킴
        self.speed = 10     # self.speed == this.speed  즉, 속성

# 2. 객체 생성 - 기본생성자를 사용 - 참조변수를 myCar 사용
# cf) 자바에서 객체 생성 : 클래스명 참조변수 = new 클래스명(); (Car myCar = new Car();)
myCar = Car()   # 파이썬에서 객체 생성하는 법. --> 참조변수 = 클래스명()

# 3. 객체의 속성 설정
#       참조변수.속성명
myCar.name = "람보르기니 우루스"
myCar.speed = 3000
myCar.color = "red"
myCar.price = 450000000

# 4. 객체의 속성 출력
print(" === 자동차 정보 출력 ===")
print("name : ", myCar.name)
print("speed : ", myCar.speed)
print("color : ", myCar.color)
print("price : ", myCar.price)

print('-----------------------')

# 5. 객체의 메서드 호출
# drive() 메서드의 self 매개변수(=자바의 this와 동일하다.) 어떤 객체가 메서드를 호출했는지 알려준다.
# 하지만 객체를 매개변수로 넣어서 drive()를 호출하지는 않는다.
# drive() 메서드를 호출할 때는 항상 "객체이름.메서드명"과 같은 형식을 사용하며, 객체 이름이 바로 self로 전달된다.

myCar.drive()           # 객체이름.메서드명 -> myCar가 drive(self)의 self에 전달됨
print("drive 스피드 : ", myCar.speed)          # drive 스피드 :  10
                                            # 만약 위의 myCar.drive() 생략시, drive.speed = 3000이 될 것임

print()
print()

print("---------------------------------------")
# === 입사 정보 출력 ===
# name : kakao
# hiredate : 20250101
# salary : 3000
# location : jejudo
# language : react
# drive 연봉 :  4000
# --------------

class Hire:
    def company(self):
        self.salary = 4000

com = Hire()

com.name="kakao"
com.hiredate = "20250101"
com.salary= 3000
com.location ='jejudo'
com.language='react'
print("=== 입사 정보 출력 ===")
print("name : ", com.name)
print("salary : ", com.salary)
print("location : ", com.location)
print("language : ", com.language)
com.company()
print("drive 연봉 : ", com.salary)

# === 입사 정보 출력 ===
# name :  kakao
# salary :  3000
# location :  jejudo
# language :  react
# drive 연봉 :  4000


print()
print()

print("==== <<< 객체 생성하면서 초기화하기 .. 매개변수 생성자를 사용 >>> ====")

# __init()__(self)  => 기본생성자
# 1. 객체의 설계도 작성
class Member:
    # 매개변수 생성자
    def __init__(self, id, name, age, email, job):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.job = job

    # 메서드
    def work(self):
        self.job = 'programmer'

# 2. 객체 생성 - 매개변수 생성자를 사용
member = Member("kim", "taehee", 30, "kim@naver.com", "talent")

# 3. 객체의 속성 출력
print(" === <<< member 정보 출력 >>> ===")
print("id : ", member.id)
print("name : ", member.name)
print("age : ", member.age)
print("email : ", member.email)
print("job : ", member.job)

# 4. 객체의 work 메서드 호출 및 출력
member.work()
print("메서드 work :" , member.job)
