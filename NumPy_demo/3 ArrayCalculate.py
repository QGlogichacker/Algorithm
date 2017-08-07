import numpy as np
from numpy import *

# 首先是array的情况
# 首先是简单的标量运算
arr = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])    # 创建二维数组
print(arr*arr)   # 行列号相同的数组元素间运算
print(arr-arr)
print(1/arr)
print(arr*0.5)

print('''
# 然后是线性代数运算
# diag    以一维数组的形式返回方阵的对角线元素
# dot     矩阵乘法
# trace   计算对角线元素的和
# det     计算矩阵行列式
# eig     计算方阵的本征值和本征向量
# inv     计算方阵的逆
# pinv    计算矩阵的Moore-Penrose伪逆
# qr      计算qr分解
# svd     计算奇异值分解
# solve   解线性方程组Ax=b，其中A为一个方阵
# lstsq   计算Ax=b的最小二乘解
''')

import numpy.linalg as lin

print("注意diag已经不在lin里了\n",diag(arr))
print("矩阵相乘\n", arr.dot(arr))
print("求行列式",lin.det(arr))
# print(lin.inv(arr)) 求逆(行列式为0会报错)

# 然后是matrix的情况（可以通过Mat(array)函数得到，是array的子集，具有其所有特性）

