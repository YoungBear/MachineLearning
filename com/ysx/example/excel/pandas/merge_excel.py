#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd
import os

# 将n个excel文件数据合并到一个excel


# 读取n个excel文件数据，并且合并到一个二维数组，每个excel只读取A列，且行数保持一样
def merge(n):
    data = []
    for i in range(n):
        data_file_path = os.path.join('data', f'data{i + 1}.xlsx')
        df = pd.read_excel(data_file_path, index_col=None, header=None, sheet_name='Sheet1')
        # 仅获取第0列数据
        data.append(df.values[:, 0])

    # print(data)
    # 转置
    transpose_data = list(map(list, zip(*data)))
    # print(transpose_data)
    merge_file_path = os.path.join('data', 'merge.xlsx')
    save(transpose_data, merge_file_path)


# 将二维数据数据保存到excel文件
def save(data, file_path):
    df = pd.DataFrame(data)
    # 写入本地excel文件
    df.to_excel(file_path, sheet_name="Sheet1", index=False, header=False)


# main函数
if __name__ == '__main__':
    merge(10)
