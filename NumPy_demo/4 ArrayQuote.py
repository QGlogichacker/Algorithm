import numpy as np
from numpy import *

arr = np.arange(10)
print("最开始的数组\n", arr)
print("和其他语言的数组访问法一样，arr[5] =", arr[5])    # 索引第6个元素
print("# 可以用arr[5:8] = 12\n令第6到第9个元素等于12")

print("# arr[5:8] 切片功能可以索引第6到第9个元素(不含9)作为数组\n", arr[5:8])
print("# 数组切片是原始数据的视图，视图上的任何修改都会反映到原数组")
arr_slice = arr[5:8]
arr_slice[:] = 64
print("# 取arr[5:8]切片并将其全部元素改为64")
print("# 看看现在的数组\n", arr)

print("# 得到数组切片的一份副本,用copy()方法\narr[5:8].copy()\n")
print(arr[5:8].copy())

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("创建一个二维数组\n", arr2d)
print("# 索引二维数组第3行\n", arr2d[2])
print("# 用列表表示位置\n", arr2d[0, 2], "\n# 对比原本的\n", arr2d[0][2]) #等价索引1行3列元素
print("# 索引第1行和第2行（不含第3行）\n", arr2d[:2])
print("# 索引第1列 \n", arr2d[:, :1])
print("# 使用负数索引将从尾部开始选取行\n", arr2d[:-2])
print("# 如果要按某个维度逆序，可以直接在切片第三个参数(步长)填-1\n", arr2d[::-1, :])

print("# 用同一个阵组合分块母阵，注意第二个参数是一个tuple，表示x行y列\n", tile(arr, (6, 1)))


arr = np.arange(15).reshape((3, 5))
print("# 生成顺序数组，后整形为3行5列arr.reshape((3,5))\n# 注意传入的是tuple\n", arr)
print("# 转置数组 arr.T\n", arr.T)
print("# 应用：利用np.dot计算矩阵内积XTX\n", np.dot(arr.T, arr))
arr = np.random.randn(6, 3)
print("# randn函数生成一些正态分布的随机数组（6行3列）\n", arr)