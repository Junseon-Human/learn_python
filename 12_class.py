class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current = r + 1
            return r
        else:
            raise StopIteration


# for i in Counter(3):
#     print(i, end=" ")


# 1 부터 홀수를 무한으로 출력하는 클래스
class EvenCount:
    def __init__(self, n=1):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        t = self.n
        self.n += 2
        return t


my_counter = EvenCount()


class OddCount:
    def __init__(self, n=1):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 2
        if self.n < 20:
            return self.n
        else:
            raise StopIteration


for i in OddCount():
    print(i, end=" ")
