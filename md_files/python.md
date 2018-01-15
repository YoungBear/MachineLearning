# Python笔记

## 列表：list，使用中括号[]
## 元组：tuple，使用小括号()。tuple一旦初始化，就不能再改变。
注意，元组只有一个元素时，定义时后边需要加一个逗号","，为了消除一个元素的歧义。
eg. `t= (1,)`

## list方法，将元组转换成一个列表。

## with 相当于文件的try ... finally...

```
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
```

使用with

```
with open('/path/to/file', 'r') as f:
    print(f.read())
```

## python基础

```
list * n # 生成一个列表，将参数列表的值复制n份
range(n) # 生成一个序列，从0到n-1，用于循环。
```

### 字符串相关函数

[参考 Python官方文档 str](https://docs.python.org/3/library/stdtypes.html?#text-sequence-type-str)

[参考 菜鸟教程 Python3 字符串](http://www.runoob.com/python3/python3-string.html)

```
len(str) # 返回字符串长度

str.lstrip([chars]) # 删除 str 字符串左边的指定字符（默认为空格），返回新的字符串
str.rstrip([chars]) # 删除 str 字符串末尾的指定字符（默认为空格），返回新的字符串
str.strip([chars]) # 删除 str 字符串头尾指定的字符（默认为空格），返回新的字符串

# 通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
str.split(str="", num=string.count(str)).
```

### Python3 OS 文件/目录方法

```
os.listdir(path) # 用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。
只支持在 Unix, Windows 下使用。
```

## numpy api

`from numpy import *`

```
mat(list) # 将一个list转换成一个矩阵
tile(A, reps) # 简单理解是此函数将A进行重复输出reps次
```


### 矩阵操作

```
matrix.tolist() # 将一个矩阵转换成一个list
matrix.transpose() # 矩阵转置
matrix.shape[1] # 矩阵第一维的长度，即矩阵的列数
matrix.shape[0] # 矩阵第二维的长度，即矩阵的行数
matrix.shape # 以元组的方式返回矩阵的行和列，即(m,n): m行n列
matrix[i,j] # 返回矩阵[i,j]位置上的元素，即第i行，第j列的元素，i和j从0开始。
matrix[i,:] # 取出第i行所有的元素，也是一个矩阵，1*n，1行n列的矩阵。
matrix[:,j] # 取出第j列所有的元素，也是一个矩阵，m*1，m行1列的矩阵。

matrix.sum() # 矩阵中所有的元素相加，得到一个整数
matrix.sum(axis=0) # 将一个矩阵的每一个列向量相加，得到一个行向量
matrix.sum(axis=1) # 将一个矩阵的每一个行向量相加，得到一个列向量
matrix.argsort() # 返回的是数组值从小到大的索引值

zeros() # 生成0矩阵，默认类型是float. eg. zeros((2,3)) 生成2行3列的矩阵，值都为0
```

## python 安装matplotlib:
http://matplotlib.org/users/installing.html

```
python -mpip install -U pip
python -mpip install -U matplotlib
```


## 文本操作

### 拷贝前n行的数据：

将文件latlng.csv中从第1行到第10000行的数据，拷贝到文件latlng_1.csv

```
sed -n '1,10000p' latlng.csv > latlng_1.csv
```
