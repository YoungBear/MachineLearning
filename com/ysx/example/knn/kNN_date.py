#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2017/12/28 18:09
# @Author  : bearyang
# @Site    : 
# @File    : kNN_date.py
# @Software: PyCharm

from numpy import *
import matplotlib
import matplotlib.pyplot as plt


def file2matrix(filename):
    """
    将文本记录转换为NumPy的解析程序
    :param filename: 文件名
    :return:
    """
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)  # 得到文件行数
    returnMat = zeros((numberOfLines, 3))  # 生成0矩阵
    classLabelVector = []
    index = 0
    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')

# print(datingDataMat)
print(datingLabels[0:20])
fig = plt.figure()
ax = fig.add_subplot(111)
# 取datingDataMat的第1列数据和第2列的数据(从第0列开始)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
plt.show()
