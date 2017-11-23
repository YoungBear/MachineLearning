# -*- coding: utf-8 -*-
__author__ = 'Wsine'

import numpy as np
import matplotlib.pyplot as plt
import math
import time

from geopy.distance import great_circle

UNCLASSIFIED = False
NOISE = 0


def circle_dis(a, b):
    """
    计算两个点之间的球面距离
    :param a: 坐标a(34.32664,108.9493)
    :param b: 坐标b(34.26104,108.9682)
    :return:
    """
    return great_circle(a, b).meters


def loadDataSet(fileName, splitChar='\t'):
    """
    输入：文件名
    输出：数据集
    描述：从文件读入数据集
    """
    print("loadDataSet...")
    dataSet = []
    with open(fileName) as fr:
        for line in fr.readlines():
            # 将每一行的数据分成坐标类型 ['15.55', '28.65']
            curline = line.strip().split(splitChar)
            # 将字符串转换成float，即真正的坐标 [15.55, 28.65]
            fltline = list(map(float, curline))
            # 添加到数据列表
            dataSet.append(fltline)
    return dataSet


def dist(a, b):
    """
    :param a:向量A
    :param b:向量B
    :return:两个向量的欧式距离
    """
    return math.sqrt(np.power(a - b, 2).sum())


def eps_neighbor(a, b, eps):
    """
    :param a:向量A
    :param b:向量B
    :param eps:半径
    :return:是否在eps范围内
    """
    # return dist(a, b) < eps
    pointA = (a[0, 0], a[1, 0])
    pointB = (b[0, 0], b[1, 0])
    return circle_dis(pointA, pointB) < eps


def region_query(data, pointId, eps):
    """
    :param data:数据集
    :param pointId:查询点id
    :param eps:半径大小
    :return:在eps范围内的点的id
    """
    nPoints = data.shape[1]
    seeds = []
    for i in range(nPoints):
        # 　判断两点的距离是否在查询点pointId的范围之内，如果在则将其添加到列表里
        if eps_neighbor(data[:, pointId], data[:, i], eps):
            seeds.append(i)
    return seeds


def expand_cluster(data, clusterResult, pointId, clusterId, eps, minPts):
    """
    :param data: 数据集
    :param clusterResult: 分类结果
    :param pointId: 待分类点id
    :param clusterId: 簇id
    :param eps: 半径大小
    :param minPts:最小点个数
    :return:能否成功分类
    """
    print("expand_cluster, pointId: {}".format(pointId))
    # 获取pointId的E邻域的所有点
    seeds = region_query(data, pointId, eps)
    if len(seeds) < minPts:  # 不满足minPts条件的为噪声点
        clusterResult[pointId] = NOISE
        return False
    else:
        clusterResult[pointId] = clusterId  # 划分到该簇
        for seedId in seeds:
            clusterResult[seedId] = clusterId

        while len(seeds) > 0:  # 持续扩张
            currentPoint = seeds[0]
            queryResults = region_query(data, currentPoint, eps)
            if len(queryResults) >= minPts:
                for i in range(len(queryResults)):
                    resultPoint = queryResults[i]
                    if clusterResult[resultPoint] == UNCLASSIFIED:
                        seeds.append(resultPoint)
                        clusterResult[resultPoint] = clusterId
                    elif clusterResult[resultPoint] == NOISE:
                        clusterResult[resultPoint] = clusterId
            seeds = seeds[1:]
        return True


def dbscan(data, eps, minPts):
    """
    输入：数据集, 半径大小, 最小点个数
    输出：分类簇id
    """
    clusterId = 1
    # 得到矩阵的列数，即得到一共有多少个点
    nPoints = data.shape[1]
    # 生成长度为n的布尔列表，值都为False
    clusterResult = [UNCLASSIFIED] * nPoints
    for pointId in range(nPoints):
        # 取出一个点，用矩阵表示
        # point = data[:, pointId]
        if clusterResult[pointId] == UNCLASSIFIED:
            if expand_cluster(data, clusterResult, pointId, clusterId, eps, minPts):
                clusterId = clusterId + 1
    return clusterResult, clusterId - 1


def plotFeature(data, clusters, clusterNum):
    print("plotFeature...")
    nPoints = data.shape[1]
    matClusters = np.mat(clusters).transpose()
    fig = plt.figure()
    scatterColors = ['black', 'blue', 'green', 'yellow', 'red', 'purple', 'orange', 'brown']
    ax = fig.add_subplot(111)
    for i in range(clusterNum + 1):
        colorSytle = scatterColors[i % len(scatterColors)]
        subCluster = data[:, np.nonzero(matClusters[:, 0].A == i)]
        ax.scatter(subCluster[0, :].flatten().A[0], subCluster[1, :].flatten().A[0], c=colorSytle, s=50)


def main():
    dataSet = loadDataSet('xian_2k.csv', splitChar=',')
    # 将数据列表转换成矩阵，并且转置。得到一个2*n(即2行788列)的矩阵
    dataSet = np.mat(dataSet).transpose()
    # print(dataSet)
    Eps = 10000
    MinPts = 100
    clusters, clusterNum = dbscan(dataSet, Eps, MinPts)
    print("cluster Numbers = ", clusterNum)
    # print(clusters)
    plotFeature(dataSet, clusters, clusterNum)


if __name__ == '__main__':
    start = time.clock()
    main()
    end = time.clock()
    print('finish all in %s' % str(end - start))
    plt.show()
