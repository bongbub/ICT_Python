print(" ==== <<< 딕셔너리 >>> ====")

# dictionary : key-value 키-값이 쌍으로 구성되어 있다
# 중괄호{} 로 생성, cf) 리스트는 대괄호[], 튜플은 소괄호()
# 예) 영어사전 - 단어(key) + 단어설명(value)

print("==== 1. 생성후 초기화 ====")
# 1-1. 생성후 초기화
phone_book = {}     # 딕셔너리 생성
phone_book["김태희"]="010-1111-2222"       # 초기화 => 딕셔너리명["key"] = value
phone_book["소지섭"]="010-3333-4444"
print('phone_book :' , phone_book)

print()

# 1-2. key를 통해서 값을 읽어옴
print("phone_book['김태희'] => ", phone_book["김태희"])       # phone_book['김태희'] =>  010-1111-2222
print("phone_book['소지섭'] => ", phone_book["소지섭"])

print()

# 1-3. key들을 읽어옴
print("keys  => ", phone_book.keys())       # keys  =>  dict_keys(['김태희', '소지섭'])

# 1-4. value들을 읽어옴
print("values => :" , phone_book.values())      # values => : dict_values(['010-1111-2222', '010-3333-4444'])

print()
print()

print(" ==== 2. 생성과 동시에 초기화 ====")
# 2-1. 생성과 동시에 초기화
phone_book = {"팜하니" : "010-5555-6666", "카리나" :"010-7777-8888"}
print("phone_book : ", phone_book)        # phone_book :  {'팜하니': '010-5555-6666', '카리나': '010-7777-8888'}

# 2-2. key들을 읽어옴
print("keys  => ", phone_book.keys())      # keys  =>  dict_keys(['팜하니', '카리나'])

# 2-3 value들을 읽어옴
print("values => :" , phone_book.values())         # values => : dict_values(['010-5555-6666', '010-7777-8888'])


print()
print()


print(" ==== 3. 삭제 ====")

# 3-1. 딕셔너리 삭제 - del
del phone_book["카리나"]
print("phone_book : ", phone_book)        # phone_book :  {'팜하니': '010-5555-6666'}

print()


# 3-2. 딕셔너리 전부삭제 - clear()
print("phone_book : ", phone_book)      # phone_book :  {'팜하니': '010-5555-6666'}
phone_book.clear()
print("phone_book 클리어 후 : ", phone_book)        #  {}

print()
print()


print(" ==== 4. 딕셔너리 추가 ====")
# 4. 새로운 요소 추가 -> 딕셔너리[key] = value

address = {1: '서울시 강남구'}
print("address : ", address)        # address :  {1: '서울시 강남구'}
address[2] = '서울시 마포구'
address[3] = '서울시 구로구'
print("address : ", address)        # address :  {1: '서울시 강남구', 2: '서울시 마포구', 3: '서울시 구로구'}

print()
print()

print(" ==== 5. key를 통해 value값 읽기 (get)  ====")
info = {"name" : "팜하니", "phone" : "010-5555-6666", "birth" : "20041006"}
print("info : ", info)

# key를 통해 value 가져오기 : 인덱스로 가져오기
print('이름은? (info["name"]) : ' , info["name"])
# get을 통해 가져오기 : get을 통해 가져오기
print('전화번호는 ? (info.get("phone") : ', info.get("phone"))
print('생년월일은? (info.get("birth") : ', info.get("birth"))

# key들을 읽어옴
print("keys  => ", info.keys())
# value들을 읽어옴
print("values => :" , info.values())


print()

print(" ==== 6. for문으로 출력 ====")
member = {"name" : "카리나", "phone" : "010-1212-3434", "birth" : "20000411"}

# for 개별값 in 집합
for key in member.keys():
    print(key , end=" ")  # end = "" : 줄바꿈 방지
print()     # name phone birth

# keys 객체를 튜플로 생성
member_tuple = tuple(member.keys())
print("member_tuple : ", member_tuple)      # member_tuple :  ('name', 'phone', 'birth')

print()
print()

print(" ==== 7. 딕셔너리의 아이템 ====")
# 7-1. 딕셔너리의 아이템
print(type(member))     # <class 'dict'>
print(type(member.items()))     # <class 'dict_items'>

print("member.items() : ", member.items()) 
# member.items() :  dict_items([('name', '카리나'), ('phone', '010-1212-3434'), ('birth', '20000411')])
# member 딕셔너리의 key-value 정보들이 튜플 안에 들어가게됨

print()
print()

# 7-2. 딕셔너리의 아이템 응용
# 편의점 재고관리
gs = {'milk' : 5, 'chocolate' : 4, 'jelly' : 3, 'snak' : 2, 'juice' : 2, 'potato':1}

ob = input("물건의 이름을 입력하세요 : ")
print("해당 물품 재고 현황 : " , gs.get(ob))       # 물건의 이름을 입력하세요 : juice
                                                # 해당 물품 재고 현황 :  2


                                                