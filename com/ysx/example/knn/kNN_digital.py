#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2017/12/29 19:02
# @Author  : bearyang
# @Site    : 
# @File    : kNN_digital.py
# @Software: PyCharm

from numpy import *
import os
import kNN


def img2vector(filename):
    """
    将一个32*32的二进制矩阵转换为1*1024的向量
    这样就可以使用前两节的分类器来处理数字图像信息了
    :param filename:
    :return:
    """
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect


def handwritingClassTest():
    """
    手写数字识别系统的测试代码
    :return:
    """
    hwLabels = []
    trainingFileList = os.listdir('trainingDigits')  # 返回文件列表
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = os.listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = kNN.classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("the classifier came back with: %d, the real answer is %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr):
            errorCount += 1.0
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount / float(mTest)))


handwritingClassTest()
# testVector = img2vector("testDigits/0_13.txt")
# print(testVector[0,0:31])
# print(testVector[0,32:63])
