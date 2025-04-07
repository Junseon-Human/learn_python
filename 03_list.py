fruits = ["banana", "apple", "orange", "kiwi"]
# print('리스트 출력 :',fruits)
# print('타입 확인 :' , type(fruits))

mixed_list = [100, 200, 400, "apple"]
# print('리스트 출력 :',mixed_list)

# 값이있는 List 생성
list1 = [1, 2, 3]

# 빈 리스트생성
list1 = list()
list2 = []

# 리스트로 형변환
tuple1 = (1, 2)
list3 = list(tuple1)

# 범위 지정하여 생성
# 1~10 까지 출력하려면 range 함수를 사용 하여 1, 11 값을 준다.
list4 = list(range(1, 11))

# 문자열을 주면 각각 쪼개서 생성함
list5 = list("ABCDEF")

# Q1 짝수를 가지는 리스트 생성하기
even_list = [2, 4, 6, 8, 10]

# Q2 range() 함수를 이용하여 1번 다시풀기
# range(start, end, step)
even_list = list(range(2, 11, 2))

# Q3 문자열로 이루어진 리스트생성
nations = ["Korea", "China", "India", "Nepal"]

# Q4 문자열 리스트 생성
friends = ["철수", "영희", "미연", "미숙", "춘자"]

# Q5 문자열 'XYZ' 를 이용하여 각 요소를 가진 리스트 생성
string = list("XYZ")

# 리스트의 인덱싱
a = [1, 2, 3, ["a", "b", "c"]]

# Q1 2~10 까지중 소수를 요소로 가지는 리스트의 첫번째 요소 출력
prime_list = [2, 3, 5, 7]
# print(f'prime_list의 첫 원소 : {prime_list[0]}')

# Q2 prime_list 의 마지막 요소를 양수 인덱스로 출력
# print(f'prime_list의 마지막 원소 {prime_list[3]}')

# Q2 prime_list 의 마지막 요소를 음수 인덱스로 출력
# print(f'prime_list의 마지막 원소 {prime_list[-1]}')

# Q4 문자열 리스트위 첫 원소 출력
nations = ["Korea", "China", "Russia", "Malaysia"]
# print(f'nations의 첫 원소 : {nations[0]}')

# Q5 nations 의 마지막 원소를 음수 인덱스를 사용
# print(f'nations의 마지막 원소 : {nations[-1]}')

# Q6 nations 의 마지막 원소를 len(nations)-1 사용
# print(f'nations의 마지막 원소 : {nations[len(nations) - 1]}')

# 리스트의 슬라이싱
# list[start:end:step] range 함수와 마찬가지로 step 가능함
# a[1::-1] 잘 이해할것

a_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(f'리스트의 1:5 슬라시싱 : {a_list[1:5]}')

# Q1 range(15) 함수를 이용하여 리스트 생성
n_list = list(range(15))

# Q2 슬라이싱 인덱스 지정
# print(f'처음부터 5개만 출력 {n_list[:6]}')
# print(f'5~10 까지 출력 : {n_list[6:11]}')
# print(f'11 부터 끝까지 출력 : {n_list[11:]}')
# print(f'짝수만 출력 : {n_list[2:11:2]}')
# print(f'10부터 6까지 역순으로 출력 : {n_list[10:5:-1]}')
# print(f'10부터 2까지 짝수만 출력 : {n_list[10:1:-2]}')

# 리스트의 연산

# + 는 덧셈이 아닌 붙이기
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b

# * 는 반복 생성
# 리스트 와 리스트는 곱할수없음 (에러발생)
d = a * 3

# 문자열로 변환시 [] 기호와 , 도 문자열로 변경됨
e = str(a) + "hi"

# == 연산자
# 리스트는 순서를 따지기때문에 값과 순서 모두 일치하면 동일하게 취급됨
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list3 = [4, 1, 2, 3]

list1 == list2  # True
list1 == list3  # False

# >, <, >=, <= 연산자 사용
# 문자열의 경우 사전적 순서를 비교한다.

list1 = [1, 2, 3, 4]
list2 = [2, 3, 3, 4]
result1 = list1 < list2  # True

# 리스트의 수정, 변경과 삭제
# 인덱스를 지정하여 수정
a = [1, 2, 3]
a[1] = 4

# 수정할때 1:2 같이 범위를 지정할때 list 를 넣어주면 list 의 요소가 분해되어 각각 하나씩 들어가며
# 인덱스를 지정하면 list 가 들어감
a = [1, 2, 3]
a[1:2] = ["a", "b", "c"]
# print(a)
a = [1, 2, 3]
a[1] = ["a", "b", "c"]
# print(a)

# 삭제
a = [1, 2, 3]
a[1:3] = []

# del list[인덱스]
a = [1, 2, 3]
del a[1:3]

# 리스트의 주요 함수

# append() 리스트에 요소 추가
a = [1, 2, 3]
a.append(4)
a.append([4, 5])

# sort() 리스트 정렬
a = [1, 4, 3, 2]
a.sort()

a = ["g", "f", "c", "d"]
a.sort()

a = ["이순신", "강감찬", "을지문덕"]
a.sort()

# sort() 의 오름차순 내림차순 정렬
a = [1, 5, 3, 4, 2]
# 오름차순 ( 기본값이기때문에 reverse 값을 주지 않아도 됨)
a.sort(reverse=False)
# 내림차순
a.sort(reverse=True)

# reverse() 순서 뒤집기
a = [1, 2, 3, 4]

# 위치 반환(index)
a = [1, 2, 3]
a.index(3)

# index는 값이 없으면 오류가 떨어짐
# a.index(5)

# insert() 요소 삽입
# insert(index, value)
# append() 와는 다르게 삽입 위치를 지정하여 삽입가능함
a = [1, 2, 3]
a.insert(1, 8)  # 1번 인덱스에 8을 삽입

# remove(value) 첫번째로 나오는 value 값을 삭제
# deL() 은 인덱스를 넣는반면 remove() 는 value 를 넣어 찾아 삭제함
a = [1, 1, 2, 3]
a.remove(1)

# pop(index) 리스트의 인덱스 요소를 리턴하며 해당요소는 삭제
# pop() 으로 인덱스를 지정하지않으면 마지막 원소를 가져옴
a = [1, 2, 3, 1, 2, 3]
b = a.pop(3)

# extend()
a = [1, 2, 3]
a.extend([4, 5])

# Q1 append() 와 extend() 의 차이 알아보기
a = [1, 2, 3]
b = [10, 20, 30]
a.append(b)

a = [1, 2, 3]
b = [10, 20, 30]
a.extend(b)

# Q2 1~10의 값을 가지는 리스트 만들기
a = list(range(1, 11))

# Q3 insert() 를 사용해 맨앞 값에 0 삽입
a.insert(0, 0)


# Q4 a 를 역순으로 바꿔
a.reverse()

# Q5 a 의 제일 마지막 원소를 가져오고 출력
last_element = a.pop()
# print(f'마지막 요소 : {last_element}\n변경후 리스트 : {a}')

# Q6 리스트 중에 you too 만 출력
a = ["Life", "is", "too", "short", "you", "need", "python"]
# print(a[4], a[2])

# Q7 Life is too short 문자열로 만들기
result = " ".join(a[:4])
# print(result)

# Q8 리스트의 갯수(사이즈) 구하기
a = [1, 2, 3]
len(a)

# Q9 리스트 를 1, 3, 5 로 만들어보자
a = [1, 2, 3, 4, 5]
a.pop(1)
a.remove(4)
