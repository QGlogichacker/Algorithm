from numpy import *
import numpy as np


def loadDataSet(fileName):
    dataMat = []
    with open(fileName) as fr:
        for line in fr.readlines():
            curLine = line.strip().split('\t')
            # 斗胆将map变为tmd array
            fltLine = array(curLine, float)
            dataMat.append(fltLine)
    return dataMat


def binSplitDataSet(dataMat, feature, value):
    mat0 = dataMat[nonzero(dataMat[:, feature] > value)[0], :]#[0]
    # print(nonzero(dataMat[:, feature] <= value))
    # print(nonzero(dataMat[:, feature] <= value)[0])
    # print(dataMat[nonzero(dataMat[:, feature] <= value)[0], :])
    # print(dataMat[nonzero(dataMat[:, feature] <= value)[0], :][0])
    mat1 = dataMat[nonzero(dataMat[:, feature] <= value)[0], :]#[0]
    # mat0 = []
    # mat1 = []
    # print((nonzero(dataSet[:, feature] > value))[0])
    # for index in (nonzero(dataSet[:, feature] > value))[0]:
    #     mat0.append(dataSet[index, :][0])
    # for index1 in (nonzero(dataSet[:, feature] <= value))[0]:
    #     mat1.append(dataSet[index1, :][0])
    return mat0, mat1


# 回归树的叶子节点
def regLeaf(data):
   return mean(data[:, -1])


# 回归树的求解方式
def regError(data):
    # print(var(data[:, -1]))
    # print(shape(data))
    return var(data[:, -1])*shape(data)[0]


def createTree(data, leafType=regLeaf, errType=regError, ops=(1, 4)):
    feat, model = chooseBestSplit(data, leafType, errType, ops)
    if feat is None:
        return model
    retTree = {}
    retTree['spInd'] = feat
    retTree['spVal'] = model
    lSet, rSet = binSplitDataSet(data, feat, model)
    retTree['left'] = createTree(lSet, leafType, errType, ops=ops)
    retTree['right'] = createTree(rSet, leafType, errType, ops=ops)
    return retTree


def chooseBestSplit(data, leafType=regLeaf, errorType=regError, ops=(1, 4)):
    tolS = ops[0]
    tolN = ops[1]
    # 如果数据集已经只有一种结果，返回叶子节点
    # if len(set(data[:, -1].T.tolist()[0])) == 1:
    if len(set(data[:, -1].T)) == 1:
        return None, leafType(data)
    m, n = shape(data)
    S = errorType(data)
    bestS = inf
    bestIndex = 0
    bestValue = 0
    for featIndex in range(n-1):
        for splitVal in set(data[:, featIndex]):
            mat0, mat1 = binSplitDataSet(data, featIndex, splitVal)
            if (shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN):
                continue
            newS = errorType(mat0) + errorType(mat1)
            if newS < bestS:
                bestIndex = featIndex
                bestValue = splitVal
                bestS = newS
    # 至此，循环结束，找到了最佳的分割点和最佳的取值点
    # 若成效不是很大，就进行剪枝
    if (S - bestS) < tolS:
        return None, leafType(data)
    mat0, mat1 = binSplitDataSet(data, bestIndex, bestValue)
    # 若切分出的数据集很小，就剪枝
    if shape(mat0)[0] < tolN or shape(mat1)[0] < tolN:
        return None, leafType(data)
    # 否则正常输出
    return bestIndex, bestValue


# dataSet = loadDataSet("./ex2.txt")
# print(dataSet)
# a = binSplitDataSet(eye(4), 1, 0.5)
#
#
# myDat = loadDataSet("ex2.txt")
# # 改mat为array
# myMat = array(myDat, float)
# tree = createTree(myMat)
# print(tree)


def isTree(obj):
    return type(obj).__name__ == 'dict'


def getMean(tree):
    if isTree(tree['left']):
        tree['left'] = getMean(tree['left'])
    if isTree(tree['right']):
        tree['right'] = getMean(tree['right'])
    return (tree['left']+tree['right'])/2.0


def regPrune(tree, testData):
    if shape(testData)[0] == 0:
        print("塌陷！")
        return getMean(tree)
    lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])
    # 还有子节点就向下递归
    # if isTree(tree['left']) or isTree(tree['right']):
    if isTree(tree['left']):
        tree['left'] = regPrune(tree['left'], lSet)
    if isTree(tree['right']):
        tree['right'] = regPrune(tree['right'], rSet)
    # 左右都是子节点的时候，
    if not isTree(tree['left']) and not isTree(tree['right']):
        errorNoMerge = sum(power(lSet[:, -1]-tree['left'], 2)) + sum(power(rSet[:, -1]-tree['right'], 2))
        treeMean = (tree['left']+tree['right'])/2.0
        errorMerge = sum(power(testData[:, -1]-treeMean, 2))
        if errorMerge < errorNoMerge:
            print("merging")
            return treeMean
        else:
            return tree
    else:
        return tree # miaomiaomiao?


def linearSolve(data):
    # m, n = data.shape
    # X = mat(ones((m, n-1)))
    # # Y = mat(ones((m, 1)))
    # Y = mat(data[:, -1])
    # X[:, 0:n] = data[:, 0:n-1]
    # # for i in range(0,n):
    # #     x[:, i+1] = data[:, i]
    # xTx = X.T * X
    # if np.linalg.det(xTx) == 0.0:
    #     raise NameError("singular")
    # ws = xTx.I*(X.T*Y)
    # return ws, X, Y
    m, n = shape(data)
    X = mat(ones((m, n)))
    X[:, 1:n] = data[:, 0:n-1]
    Y = mat(data[:, -1]).T #and strip out Y
    xTx = X.T*X
    if linalg.det(xTx) == 0.0:
        raise NameError('This matrix is singular, cannot do inverse,\n\
        try increasing the second value of ops')
    d = np.linalg.inv(xTx) * mat(X.T)
    ws = d * Y
    # ws = np.linalg.inv(Y)
    return ws, X, Y


def modelLeaf(data):
    ws, X, Y = linearSolve(data)
    return ws


def modelError(data):
    ws, X, Y = linearSolve(data)
    yHat = X * ws
    return sum(power(Y-yHat, 2))


# data = array(loadDataSet("exp2.txt"), float)
# tree = createTree(data, leafType=modelLeaf, errType=modelError, ops=(1, 10))
# print(tree)


def regTreeEval(model, inDat):
    return float(model)


def modelTreeval(model, inDat):
    n = shape(inDat)[1]
    X = mat(ones((1,n+1)))
    X[:,1:n+1] = inDat
    # 获得设计矩阵
    return float(X*model)


def treeForeCast(tree, inData, modelEval=regTreeEval):
    if not isTree(tree):
        return modelEval(tree, inData)
    if inData[tree['spInd']] > tree['spVal']:
        if isTree(tree['left']):
            return treeForeCast(tree['left'], inData, modelEval)
        else:
            return modelEval(tree['left'], inData)
    else:
        if isTree(tree['right']):
            return treeForeCast(tree['right'], inData, modelEval)
        else:
            return modelEval(tree['right'], inData)


def createForeCast(tree, testData, modelEval=regTreeEval):
    m = len(testData)
    yHat = mat(zeros((m,1)))
    for i in range(m):
        yHat[i,0] = treeForeCast(tree, mat(testData[i]), modelEval)
    return yHat


trainMat = array(loadDataSet('bikeSpeedVsIq_train.txt'))
testMat = array(loadDataSet('bikeSpeedVsIq_test.txt'))
myTree = createTree(trainMat, ops=(1, 20))
yHat = createForeCast(myTree, testMat[:, 0])
print(corrcoef(yHat, testMat[:, 1], rowvar=False)[0, 1])
