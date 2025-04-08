"""
클래스
"""


class User:
    # 클래스의 변수를 선언하지 않아도 알아서 새로 생성함
    phone_number = ""
    email_address = ""
    name = ""

    # 초기 initalize 함수 (자바의 생성자 와 같음)
    # 진짜 java 의 생성자와 같으려면 __init__ 을 쓰면 클래스를 생성할때 매개변수로 집어넣어 초기화 할수있다.
    def init(self, phone_number, email_address, name):
        self.phone_number = phone_number
        self.email_address = email_address
        self.name = name

    def getPhoneNumber(self):
        return self.phone_number

    def getEmail(self):
        return self.email_address

    def getName(self):
        return self.name


user1 = User()
user1.init("010-9852-5508", "kimkva@naver.com", "김준선")
# print(user1.getPhoneNumber())
# print(user1.getEmail())
# print(user1.getName())


class User:
    phone_number = ""
    email_address = ""
    name = ""

    # 초기 initalize 함수 (자바의 생성자 와 같음)
    # 진짜 java 의 생성자와 같으려면 __init__ 을 쓰면 클래스를 생성할때 매개변수로 집어넣어 초기화 할수있다.
    def __init__(self, phone_number, email_address, name):
        self.phone_number = phone_number
        self.email_address = email_address
        self.name = name

    def getPhoneNumber(self):
        return self.phone_number

    def getEmail(self):
        return self.email_address

    def getName(self):
        return self.name


user1 = User("010-9852-5508", "kimkva@naver.com", "김준선")
# print(user1.getPhoneNumber())
# print(user1.getEmail())
# print(user1.getName())


# 클래스 예제
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

# print(cal1.add(3))  # 3
# print(cal1.add(4))  # 7
# print(cal2.add(3))  # 3
# print(cal2.add(7))  # 10


# 클래스 예제2
# 속성을 동적으로 생성하기때문에 setdata() 를 호출하기전에는 a.first 를 호출할수없음
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


a = FourCal()

a.setdata(4, 2)
# print(a.first)  # 4
# print(a.second)  # 2


# 클래스 예제3
# self. 의 호출이 아닌 객체. 으로 호출할때의 차이
class FourCal:
    count = 0

    def stadata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        FourCal.count += 1
        return result


a = FourCal()
b = FourCal()

a.stadata(4, 2)
# print(a.first)  # 4
# print(a.second)  # 2
# print(a.sum())  # 6

# print(FourCal.count)  # 1

# b.stadata(7, 8)
# print(b.sum())  # 15
# print(FourCal.count)  # 2


# 클래스예제 4
# 클래스 변수와 인스턴스 변수 를 헷갈리지 말어라
# 변수이름을 헷갈리게 하지말고 구분하면 알아보기 쉬움
class Daeheeyun:
    class_value = 0

    def __init__(self):
        self.instance_value = 0

    def set_class_value(self):
        Daeheeyun.class_value = 10

    def set_instace_value(self):
        self.class_value = 20


instance1 = Daeheeyun()
instance2 = Daeheeyun()

instance1.set_class_value()
# print(instance1.class_value, instance2.class_value)  # 10 10
instance1.set_instace_value()
# print(instance1.class_value, instance2.class_value)  # 20 10

# instance2 는 class_value 가 없는것임 출력되는 10은 Daeheeyun 클래스가 가지고있다고 봐야함
# print(instance1.__dict__)  # {'instance_value': 0, 'class_value': 20}
# print(instance2.__dict__)  # {'instance_value': 0}

"""
상속
요즘은 잘 안쓴다고...
"""


class FourCal:
    def __init__(self, first, second):
        self.second = second
        self.first = first

    def sum(self):
        return self.first + self.second


class MoreFourCal(FourCal):
    def pow(self):
        return self.first**self.second


m = MoreFourCal(4, 2)  # 부모의 __init__ 을 가져다가 사용함
# print(m.pow())  # 16
# print(m.sum())  # 6 / 부모의 sum() 함수를 가져옴
# print(m.first)  # 4 / 부모로 부터 상속받은 변수도 가져옴


# 상속 예제 1
class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def mul(self):
        return self.first * self.second


class Scientific_Calculator(Calculator):
    pass  # 아무 작업도 하지않음


scientific1 = Scientific_Calculator(6, 6)
# print(scientific1.mul())  # 36


# 상속 예제2
# 함수 오버로딩
# 부모에게 있는 함수를 자식이 공통으로 선언하면 자식클래스의 것으로 덮어쓰기됨
class BaseClass:
    def myfunc(self):
        print("BaseClass's myfunc")


class InhClass(BaseClass):
    def myfunc(self):
        print("InhClass's my func")


ex1 = BaseClass()
# ex1.myfunc()  # BaseClass's myfunc

ex2 = InhClass()
# ex2.myfunc()  # InhClass's my func


# 상속 예제3
# 다중 상속
# 호출될때 나 자신 먼저 그 이후 선언된 부모 순서대로 찾음 앞에서 찾으면 뒤는 나오지않음
class Base1:
    def myfunc(self):
        print("Base1")


class Base2:
    member1 = 100
    member2 = 200

    def myfunc(self, a, b):
        print(a - b)


class Base3:
    def myfunc2(self, a, b):
        print(a * b)


class InhClass(Base1, Base2, Base3):
    member3 = 300


ex1 = InhClass()
# ex1.myfunc()  # Base1

# ex1.myfunc2(ex1.member1, ex1.member3)  # 100 * 300 == 30000


# 상속 예제 4
# 다이아몬스 상속
# B 는 A를 상속받았지만 D 는 B 와 C 만 상속받았기에 최종적으로 오버로딩 된 B 와 C 가 대상임 그중에 순서가 앞인 B 가 당첨
class A:
    def greeting(self):
        print("안녕하세요 A 입니다.")


class B(A):
    def greeting(self):
        print("안녕하세요 B 입니다.")


class C(A):
    def greeting(self):
        print("안녕하세요 C 입니다.")


class D(B, C):
    pass


x = D()
# x.greeting()  # 안녕하세요 B 입니다.
# print(D.mro())
# mro() 함수 : 우선순위 나와용
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# 상속 예제 5
# 함수 오버라이딩
# 부모의 함수도 호출하며 자식의 함수도 재정의 할수있음


class Person:
    def greeting(self):
        print("안녕하세요")


class Student(Person):
    def greeting(self):
        super().greeting()
        print("저는 파이썬 코딩 도장 학생입니다.")


# tom = Person()
# tom.greeting()  # 안녕하세요
# james = Student()
# james.greeting()  # 안녕하세요 저는 파이썬 코딩 도장 학생입니다.


class Data:
    def __init__(self, data):
        tmp = data.split("|")
        self.name = tmp[0]
        self.age = tmp[1]
        self.grade = tmp[2]

    def print_age(self):
        print(self.age)

    def print_grade(self):
        print(f"{self.name}님 당신의 점수는 {self.grade}입니다. ")


data = Data("홍길동|42|A")

data.print_age()
data.print_grade()
