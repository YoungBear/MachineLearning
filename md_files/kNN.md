# k-近邻算法

kNN: k Nearest Neighbor

## k-近邻算法的一般流程

1. 收集数据：可以使用任何方法。
2. 准备数据：距离计算所需要的数值，最好是结构化的数据格式。
3. 分析数据：可以使用任何方法。
4. 训练方法：此步骤不适用与k-近邻算法。
5. 测试算法：计算错误率。
6. 使用算法：首先需要输入样本数据和结构化的输出结果，然后运行k-近邻算法判定输入数据分别属于哪个分类，最后应用对计算出的分类执行后续的处理。

## 实施kNN分类算法

对未知类别属性的数据集中的每个点依次执行以下操作：

1. 计算已知类别数据集中的点与当前点之间的距离；
2. 按照距离递增次序排序；
3. 选取与当前点距离最小的k个点；
4. 确定前k个点所在类别的出现频率；
5. 返回前k个点出现频率最高的类别作为当前点的预测分类。

k-近邻算法

```
def classify0(inX, dataSet, labels, k):
    """
    :param inX: 分类的输入向量
    :param dataSet: 训练样本集
    :param labels: 标签向量
    :param k: 选择最近邻居的数目
    :return:
    """
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
```

## 手写识别系统

使用k-近邻算法的手写识别系统：

1. 收集数据：提供文本文件。
2. 准备数据：编写函数img2vector(),将图像格式转换为分配器使用的向量格式。
3. 分析数据：在Python命令提示符中检查数据，确保它符合要求。
4. 训练算法：此步骤不适用于k-近邻算法。
5. 测试算法：编写函数使用提供的部分数据集作为测试样本，测试样本与非测试样本的区别在于测试样本是已经完成分类的数据，如果预测分类与实际类别不同，则标记为一个错误。
6. 使用算法：本例没有完成此步骤，若你感兴趣可以构建完整的应用程序，从图像中提取数据，并完成数字识别，美国的邮件分拣系统就是一个实际运行的类似系统。

