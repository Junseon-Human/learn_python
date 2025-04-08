"""
numpy
행렬 연산을 위함
"""

import numpy

csv_data = numpy.loadtxt("data.csv", delimiter=",")
# print(csv_data[0][0])
# print(csv_data)

"""
pandas
테이블 연산을 위해 주로 쓰임
"""

import pandas

csv_data = pandas.read_csv("com.csv", header=0)
print(csv_data)
