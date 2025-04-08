import mycircle0
import myrect0
import mysquare

# 반지름이 5일때의 면적, 둘레를 구하고 x,y 위치를 100, 100 으로 보내보자.
print(mycircle0.get_area(5))
print(mycircle0.get_peri(5))
mycircle0.set_pos(100, 100)

# 너비가 3이고 높이가 4 인 직사각형의 면적, 둘레를 구하고, x, y 위치를 200, 200으로 설정하자
width = 3
height = 4
area = myrect0.get_area(3, 4)
peri = myrect0.get_peri(3, 4)
myrect0.set_pos(200, 200)

mysquare.get_area(5)

# __doc__ 로 설명을 출력할수도있음
print(mysquare.__doc__)
print(mysquare.get_area.__doc__)
