import numpy as np
from numpy import *

arr = np.arange(10)
print("# 最开始的数组\n", arr)
print("# 和其他语言的数组访问法一样，arr[5] =", arr[5])    # 索引第6个元素
print("# 可以用 arr[5:8] = 12 令第6到第9个元素等于12")

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

print("##################################################")
print("# 用同一个阵组合分块母阵，注意第二个参数是一个tuple，表示x行y列\n", tile(arr, (6, 1)))
arr2d = np.arange(15).reshape((3, 5))
print("# 生成顺序数组，后整形为3行5列 \n# arr.reshape((3,5))\n# 注意传入的是tuple\n", arr2d)
print("# 转置数组 arr.T\n", arr2d.T)
print("# 应用：利用np.dot计算矩阵内积XTX\n", np.dot(arr2d.T, arr2d))
arr2d = np.random.randn(6, 3)
print("# randn函数生成一些正态分布的随机数组（6行3列）\n", arr2d)

print("###################################################")
print("# 直接sort()的话会导致原数组丢失")
arr.sort()
print("# 一维数组排序需要sort()\n", arr)

arr2dcopy = arr2d.copy()
arr2d.sort(0)
print("# 二维数组排序需要指定轴(0为行，１为列)(该轴数据会被拆散)\n", arr2d)
print("# 也可以返回排序后的坐标(垂直的轴不变，另一个轴是坐标)，方便保持原数组并且获得排序后结果\n", arr2dcopy.argsort(0))
print("# 有一个唯一排序，也不是在原数组上操作，会返回一个不重复的排序好的数组")
arraytosort = array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print("# 对", arraytosort, "unique()排序\n", unique(arraytosort))

print("########################################################")
print("# 最后是用于数组的文件输入输出")

print("# 可以通过save(路径名,数组名)来保存数组(.npy),load\n# 并通过np.load(文件名)读取磁盘上的数组")
np.save('.\\someArray', arr)
np.load('.\\someArray.npy')
print("# 也可以用savez()将多个数组以保存在一个压缩文件中")
np.savez('.\\array_archive.npz', a=arr, b=arr)
a = np.arange(0, 12, 0.5).reshape(4, -1)

print("# 要保存为txt的话有几点需要注意，savetxt()，loadtxt()和上面参数可以一样，但是缺省按照’%.18e’格式保存数据，以空格分隔")
np.savetxt('.\\a.txt', a)
print(np.loadtxt('.\\a.txt'))
print("# fmt改为保存为整数，delimiter改分隔符")
np.savetxt('.\\a.txt', a, fmt="%d", delimiter=",")
print("# 读取的时候也要记得指定delimiter")
print(np.loadtxt('.\\a.txt', delimiter=","))
