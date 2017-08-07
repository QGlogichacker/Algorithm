import numpy as np
from numpy import *

arr = np.arange(10)
print("最开始的数组\n", arr)
print("和其他语言的数组访问法一样，arr[5] =", arr[5])    # 索引第6个元素
print("# 可以用arr[5:8] = 12\n令第6到第9个元素等于12")

print("# 切片功能可以索引第6到第9个元素(不含9)作为数组\n", arr[5:8])
print("# 数组切片是原始数据的视图，视图上的任何修改都会反映到原数组")
arr_slice = arr[5:8]
arr_slice[:] = 64    # 将数组切片的全部元素改为64
print("# 看看现在的数组\n", arr)

arr[5:8].copy()    # 得到数组切片的一份副本

arr2d=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("# 索引二维数组第3行\n", arr2d[2])
print("# 用列表表示位置\n", arr2d[0, 2], "\n# 对比原本的\n", arr2d[0][2]) #等价索引1行3列元素
print("# 索引第1行和第2行（不含第3行）\n", arr2d[:2])
print("# 索引第1列 \n", arr2d[:, :1])
print("# 使用负数索引将从尾部开始选取行\n", arr2d[:-2])
print("# 如果要按某个维度逆序，可以直接在切片第三个参数(步长)填-1\n", arr2d[::-1, :])

print("# 用同一个阵组合分块母阵，注意第二个参数是一个tuple，表示x行y列\n", tile(arr, (6, 1)))
