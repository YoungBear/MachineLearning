import os
import openpyxl
# 将n个excel文件数据合并到一个excel


# 读取n个excel文件数据，并且合并到一个二维数组，每个excel只读取A列，且行数保持一样
def merge(n):
    data = []
    for i in range(n):
        data_file_path = os.path.join('data', f'data{i + 1}.xlsx')
        # 返回一个workbook数据类型的值
        workbook = openpyxl.load_workbook(data_file_path)
        sheet = workbook.active
        # 取A列数据
        cell = sheet['A']
        column = []
        for j in cell:
            column.append(j.value)
        data.append(column)

    # print(data)
    # 转置
    transpose_data = list(map(list, zip(*data)))
    # print(transpose_data)
    merge_file_path = os.path.join('data', 'merge.xlsx')
    save(transpose_data, merge_file_path)


# 将二维数据数据保存到excel文件
def save(data, file_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Sheet1'
    workbook.save(file_path)

    for row in data:
        sheet.append(row)
    workbook.save(file_path)


# main函数
if __name__ == '__main__':
    merge(10)
