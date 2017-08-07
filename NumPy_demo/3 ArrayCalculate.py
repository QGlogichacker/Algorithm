import numpy as np
from numpy import *

print('''
#######################################
# 用数组表达式代替循环的做法，通常称为矢量化 #
#######################################
# 首先是array的情况
# 简单的标量运算
''')
arr = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]], dtype=int)    # 创建二维数组
print("元素乘arr*arr\n", arr*arr)   # 行列号相同的数组元素间运算
print("元素减arr-arr\n", arr-arr)
print("元素倒数1/arr\n", 1/arr)
print("常数乘法arr*0.5\n", arr*0.5)
print("# 计算各元素的平方根sqrt(arr)\n也可以用（arr**0.5）\n", np.sqrt(arr))
print("# 计算各元素指数exp(arr);  \nabs  #绝对值;\n", exp(arr))
print("add(arr,arr) #两数组中对应元素相加;  \nsubtract # 相减;  \nmultiply # 相乘;  \ndivide # 相除;", np.add(arr, arr))

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

print("注意diag已经不在lin里了diag(arr)\n", diag(arr))
print("矩阵相乘 arr.dot(arr)\n", arr.dot(arr))
print("求行列式 det(arr)\n", lin.det(arr))
arr = np.random.randn(3, 3)
print("# 求逆inv(arr)(行列式为0会报错)\n", lin.inv(arr))

print("# 然后是matrix的情况（可以通过Mat(array)函数得到，是array的子集，具有其所有特性")

