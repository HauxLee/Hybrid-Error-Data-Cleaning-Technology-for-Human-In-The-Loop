#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pandas as pd

pd.set_option('display.width', None)  # 使输出无省略号无换行


class DataOperation:
    def __init__(self, path):
        self.path = path  # 文件路径
        self.df = pd.read_csv(path)  # 读取数据

    # 获取数据集
    def get_data(self):
        return self.df

    # 获取数据集的行数
    def get_row_quantity(self):
        return self.df.shape[0]

    # 获取数据集的列数
    def get_column_quantity(self):
        return self.df.shape[1]

    # 获取数据集的某一行
    def get_row(self, row_number):
        return self.df[row_number - 1: row_number]

    # 获取列名
    def get_column_name(self):
        return self.df.columns

    # 获取数据集的某一列
    def get_column(self, column_name):
        return self.df[column_name]

    # 删除数据集的某一行
    def delete_row(self, row_number):
        updated_dataset = self.df
        updated_dataset.drop(self.df.index[row_number: row_number + 1]).to_csv("TestDataSet/updated_data.csv")

    # 改变数据集的某一单元格的数据
    def change_cell(self, row_number, column_number, value):
        updated_dataset = self.df
        updated_dataset.iloc[row_number, column_number] = value
        updated_dataset.to_csv("TestDataSet/updated_data.csv")

    # 根据列名获取第几列
    def get_columnNumber_by_columnName(self, column_name):
        return self.df.columns.get_loc(column_name)
