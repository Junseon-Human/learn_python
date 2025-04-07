"""
range()
range() 내부 매개변수는 정수만 가능 0.5 같은 실수는 불가능함
"""

a = list(range(1, 101))

a = list(range(2, 101, 2))

a = list(range(1, 100, 2))

a = list(range(-100, 0))

a = list(range(0, -101, -1))

"""
numpy 에서는 arange() 함수를 이용해 실수도 스탭으로 넣을수있음
반환은 list로 하지않고 numpy.ndarray 타입임
"""
import numpy as np

a = np.arange(0, 10, 0.5)

"""
함수 맨들기
"""


# def 함수명():
#   할 작업
def print_star():
    print("*" * 50)


# 함수 예제
def get_sum(a, b):
    return a + b


sum1 = get_sum(10, 20)
# print(f"두 수의 합은 : {sum}")


# return 값이 두개인 함수
# 튜플로 값이 반환됨
def sum_and_mul(x, y):
    return x + y, x * y


sum1, mul = sum_and_mul(3, 5)


# 근의 공식의 해를 구하는 함수 만들기
def get_root(a, b, c):
    r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1, r2


r1, r2 = get_root(1, 2, -8)
# print(r1, r2)


"""함수의 default 값"""


# 매개변수에 값을 넣어주면 함수를 호출할때 넣어주지않아도 알아서 적용함
def div(a, b=2):
    return a / b


# default 값은 뒤에서 부터 배치해야함 앞의 변수는 배치불가
def div(a, b=2, c=3):
    return a / b / c


# Q1 두 수의 차를 출력하는 함수 만들어봐
def print_sub(a, b):
    print(f" {a} 와 {b} 의 차는 {a - b} 입니다.")


# Q2 두 수의 곱을 출력해봐라
def print_mul(a, b):
    print(f"{a} 와 {b} 의 곱은 {a*b}")


"""
가변인자 전달하기
매개변수 앞에 * 붙이기
"""


def greet(*names):
    for name in names:
        print(f"안녕 {name}")


# 예제
def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # 55


# 매개변수가 여러개 일때 가변인자 넣기
def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result


sum_mul("sum", 1, 2, 3, 4, 5)  # 15
sum_mul("mul", 1, 2, 3, 4, 5)  # 120


# Q1 가변인자를 튜플로 출력하고 모든 인자들의 합과 평균 출력
def sum_nums(*numbers):
    print(f"{len(numbers)} 개의 인자 {numbers}")
    for number in numbers:
        sum = 0
        sum += number
    print(f"합계 {sum}, 평균 {sum / len(numbers)}")


# Q2 정수를 인자로 받을 수 있는데 이 인자의 개수가 가변적이다.
def min_nums(*numbers):
    min = numbers[0]
    for number in numbers[1:]:
        if min > number:
            min = number
    return min


"""
키워드 인자
매개변수 앞에 ** 를 붙여 선언함
딕셔너리로 반환함
"""


def func(**kwargs):
    print(kwargs)


# result1 = func(a=1)
# result2 = func(name="foo", age=3)

"""
가변 인자 와 키워드 인자를 섞어 쓸수있다
가변은 튜플로 키워드는 딕셔너리로 적용됨
"""


def func(*args, **kwargs):
    print(args)
    print(kwargs)


# func(1, 2, 3, name="foo", age=3)


def func(*data, **method):
    num = sum(data) * method["scale"]
    print(num, method["unit"], "입니다")


# func(3, 4, 5, scale=10, unit="개")


def func(*data, message, **method):
    print(message)

    num = sum(data) * method["scale"]
    print(num, method["unit"], "입니다.")


# func(3, 4, 5, message="계산된 값입니다.", scale=10, unit="개")


def func(message1, message2, *data, **method):
    print(message1)
    print(message2)

    num = sum(data) * method["scale"]
    print(num, method["unit"], "입니다.")


# func("계산된 값입니다.", "값이 10패 커져용", 3, 4, 5, scale=10, unit="개")

"""
매개변수 초기값 미리 설정하기
"""


def say_myself(name, old, man=True):
    print(f"나의 이름은 {name} 입니다. ")
    print(f"나이는 {old} 살 입니다.")

    if man:
        print("남자용")
    else:
        print("여자용")


# say_myself("김준선", 29)
# say_myself("김준선", 29, False)


"""
변수의 scope
전역 변수(Global variable)
지역 변수(Local variable)
"""


def print_sum():
    a = 100  # 지역 변수
    b = 200  # 지역 변수
    result = a + b  # 지역 변수
    # print(f"print sum() 내부: {a} 와 {b} 의 합 {result}")


a = 10  # 전역변수
b = 20  # 전역변수
print_sum()
result = a + b  # 전역 변수
# print(f"print sum() 외부: {a} 와 {b} 의 합 {result}")

# 함수에 대입


# 헷갈리게 하지말고 return 을 써보자
a = 1


def varTest(a):
    a = a + 1


varTest(a)

a = 1


def varTest(a):
    return a + 1


a = varTest(a)

# 또다른 방법으로는 global 변수 선언

a = 1


def vartest():
    global a
    a = a + 1


vartest()


# 제일 이해하기 좋은건 return 쓰기


# global 변수를 쓰면 더 헷갈림
def print_sum():
    global a, b
    a = 100
    b = 200
    result = a + b
    print(f"print sum() 내부 {a} 와 {b} 합은 {result} 입니다")


a = 10
b = 20
print_sum()
result = a + b
print(f"print sum() 외부 {a} 와 {b} 합은 {result} 입니다")
