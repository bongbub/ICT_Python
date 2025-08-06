# json 분석

import json         # 자동 임포트 -> 설치할 필요 x


# json => {key : value, key : value ...}
# 파이썬의 딕셔너리와 형식이 동일함
# \ => 문장연결
str = '{"amount":[{"num": 0}, {"num":1}, {"num":2}], \
       "fruits":[{"fruit":"banana"}, {"fruit":"mango"}, {"fruit":"apple"}]}'

obj = json.loads(str)           # loads() : 파일이나 url에서 데이터를 읽어온다

# json 객체.get("key")  =>  key값에 맞는 value 값을 읽어온다
print(obj.get("fruits"))            # [{'fruit': 'banana'}, {'fruit': 'mango'}, {'fruit': 'apple'}]

print(obj.get("fruits")[0])         # {'fruit': 'banana'}
print(obj.get("fruits")[1])         # {'fruit': 'mango'}
print(obj.get("fruits")[2])         # {'fruit': 'apple'}
print()
print()

# banana, mango, apple 따로따로 가져와보기!
f1 = obj.get("fruits")[0]
print(f1["fruit"])
print(obj.get("fruits")[1].get("fruit"))
print(obj.get("fruits")[2]["fruit"])

print()


# [{"num": 0}, {"num":1}, {"num":2}]
# {"num": 0}
# {"num": 1}
# {"num": 2}
print(obj.get("amount"))
print(obj.get("amount")[0])
print(obj.get("amount")[1])
print(obj.get("amount")[2])
# 0
# 1
# 2
print(obj.get("amount")[0].get("num"))
print(obj.get("amount")[1].get("num"))
print(obj.get("amount")[2].get("num"))

