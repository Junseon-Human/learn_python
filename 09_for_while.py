# while 문
# while 조건식:
i = 0
while i < 5:
    i += 1

# for 문
for i in range(10):
    i += 1

# 문자열을 순회하다가 모음을 만나면 정지
st = "Programming"
for ch in st:
    if ch.lower() in ["a", "e", "i", "o", "u"]:
        # break     # 조건문에 들어오면 중지됨
        continue  # 조건문에 들어오면 반복문의 시작지점으로 감
    # print(ch)
# print("End")

# 나무 넘어갑니다

# for tree_hit in range(1, 11):
#     print(f"나무를 {tree_hit} 번찍었다")
#     if tree_hit == 10:
#         print(f"나무 넘어가유")

# tree_hit = 0
# while tree_hit < 10:
#     tree_hit += 1
#     print(f"나무를 {tree_hit}번 찍었다")
#     if tree_hit == 10:
#         print("나무 넘어가유")

# while 문 으로 프롬프트 돌리기

# prompt = """1. Add
# 2. Del
# 3. List
# 4. Quit
# Enter number : """

# i = 0
# while i != 4:
#     i = int(input(prompt))

# while 문으로 커피 자판기 만들기ㅋ

# coffee = 3
# while True:
#     print(f"남은 커피 : {coffee} 잔")
#     money = int(input("돈을 넣어주세요 : "))
#     if money == 300:
#         print("커피드림")
#         coffee -= 1
#     elif money > 300:
#         print(f"커피 랑 잔돈 {money - 300}원 드림")
#         coffee -= 1
#     else:
#         print(f"돈이 모지라요 최소 300원이염")
#     if not coffee:
#         print("커피 다떨어짐 ㅅㄱ")
#         break

# Q1 1~100 까지 더한 수
sum = 0
for i in range(1, 101):
    sum += i
# 5050

# Q2 1 부터 1000 까지의 자연수중 3의 배수의 합을 구하세용
sum = 0
for i in range(3, 100, 3):
    sum += i
# 1683
"""
Q3 리스트에서 50점 이상의 점수들의 총합을 구하기
"""
A = [20, 55, 67, 82, 45, 44, 90, 87, 100, 25]
sum = 0
for score in A:
    if score >= 50:
        sum += score
# 481

"""
Q4 while 문으로 별 산을 만들어보아요
"""
i = 1
while i < 6:
    # print("*" * i)
    i += 1

"""
파이썬의 for 문!
print() 의 end 옵션으로 줄넘김을 하지않고 한번에 표현가능
"""
numbers = [11, 22, 33, 44, 55, 66]
# for n in numbers:
# print(n, end=" ")

summer_fruits = ["수박", "참외", "체리", "포도"]
# for fruit in summer_fruits:
#     print(fruit, end=" ")

"""
구구단 가보자잇
"""

# for i in range(2, 10):
#     print(f"{i} 단")
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j}", end=" ")
# print()
# print("=" * 100)

"""
튜플을 for 문에 넣을때
for 의 변수쪽에 하나가 아니라 여러개를 쓸수있음
해당 튜플은 2개값을 가지고있기때문에 두개 변수로 받을수있음
"""

a = [(1, 2), (3, 4), (5, 6)]
# for first, last in a:
#     print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
# for mark in marks:
#     number += number + 1
#     if mark >= 60:
#         print(f"{number}번 학생은 합격입니다.")
#     else:
#         print(f"{number}번 학생은 불합격 입니다.")

"""
for else 문
"""
# for i in range(3):
#     print(f"i = {i}")
# else:
#     print("END")

"""
for break continue
for 문 안에서 continue 를 만나면 나머지를 실행하지않고 for 문의 처음으로 돌아가 이어서 수행함
"""
list1 = ["I", "love", "python"]

# for index in range(len(list1)):
#     if list1[index] == "love":
#         print(f"love를 찾았습니다. 인덱스는 {index} 입니다.")
#         break

"""
변수를 사용하지않을때는 _ 로 쓸수있음
"""
# for _ in range(10):
#     print("안녕하세요")

"""
인덱스 값 사용하기
enumerrate()
"""
names = ["A", "B", "C"]
i = 0

# # 사용전
# for name in names:
#     print(i, name)
#     i += 1

# # 사용후
# for idx, name in enumerate(names):
#     print(idx, name)
#     i += 1

"""
zip() 함수
"""
names = ["A", "B", "C"]
scores = [70, 80, 90]

# for name, score in zip(names, scores):
#     print(f"이름 {name}, 점수: {score}")

"""
길이가 다른 리스트를 zip 했을때는 길이가 작은 갯수만큼만 됨
"""

data1 = ["Python", "076923", "TUNDAEHEE", "X"]
data2 = ["파이썬", "076923", "윤대희"]

# for i, (datum1, datum2) in enumerate(zip(data1, data2)):
#     print(i, datum1, datum2)

"""
리스트 내포
"""

# 1)
list1 = list()
for i in range(3, 13, 3):
    list1.append(i)

result = [num * 3 for num in range(1, 5)]
result = [num * 3 for num in range(1, 5) if num % 2 == 0]

# 2) 중첩도 가능함
result = [x * y for x in range(2, 10) for y in range(1, 10)]

# 3) 튜플도 가능
result = tuple(x * y for x in range(2, 10) for y in range(1, 10))
# print(result)

# Q1 1부터 100까지 for 문으로 출력
# for n in range(1, 101):
#     print(n)

# Q2 5의 배수의 총합
sum = 0
for n in range(5, 1001, 5):
    sum += n
# print(sum)

# Q3 for 를 이용해서 리스트의 평균값 구하기
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for num in A:
    sum += num
avg = sum / len(A)

# Q4 리스트의 갯수
blood_list = ["A", "B", "O", "AB", "AB", "O", "A", "B", "O", "B", "AB"]

blood_dict = dict()
for blood in blood_list:
    blood_dict[blood] = blood_dict.get(blood, 0) + 1

# for blood, count in blood_dict.items():
#     print(f"{blood} 형은 {count}명")

# Q5 리스트 내포 로 변환하기

# 기존
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)

# 변환 후
result = [n * 2 for n in numbers if n % 2 == 1]
