# while True:
#     a = input("정수 입력해봐라 : ")
#     try:
#         a = int(a)
#     except:
#         print("디질래? 내가 정수 넣으랬지")
#         continue
#     if a == -1:
#         break
#     elif a % 2 == 0:
#         print(f"입력한 숫자 {a} 는 짝수요")
#     elif a % 2 == 1:
#         print(f"입력한 숫자 {a} 는 홀수요")


# 자바와 다르게 파이썬의 & 와 | 는 비트연산자
# if문에서 쓰려면 and 와 or 를 써야함

# a = 14
# b = 15
# if a % 2 == 0 & b % 2 == 0:
#     print("두수모두 짝수")
# elif a % 2 == 0 | b % 2 == 0:
#     print("두수중 하나는 짝수")

# a = 14
# b = 15
# if a % 2 == 0 and b % 2 == 0:
#     print("두수모두 짝수")
# elif a % 2 == 0 or b % 2 == 0:
#     print("두수중 하나는 짝수")

# score = int(input("점수를 입력하세요 : "))
# grade = ""
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "루저"
# print(f"당신은 {grade}!")

# speed = int(input("속도를 입력하세요 : "))

# if speed >= 100:
#     print("호에에 너무 빨라요")
# elif speed > 60:
#     print("중속")
# else:
#     print("저속")

# 삼항연산자
"참일때" if 0 == 0 else "거짓일때"

# Q1
money = 5000
card = False

# if money >= 4000 or card:
#     print("택시탑승가능")
# else:
#     print("탑승불가")

# print("택시탑승가능") if money >= 4000 or card else print("택시탑승불가")

# Q2
lucky_list = [1, 9, 23, 46]


no = 11
# print("야호!") if no in lucky_list else print("실패!")

# Q3
no = 0
str1 = ""

str1 = "짝수" if no % 2 == 0 else "홀수"
# print(f"{no}는 {str1}입니당")
