# 집합
# set() 함수를 사용해 리스트 를 집합으로
s1 = set([1, 2, 3])

# 딕셔너리와 유사하게 생겼지만 키가 없으면 집합임
s1 = {1, 2, 3}

# 집합은 순서가 없고 중복을 제거함
s2 = set("Hello")  # {'e', 'H', 'o', 'l'}

# 집합을 사용해 리스트의 중복제거
list1 = [1, 2, 3, 4, 1, 2]
set1 = set(list1)  # {1, 2, 3, 4}
list1 = list(set1)  # 1, 2, 3, 4]

# 리스트 와 튜플 과 집합은 변환이 자유로운편
s = set([1, 2, 3])
t = tuple(s)
l = list(t)

# s1 = set() 로 빈집합 생성
# s1 = {} 와 같이 할경우는 딕셔너리 형이 됨
# 집합은 순서가 없으므로 인덱스를 사용할수없음

# 리스트와 튜플을 집합으로 변경해보기
days_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days_set = set(days_list)

fruits_tuple = ("apple", "orange", "water melon")
fruits_set = set(fruits_tuple)

# 문자열 넣기
h_str = "hello"
h_set = set(h_str)

# 교집합
s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}

s3 = s1 & s2  # {4, 5, 6}
s3 = s1.intersection(s2)

# 합집합
s3 = s1 | s2  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
s3 = s1.union(s2)

# 차집합
s3 = s1 - s2  # {1, 2, 3}
s3 = s1.difference(s2)

# 대칭 차집합 (합집합에서 교집합을 뺌)
s3 = s1.symmetric_difference(s2)

# 집합의 함수

# add() 값 추가하기
s1 = {1, 2, 3}
s1.add(4)  # {1, 2, 3, 4}

# update() 여러개 값 추가하기
s1 = {1, 2, 3}
s1.update({4, 5})  # {1, 2, 3, 4, 5}

# remove(), discard() 특정 값 제거하기
s1 = {1, 2, 3}
s1.discard(3)  # {1, 2}
s1.remove(2)  # {1}

# Q1 2개 집합에 포함된 항목을 제거하자
s1 = {"a", "b", "c", "d", "e"}
s2 = {"c", "d", "e", "f", "g"}
s = s1 - s2  # {'b', 'a'}

# Q2 a 에 d, e, f 추가하기
a = set("abc")
a.update(set("def"))
