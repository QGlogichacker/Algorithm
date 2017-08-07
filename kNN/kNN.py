from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

group,labels = createDataSet()

def classify(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    ##将矩阵作为分块子阵，创建dataSetSize行，1列的矩阵
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    ##将所有列向量求和
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5

    ##利用argsort()方法得到排序后的下标
    sortedDistIndicies = distances.argsort()

    ##对k个邻居进行投票
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        ##这一步就可以直接利用map.get()中的默认值，创建不存在的key
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename,spilt):
    with open(filename) as fr:##这里进行了一个替换,使得文件读写更加安全
        arrayOlines=fr.readlines()
        LinesNumber = len(arrayOlines)
        returnMat = zeros((LinesNumber,3)) ##先初始化一个零数组
        index = 0 ##读取第index行的数据
        classLabelVector=[] ##类别记录
        for line in arrayOlines:
            line = line.strip()
            listFromLine = line.split(spilt)
            returnMat[index,:]=listFromLine[0:3] ##对某一行进行读取
            classLabelVector.append(int(listFromLine[-1])) ##加入对应的结果
            index += 1
    return returnMat,classLabelVector

returnMat,classLabelVector = file2matrix("datingTestSet2.txt","\t")
print(returnMat)
print(classLabelVector)

import matplotlib
import matplotlib.pyplot as plt
def mat2gra(mat,result):
    fig = plt.figure()  ##新建一个视图
    ax = fig.add_subplot(111)  ##在视图的中央建立一个子图
    ax.scatter(mat[:,1], mat[:,0], 15.0*array(result), 15.0*array(result))
    ##ax.axis([-2,25,-0.2,2.0])
    ##plt.xlabel('Percentage of Time Spent Playing Video Games')
    ##plt.ylabel('Liters of Ice Cream Consumed Per Week')
    plt.show()

def autoNorm(dataSet):
    minValues = dataSet.min(0)
    maxValues = dataSet.max(0)
    ranges = maxValues - minValues
    ##normalDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normalDataSet = dataSet - tile(minValues,(m,1))
    normalDataSet = normalDataSet/tile(ranges,(m,1))
    return normalDataSet , ranges , minValues

dataSet,ranges,minValues = autoNorm(returnMat)

print(dataSet)
print(ranges)
print(minValues)

def datingClass():
    hoRatio = 0.1
    dataDataMat,datingLabels = file2matrix("datingTestSet2.txt","\t")
    normal , ranges ,minValue =autoNorm(dataDataMat)
    m = normal.shape[0]
    numTestVec = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVec):
        break
        ##TODO:to be continue

##mat2gra(*file2matrix("datingTestSet2.txt","\t"))