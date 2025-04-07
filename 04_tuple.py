# 튜플 만들기
t = ()
t = (1,)

t = (1, 2, 3)
t = 1, 2, 3

# 튜플은 수정 불가함
t = (0, 1, 2, 3)
# t[0] = 100

# 튜플 변환
n_list = [1, 2, 3]
t = tuple(n_list)

# packing 과 unpacking

# 패킹
a = (1, 2)
a[0]  # 1
a[1]  # 2

# 언패킹
c = (3, 4)
d, e = c
# d = 3, e = 4

# swap
# swap 사용하지 않고 함
a = 100
b = 200
temp = a
a = b
b = temp

# swap 사용
a = 100
b = 200
a, b = b, a

# 튜플의 연산도 list 와 같음
# + 는 이어 붙이기 * 는 반복

# Q1 다음 튜플의 최댓값을 구하시오
tuple1 = (1, 5, 250, 3, 200, 107, 143)
max_num = 0
for n in tuple1:
    if n > max_num:
        max_num = n
# print(f'가장 큰 숫자는 : {max_num} 입니다.')

# 문제 1번을 리스트로 변환하여 가지고 놀아보기
list1 = list(tuple1)
list1.sort()
tuple1 = tuple(list1)

# 튜플의 함수
# 리스트의 수정, 삭제, 삽입과 같은 함수는 사용할수없고 조회하는 류의 함수는 대부분 같은 동작을함
t = (10, 20, 30, 20, 20, 10, 50)
t.count(10)  # 2

t.index(20)  # 1

# 튜플을 리스트로 변환하여 항목 변경후 다시 튜플로 돌리기
t_fruits = ("apple", "banana", "water melon")
l_fruits = list(t_fruits)
l_fruits[1] = "kiwi"
t_fruits = tuple(l_fruits)
# print(f'변경 후 튜플 {t_fruits}')

# (1, 2, 3) 이라는 튜플에 4라는 값을 추가
t = (1, 2, 3)
t = t + (4,)
