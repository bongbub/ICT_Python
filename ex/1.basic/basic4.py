# if 조건문 뒤에는 반드시 콜론(:)을 붙인다.
# 콜론(:) => 다음 문장과 연결됨을 의미하며, 다음문장은 반드시 들여쓰기(탭, 스페이스바 4칸)를 하지 않으면 문법오류가 발생

# if 조건문:            # 조건문에 ()를 사용하면 구문 오류
# ....수행할 문장1       # 들여쓰기를 안하면 구문 오류
# ....수행할 문장2       # 들여쓰기를 안하면 구문 오류
# else:
# ....수행할 문장1       # 들여쓰기를 안하면 구문 오류
# ....수행할 문장2       # 들여쓰기를 안하면 구문 오류

print("===== <<< 1. 성적 출력 >>> =====")
score = int(input("성적을 입력하세요 :"))

# 60점 이상이면 합격, 그렇지 않으면 불합격
if score >= 60 :
    print("합격입니다.")
else :
    print("불합격입니다.")

# 이름(name), 국(kor), 영(eng), 수(math), 입력 받아서 총점과 평균(avg), 학점(grade)을 구하고 모두 출력하시오
name = input("이름을 입력하세요 : ")
kor = int(input("국어 점수를 입력하세요 : "))
eng = int(input("영어 점수를 입력하세요 : "))
math = int(input("수학 점수를 입력하세요 : "))
total = math+eng+kor
avg = total//3


if avg == 100 or avg >= 90:
    grade="A"
if avg >= 80 and avg >= 70:
    grade="B"
if avg >= 70 and avg >= 60:
    grade="C"
if avg >= 60 and avg >= 50:
    grade="D"
else:
    grade="F"

text="이름 : {0} \n국어 : {1}\n영어 : {2} \n수학 : {3} \n총점: {4} \n평균 : {5} \n학점 : {6}".format(name,kor,eng,math,total,avg,grade)
print(text)