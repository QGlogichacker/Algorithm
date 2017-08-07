import numpy as np
from numpy import *
#     创建数组最简单的办法是使用array函数。它接受一切序列型的对象（包括其他数组），然后产生一个新的含有传入数据的NumPy数组。以一个列表的转换为例：
data1=[6,7.5,8,0,1]    #创建列表
arr1=np.array(data1)    #转换为数组
print("转换为一维数组")
print(arr1)
print("数据类型",arr1.dtype)    #数据类型保存在dtype对象中
arr1=np.array([1,2,3],dtype=np.int8)    #解释为特定数据类型
print(arr1)

data2=[[1,2,3,4],[5,6,7,8]]    #创建嵌套序列（由等长列表组成的列表）
arr2=np.array(data2)    #转换为多维数组
print("转换为二维数组")
print(arr2)

print(zeros(10))    #创建指定长度(10)的全0数组
print(zeros((10,10)))    #如果要那样的话需要一个shape
print(ones((3,6)))    #创建指定长度的(3行6列二维)的全1数组

print("内置函数range",range(10))    #创建指定数量的顺序列表（内置函数,默认0开始）
print("numpy函数arange",arange(10))    #创建指定数量的顺序数组

print("单位阵eye")
print(eye(10))    #创建一个正方的N×N单位矩阵

print('''
# 总结：
# 首先是array，必须要指定是numpy库中的，否则会出大事
# 然后是创建数组，可以创建一维二维等等数组，也可以指定数字类型
# 然后是zeros和ones，他们接受的，是shape(一个tuple)作为参数，而不是两个参数
# range和arange有所不同，实际上arange产生了一个数组，range产生了序列生成器
# 最常用的应该就是单位阵了吧
''')
