#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import data
import RecordUserOperation
import AutomaticCorrectData


# 检查数据集中的丢失数据
def check_missing_data(path):
    # 读取数据
    myData = data.DataOperation(path)
    rows = myData.get_row_quantity()  # 获取行数
    columns = myData.get_column_quantity()  # 获取列数

    df_missing_data = myData.get_data().isnull()  # 返回一个与myData行列相同的数据集，每个单元的True/False代表着该位置是否为缺失值

    for row in range(0, rows):
        for column in range(0, columns):
            if df_missing_data.iloc[row, column]:
                # 判断是否可以自动改正缺失值点
                confidence = AutomaticCorrectData.predict_operation_result(1, 0, column, row, myData)
                if confidence:
                    print("Missing data has been solved")
                if not confidence:
                    report_missing_data(myData, row, column)

    print("\nNo more missing data\n")


# 报告丢失数据信息
def report_missing_data(myData, row, column):
    print("\nMissing \"" + myData.get_column_name()[column] + "\" value in row:")
    print(myData.get_row(row + 1))
    MissingOperation = menu_repair_missing_data()

    if MissingOperation == "1":
        delete_missing_data(myData, row)
        # 记录用户操作
        RecordUserOperation.GetUserClassifyOperation(0, 0, column, row, 0)

    elif MissingOperation == "2":
        value = repair_missing_data(myData, row, column)
        # 记录用户操作
        RecordUserOperation.GetUserClassifyOperation(0, 0, column, row, 1)
        # 记录用户修复的数据值
        RecordUserOperation.GetUserRepairValue(0, 0, column, row, value)

    elif MissingOperation == "3":
        # 记录用户操作
        RecordUserOperation.GetUserClassifyOperation(0, 0, column, row, 2)

    else:
        print("invalid operation")


# 丢失数据修复选项菜单
def menu_repair_missing_data():
    print("\nwhich operation do you prefer to solve the missing data?")
    print("1. delete the row which includes the missing data")
    print("2. Assign a value for the missing data")
    print("3. Ignore and mark that this cell should be empty")
    MissingOperation = input()
    return MissingOperation


# 修复丢失数据
def repair_missing_data(myData, row, column):
    value = input("input the value to replace the empty unit: ")
    myData.change_cell(row, column, value)
    return value


# 删除丢失数据所在行
def delete_missing_data(myData, row):
    myData.delete_row(row)
