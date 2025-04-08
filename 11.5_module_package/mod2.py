# mod2.py
PI = 3.141592


class Math:
    def solv(self, r):
        return PI * (r**2)


def sum(a, b):
    return a + b


# 밑의 실행구문은 다른곳에서 모듈을 로드 하는 순간 실행하게됨
# 파이썬 코드를 실행할때 name 은 main 을 가지게 됨
if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))
"""
# 파이썬 실행
python
# sys 임포트
import sys
# 현재 시스템 패스 확인
sys.path
# os 임포트
>>> import os
# 현재 경로 확인
>>> os.getcwd()
# 시스템 패스에 현재 경로 추가
>>> sys.path.append(os.getcwd())
# 시스템 패스에 현재 경로 삭제
>>> sys.path.remove(os.getcwd())
>>> sys.path
"""
