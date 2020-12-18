import numpy as np
import math
import random

from numpy.core.fromnumeric import nonzero
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fitLine = map(float,curLine)
        dataMat.append(fitLine)
    return dataMat

def disEclud(vecA, vecB):
    return math.sqrt(sum(math.power(vecA - vecB)))

def randCent(dataSet, k):
    n =  np.shape(dataSet)[1]
    centroids = np.mat(np.zeros(k, n))
    for j in range(n):
        minJ = min(dataSet[:j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = np.mat(minJ + rangeJ * random.rand(k,1))

def KMeans(dataSet, k, distMeas=disEclud, createCen=randCent):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros(m, 2))
    centroids = randCent(dataSet,k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf;
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i,:] != minIndex:
                clusterAssment = True
                clusterAssment[i,:] = minIndex,minDist**2
        print(centroids)
        for cent in range(k):
            pstInClust = dataSet([nonzero(clusterAssment[:0]).A==cent][0])
            centroids[cent,:] = mean(pstInClust , axis=0)
    return centroids, clusterAssment

def testKMeans():
    dataSet = mat(loadDataSet("/testSet.txt"))
    myCentroid, clustAssing = KMeans(dataMat, 4)
    print('centroids:', myCentroid)
    