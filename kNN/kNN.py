from numpy import *
import operator
import matplotlib.pyplot as plt


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

group, labels = createDataSet()


def classify(inX, Set, thelabels, num):
    dataSetSize = Set.shape[0]
    # 将矩阵作为分块子阵，创建dataSetSize行，1列的矩阵
    diffMat = tile(inX,(dataSetSize,1)) - Set
    sqDiffMat = diffMat**2
    # 将所有列向量求和
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5

    # 利用argsort()方法得到排序后的下标
    sortedDistIndicies = distances.argsort()

    # 对k个邻居进行投票
    classCount={}
    for i in range(num):
        voteIlabel = thelabels[sortedDistIndicies[i]]
        # 这一步就可以直接利用map.get()中的默认值，创建不存在的key
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename, spilt):
    with open(filename) as fr: # 这里进行了一个替换,使得文件读写更加安全
        arrayOlines=fr.readlines()
        LinesNumber = len(arrayOlines)
        mainMat = zeros((LinesNumber, 3)) # 先初始化一个零数组
        index = 0 # 读取第index行的数据
        clasRecord=[] # 类别记录
        for line in arrayOlines:
            line = line.strip()
            listFromLine = line.split(spilt)
            mainMat[index, :]= listFromLine[0:3] # 对某一行进行读取
            clasRecord.append(int(listFromLine[-1])) # 加入对应的结果
            index += 1
    return mainMat, clasRecord


def mat2gra(mat, result):
    fig = plt.figure()  # 新建一个视图
    ax = fig.add_subplot(111)  ##在视图的中央建立一个子图
    ax.scatter(mat[:, 1], mat[:, 0], 15.0*array(result), 15.0*array(result))
    # ax.axis([-2,25,-0.2,2.0])
    # plt.xlabel('Percentage of Time Spent Playing Video Games')
    # plt.ylabel('Liters of Ice Cream Consumed Per Week')
    plt.show()


def autoNorm(numSet):
    minValues = numSet.min(0)
    maxValues = numSet.max(0)
    ranges = maxValues - minValues
    # normalDataSet = zeros(shape(dataSet))
    m = numSet.shape[0] # shape指的是各个维度的大小
    print(numSet.shape) # 返回一个各个维度的shape的列表
    print(numSet.size) # 返回真-size
    normalDataSet = numSet - tile(minValues, (m, 1))
    normalDataSet = normalDataSet / tile(ranges, (m, 1))
    return normalDataSet, ranges, minValues


returnMat, classLabelVector = file2matrix("datingTestSet2.txt", "\t")
dataSet, ranges1, minValues1 = autoNorm(returnMat)
print(dataSet)
print(ranges1)
print(minValues1)
mat2gra(dataSet, classLabelVector)


def dating_class():
    hoRatio = 0.1
    dataDataMat,datingLabels = file2matrix("datingTestSet2.txt", "\t")
    normal, ranges, minValue = autoNorm(dataDataMat)
    m = normal.shape[0]
    numTestVec = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVec):
        break
        # TODO:to be continue


