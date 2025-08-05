print(" <<< 무자열 보팻 >>")
# %d, %s, %c, %f
#    : 문자열 포맷 코드
# 문자열.format(변수)

# 1. 숫자 바로 대입
str1 = "I eat %d apple" %3
print("str1 :", str1)

#2. 문자열 바로 대입
str2 ="I eat %s bananas" %"five"
print("str2 :", str2)

# 3. 2개 이상의 값 넣기
number = 10
day = "four"
str3 = "I eat %s bananas, for %s days" %(number, day)
print("str3 :", str3)

# 문자열.format(변수)        => 인덱스 사용
number = 2
str4 = "I eat {0} bananas".format(number)
print("str4 :", str4)

number = 5
day = 3
str5 = "I eat {0} bananas, for {1} days".format(number, day)
print("str5 :", str5)


# 문자열.format(변수) => {인덱스} 대신 {변수명} 사용
str6 = "이름 : {name} \n 나이 : {age} \n 성별 : {gender}".format(name="홍길동", age=12, gender="male")
print("str6 :", str6)
print()


# 천 단위 콤마
num = 123456789
print("{0: }".format(num))          # 123456789
print("{0:,}".format(num))         # 123,456,789
# print("{0:, }".format(num))  ->  콤마 뒤 공백 있으면 에러
print()

# 7. 백분율
fnum = 0.6789
print("{0:0%}".format(fnum))        # 67.890000%
print("{0:.0%}".format(fnum))       # 68%       -> .0% : 소수점 이하의 자릿수가 0
print("{0:.1%}".format(fnum))       # 67.9%     -> .1% : 소수점 이하의 자리수가 1
print("{0:.2%}".format(fnum))       # 67.89%    -> .2% : 소수점 이하의 자릿수가 2








