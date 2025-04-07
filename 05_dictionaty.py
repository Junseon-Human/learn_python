# 딕셔너리 선언
person = {"이름": "김준선"}

# 추가
person["주소"] = "부평구"

# 삭제
# 키값이 없는것을 넣으면 에러
del person["주소"]

# 수정
person["이름"] = "홍길동"

# 쌍 추가, 삭제하기
# 추가
a = {1: "a"}
a[2] = "b"
a["name"] = "pey"

# 삭제
del a[1]

# 딕셔너리의 key 에는 list 는 사용불가 tuple 는 사용가능
# key 값은 변경되어서는 안되기때문에 list는 사용이 불가능한것임

# 키 값 뽑아오기
# keys() 를 사용해서 리스트를 반환함
a = {"name": "pey", "phone": "011010101", "birth": "1118"}

# 다음 딕녀너리의 키와 밸류를 찍어보자
dic = {
    "이름": "홍길동",
    "나이": 26,
    "몸무게": 82,
    "직업": "율도국왕",
    "주소": "경상북고 울릉군 울릉읍",
}
dic_items = dic.items()
# for item in dic_items:
#     (key, value) = item
#     print(key, value)

# Q1 표를 딕셔너리로 만들기
dic = {"name": "홍길동", "birth": "1128", "age": "30"}

# Q2 딕셔너리 a 에서 b 의 해당하는 값을 추출하고 삭제
# 1)
a = {"A": 90, "B": 80, "C": 70}
b = a.pop("B")

# 2)
a = {"A": 90, "B": 80, "C": 70}
b = a["B"]
del a["B"]

# Q3 딕셔너리 a 에서 'C'라는 key에 해당되는 value를 출력하는 프로그램이다.
# a 딕셔너리에는 'C'라는 key 가 없으므로 위와같은 오류가 발생한다 'C'에 해당되는 키값이 없을 경우 오류 대신 70을 얻을수있도록 수정
a = {"A": 90, "B": 80}

b = a.get("C", 70)

# Q4 딕셔너리 a 의 최소 값을 출력
a = {"A": 90, "B": 80, "C": 70}

min = 100
for value in a.values():
    if min > value:
        min = value
# print(f"최솟값 : {min}")

# Q5 딕셔너리를 리스트로 만들기
a = {"A": 90, "B": 80, "C": 70}
# print(list(a.items()))
