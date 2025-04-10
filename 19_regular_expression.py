"""
정규표현식이 유용한 경우
1) 주민번호 와 같이 패턴이 정해져있는 경우
2) 비밀번호 와 같이 패턴이 있는경우
 1) 8자리 이상
 2) 영문 대문자/소문자 1개 이상씩 포함
 3) 특수문자 허용안함
 4) 특수문자는 !@# 만 허용
3) 검색 할때
 1) 하지만 보통 DB에 의존함 (응용 부분에 가까움)
"""

# 정규 표현식 사용 전
data = """
park 800905-1049118
kim 700905-1059119
"""
result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
# print("\n".join(result))

# 정규 표현식 사용
import re

data = """
park 800905-1049118
kim 700905-1059119
"""

# pat = re.compile("(\d{6})[-]\d{7}")
# print(pat.sub("\g<1>-*******", data))

"""match()"""

p = re.compile("[a-z]+")  # a ~ z 소문자 0개 이상
m = p.match("python")  # 6개
m = p.match("pytHon")  # 3개 중간에 대문자가 있음

m = p.match("string goes here")  # 정규표현식에 따라 띄어쓰기는 허용되지않음
# if m:
#     print("match found:", m.group())  # group() 매치된 문자열을 돌려줌
# else:
#     print("no match")

m = p.match("python")
# print(m.start())  # 매치된 문자열의 시작 인덱스
# print(m.end())  # 매치된 문자열의 마지막 인덱스
# print(m.group())  # 매치된 문자열을 반환
# print(m.span())  # 매치된 문자열의 시작과 끝 인덱스를 튜플로 반환

"""search()
match() 랑은 다르게 중간에 정규표현식에 맞지 않으면 중단하는게 아니라 건너 뛴다 
단 구분되어있지 않으면 match 와 동일함 ex) 3 python = 'python', py3thon = 'py'
"""
m = p.search("3 python")
# print(m)  # <re.Match object; span=(2, 8), match='python'>

"""findall()
각각 문자열에 정규표현식을 적용하고 리스트로 반환
"""
result = p.findall("life is too short")
# print(result) # ['life', 'is', 'too', 'short']

"""finditer()
반복 가능한 객체로 돌려준다 작동 자체는 findall 과 동일함
"""
result = p.finditer("life is too short")
# print(result)

"""
정규표현식의 옵션
"""

"""DOTALL, S"""
p = re.compile("a.b")  # . 은 모든 문자를 포함함 단 \n 문자는 제외함
m = p.match("a\nb")
# print(m)  # None 개행문자가 포함되었기때문에 매치되지않음

p = re.compile("a.b", re.DOTALL)  # 메타문자의 \n 문자를 매치에 포함
m = p.match("a\nb")
# print(m)  # <re.Match object; span=(0, 3), match='a\nb'>

"""IGNORECASE, I"""
p = re.compile("a.b")  # . 은 모든 문자를 포함함 단 \n 문자는 제외함
m = p.match("AxB")
# print(m)

p = re.compile("a.b", re.IGNORECASE)  # 정규표현식 조건의 대소문자를 무시함
m = p.match("AxB")
# print(m)  # <re.Match object; span=(0, 3), match='AxB'>

"""MULTILINE, M"""
"""한줄만 찾을때"""
p = re.compile(
    r"^python\s\w+"
)  # ^ = 시작을 지정 \s = 뒤에 공백이 있어야함 \w = 뒤에 문자하나 \w+ = 뒤에 문자열 하나
data = """python one
life is too short
python two
you need python
python three"""

# print(p.findall(data))  # ['python one']

"""여러줄을 찾고싶을때 MUTILINE 을 씀"""
p = re.compile(r"^python\s\w+", re.MULTILINE)
# print(p.findall(data))  # ['python one', 'python two', 'python three']

"""정규식 표현이 복잡할 경우 여러줄로 나누어 주석을 달면 이해하기 좋음"""
# 기존 정규표현식
charref = re.compile(r"&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);")

# 여러줄로 나누어 표현
charref = re.compile(
    r"""
    &[#]                # Start of a numeric entity reference
    (
        0[0-7]+         # Octal form
      | [0-9]+          # Decimal form
      | x[0-9a-fA-F]+   # Hexadecimal form
    )
    ;                   # Trailing semicolon
""",
    re.VERBOSE,
)

"""정규표현식의 메타문자"""
"""
[]
[abc] 는 'abc' 가 아니라 a, b, c 각각 하나를 의미
[a-zA-Z0-9_] 영어 소문자, 영어 대문자, 숫자 0~9, 언더스코어 중 하나를 의미
[^] []안에서 ^ 는 시작하는 뜻이 아닌 반대문제
[^0-9] 숫자가 아닌 문자
"""

"""| : OR연산자로 “또는”이라는 의미
• a(b|c) : a 다음에 문자 b 또는 c가 한번 따라 나온다는 의미
• a(b|c)+ : a 다음에 문자 b 또는 c가 한번 이상 따라 나온다는 의미"""

"""( ) : 소괄호 속에 들어있는 내용을 하나의 그룹으로 간주
• a(bc) : a 다음에 나오는 bc를 하나의 그룹으로 간주
• a(bc)+ : a 다음에 그룹 bc가 한 번 이상 나온다는 것을 의미"""

# 예제 1
text = """이름 : 김철수
전화번호 : 010 - 1234 - 1234
나이 : 30
성별 : 남"""

# 숫자로 이루어진 모든 값을 리스트로 저장
result = re.findall(r"\d+", text)

# 숫자가 아닌 모든 값을 리스트로 저장
result = re.findall(r"\D+", text)

# 문자와 숫자가 아닌 값 찾기
result = re.findall(r"\W+", text)

# 예제2
with open("etc/doremisong.txt", "r") as file:
    mytext = file.read()
    exp1 = r"\s...\s"
    # print("exp1", re.findall(exp1, mytext))

    exp2 = r"([a-zA-Z]+),"
    # print("exp2", re.findall(exp2, mytext))

# 예제3
with open("etc/hunmin.txt", "r", encoding="utf-8") as hunmin:
    hantext = hunmin.read()
    exp1 = r"[가-힝]{5}"
    # print("exp1: ", re.findall(exp1, hantext))

    exp2 = r"\s사[가-힝]*\s"
    # print("exp2 : ", re.findall(exp2, hantext))

# 예제4
telnum = True
tel_exp = "0[1-8][0-9]?-[0-9]{3,4}-[0-9]{4}"
# while telnum:
#     try:
#         telnum = input("[전화번호] >> ")
#         if not telnum:
#             raise Exception
#         result = re.match(tel_exp, telnum)
#     except:
#         print("입력오류 전화번호가 제대로 입력되지 않았습니다.")
#     else:
#         if result:
#             print("전화번호가 제대로 입력되었습니다.")
#         else:
#             print("전화번호가 형식에 맞지 않아요")
