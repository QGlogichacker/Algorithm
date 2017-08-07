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
print("# 元素乘arr*arr\n", arr*arr)   # 行列号相同的数组元素间运算
print("# 元素减arr-arr\n", arr-arr)
print("# 元素倒数1/arr\n", 1/arr)
print("常数乘法arr*0.5\n", arr*0.5)
print("# 计算各元素的平方根sqrt(arr)\n也可以用（arr**0.5）\n", np.sqrt(arr))
print("# 计算各元素指数exp(arr);  \nabs  #绝对值;\n", exp(arr))
print("add(arr,arr) #两数组中对应元素相加;  \nsubtract # 相减;  \nmultiply # 相乘;  \ndivide # 相除;\n", np.add(arr, arr))

print("# 维度约归也是一种常用的矢量化方法")
print('''
# 通过数组上的一组数学函数对整个数组或某个轴向的数据进行统计计算。
# sum、mean以及标准差std等聚合计算
# 既可以当做数组的实例方法调用，也可以当做顶级NumPy函数使用：
''')

arr2 = np.eye(3)+np.ones((3, 3))
arr2[2, 1] = 0
print("##################################################################")
print("求和和平均")
print("mean()方法是默认求所有元素的平均值", arr2.mean())
print("sum()方法默认求返回对应轴的和的list\n", arr2.sum())
print("# axis参数是轴的标号，sum()计算该轴上的统计值（0为列，1为行）\n", arr2.sum(axis=1))
print('# 也可以对mean()使用', arr2.mean(axis=1))

print('''
#################################################################
# 还可以将条件逻辑表述为数组运算
# bools = (arr>0) 即可构造一个布尔数表
# bools.any()    #用于测试数组中是否存在一个或多个True  
# bools.all()    #用于测试数组中所有值是否都是True  
''')

bools = (arr>0)
print("打印arr>0\n", bools)
print("any()?:",  bools.any())
print("all()?:", bools.all())

print("# Numpy.where函数是三元表达式x if condition else y的矢量化版本")
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])    # 两个数值数组
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])    # 一个布尔数组
result = np.where(cond, xarr, yarr)    # 三元表达式
print("两个数组，一个布尔数组即可组成 np.where(cond, xarr, yarr)\n", result)

print('''
#################################################################
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
print("# 求逆 inv(arr)(行列式为0会报错)\n", lin.inv(arr))

print("#################################################")
print("# 最后是matrix的情况（可以通过Mat(array)函数得到，是array的子集，具有其所有特性")
print("# 但是有许多便利的特性\n详情请看：http://blog.csdn.net/vincentlipan/article/details/20717163")

am = array([1.5,  2.5])
print("# 最后是一个特别神奇的操作\n", am)
print("# am[:, np.newaxis]\n", am[:, np.newaxis])
