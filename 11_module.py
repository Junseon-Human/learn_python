"""
import 모듈명
from 모듈명 import 함수명
쓸때는
모듈명.함수명
"""

from math import sqrt
import math

# print(sqrt(16))  # 루트 16
# print(math.ceil(3.2))  # 올림
# print(math.floor(2.9))  # 내림
# print(round(2.4))  # 반올림
# print(math.factorial(3))  # 팩토리얼

"""
as 를 사용하여 명칭 부여
"""
import math as mp

a = mp.pi

# 난수 뽑기
# rand() * 6 은 0~5 까지라서 1을 더하면 1~6나옴
from random import random as rn
import random

a = int(rn() * 6 + 1)

# 정수는 randint() 를 활용
a = random.randint(1, 6)

import datetime

a = datetime.datetime.now()  # 현재시간
a = datetime.datetime(2024, 1, 1, 0, 0)  # 지정 시간 연 월 일 시 분


# Q1 홀수인지 짝수인지 알려주는 함수 맨들기
def is_odd(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"


result = is_odd(4)


# Q2 입력으로 들어오는 모든 수의 평균값을 계산해주는 함수를 작성해보자
def my_average(*numbers):
    my_sum = sum(numbers)
    return my_sum / len(numbers)


# print(my_average(10, 20, 30, 40))


# Q3 입력하는 숫자의 구구단을 출력하는 함수
def gugudan(number):
    print(f"{number} 단")
    for n in range(1, 10):
        print(f"{number} * {n} = {number * n}")


"""
람다
람다식으로 함수 만들기이
함수이름 = lambda 매개변수 : 표현식
"""
sum1 = lambda a, b: a + b

# 람다를 쓰면 def 를 쓸수없는 곳에도 쓸수있음
# ex 리스트

my_list = [lambda a, b: a + b, lambda a, b: a * b]
my_list[0](3, 4)  # 7

my_list[1](3, 4)  # 12

"""
람다 인자
"""
f = lambda: 1
f()  # 1

g = lambda x, y: x + y
g(1, 2)  # 3

(lambda x: x**3)
(3)  # 27


# 일반 함수 람다함수로
def add(x, y):
    return x + y


add(100, 200)  # 300

add = lambda x, y: x + y
add(100, 200)  # 300

# 람다의 가변 인자
f = lambda *x: max(x) * 2
f(1, 2, 5, 7, 200)  # 400

f = [lambda x: x + 1, lambda x: x + 2, lambda x: x + 3]
f[0](1)  # 2
f[1](1)  # 3
f[2](1)  # 4

# 딕셔너리에서 람다 활용
dic1 = {"add": lambda x, y: x + y, "sub": lambda x, y: x - y, "mul": lambda x, y: x * y}
dic1["add"](3, 4)  # 7
dic1["sub"](3, 4)  # -1
dic1["mul"](3, 4)  # 12


# Q1 일반 함수 람다함수 만들기
def sub(a, b):
    return a - b


result = sub(200, 100)  # 100

sub = lambda a, b: a - b
result = sub(200, 100)  # 100

"""
filter() 함수
filter (함수, 대상)
반환을 하려면 list(filter()) 방식으로 사용
"""
# 람다를 이용해 bool 을 return 하는 함수 f
f = lambda x: x > 0
list(filter(f, range(-5, 5)))  # [1, 2, 3, 4]

list1 = list(range(1, 8))
f = lambda x: x % 2 == 0
list(filter(f, list1))  # [2, 4, 6]


# 필터 함수는 값이 반환되는게 아닌 논리값 True, False 만 반환함
# return 에 연산을 한다고해도 값이 반환되지않음
def func(x):
    if x > 0:
        return x
    else:
        return x - 100


result = list(filter(func, range(-5, 5)))  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

# 반복문에 람다 써보기
# ages = [34, 39, 20, 18, 13, 54]
# print("성인 리스트 :")
# for a in filter(lambda x: x >= 19, ages):
#     print(a, end=" ")


# 음수값을 추출하는 필터 함수 정의
def minus_func(n):
    if n < 0:
        return True
    else:
        return False


# 람다 X
n_list = [-30, 45, -5, 90, 20, 53, 77, -36]
result = []
for n in filter(minus_func, n_list):
    result.append(n)

# 람다 O
n_list = [-30, 45, -5, 90, 20, 53, 77, -36]
for n in filter(lambda x: x < 0, n_list):
    result.append(n)

# for 문 도 제거
n_list = [-30, 45, -5, 90, 20, 53, 77, -36]
result = list(filter(lambda x: x < 0, n_list))

# 람다 예제
# Q1 n_list 중 짝수만 필터링 하는 리스트 생성하기
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 == 0, n_list))

"""
map 함수
map(적용시킬함수, 반복가능 객체)
"""

a = [1, 2, 3, 4, 5, 6, 7]


def square(x):
    return x**2


result = list(map(square, a))

# 람다로도 해보자
a = [1, 2, 3, 4, 5, 6, 7]
result = list(map(lambda x: x**2, a))

# Q1 리스트를 대문자로 변환해보자
a_list = ["a", "b", "c", "d"]


def to_upper(str):
    return str.upper()


result = list(map(to_upper, a_list))
result = list(map(lambda x: x.upper(), a_list))

# Q2 리스트를 n 배 하는 함수 맨들어바라
n_list = [10, 20, 30]


def twice(n_list):
    return n_list * 2


def triple(n_list):
    return n_list * 3


result = list(map(twice, n_list))
result = list(map(lambda x: x * 2, n_list))
result = list(map(triple, n_list))
result = list(map(lambda x: x * 3, n_list))


"""
zip()
기본적으로 묶어서 튜플로 반환함
"""
a = "YUN"
b = [1, 2, 3]
c = ("one", "two", "three")
result = list(zip(a, b, c))  # [('Y', 1, 'one') , ('U', 2, 'two'), ('N', 3, 'three')]
result = set(zip(a, b, c))  # {('U', 2, 'two'), ('N', 3, 'three'), ('Y', 1, 'one')}
result = dict(zip(a, b))  # {'Y': 1, 'U': 2, 'N': 3}

"""
reduce()
"""
from functools import reduce

a = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, a)  # 10

# 1부터 100 까지 더해라
result = reduce(lambda x, y: x + y, range(1, 101))  # 5050

# 1부터 10까지 계속 곱해봐라
result = reduce(lambda x, y: x * y, range(1, 11))  # 3628800


"""
리스트 컴프리헨션에 if 쓸때와 else 까지 쓰고싶을때
"""

list1 = [i**2 if i < 5 else i for i in range(1, 11)]
list1 = [i**2 for i in range(1, 11) if i < 5]

st = "Hello World"
result = [x.upper() for x in st]
result = list(map(str.upper, st))

# 문자열 갯수 파악
text = "cheese"
result = {i: text.count(i) for i in text}

# 2의 배수 이면서 3의배수 이면서 5의 배수 인것 뽑기
# if 다음 if 를 쓰면 and 연산임
result = [n for n in range(1, 31) if n % 2 == 0 if n % 3 == 0 if n % 5 == 0]

# 세제곱이 500이하가 되는 수를 1~10 사이에서 뽑아요
result = [x**3 for x in range(1, 11) if x**3 <= 500]

# 문자열에서 정수만 꺼낸 리스트 만들기
st = "Hello 1234 Python"
result = [x for x in st if x.isdigit()]


"""
iterator
반복자
"""
import numpy as np

_str = iter("1234")
_tuple = iter((1, 2, 3, 4))
_dict = iter({"a": 1, "b": 2, "c": 3})
_set = iter({1, 2, 3, 4})
_array = iter(np.array([[1, 2], [3, 4]]))
