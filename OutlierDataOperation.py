#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import data
import numpy as np
import RecordUserOperation
import AutomaticCorrectData


# 检查数据集某一列的离群点
def check_outlier_data(path):
    # 读取数据
    myData = data.DataOperation(path)
    rows = myData.get_row_quantity()  # 获取行数
    columns = myData.get_column_quantity()  # 获取列数

    # 以列为单位检查离群点
    while True:
        # 获取列名
        print(myData.get_column_name())
        check_column_name = input("which column will be checked? : ")

        # 使用箱线图检查离群点
        box_plot(myData, rows, check_column_name)

        # 询问是否检查其他列的离群点
        continue_check = input("check outliers in other columns? [Y/N]: ")
        if continue_check == "N":
            break


# 使用箱线图检查离群点
def box_plot(myData, rows, check_column_name):
    # 获取待检查列的数据
    check_column = myData.get_column(check_column_name)

    #  获取离群值所在列数
    column = myData.get_columnNumber_by_columnName(check_column_name)

    # 获取箱体图特征
    percentile = np.percentile(check_column, (25, 50, 75), interpolation='linear')
    # 以下为箱线图的五个特征值
    Q1 = percentile[0]  # 上四分位数
    Q2 = percentile[1]  # 中位数
    Q3 = percentile[2]  # 下四分位数
    IQR = Q3 - Q1  # 四分位距
    ulim = Q3 + 1.5 * IQR  # 上限 非异常范围内的最大值
    llim = Q1 - 1.5 * IQR  # 下限 非异常范围内的最小值
    if llim < 0:
        llim = 0

    # 检查离群点
    for row in range(0, rows):
        # print(check_column.iloc[row])  #test
        if check_column.iloc[row] < llim or check_column.iloc[row] > ulim:
            # 判断是否可以自动改正离群点
            confidence = AutomaticCorrectData.predict_operation_result(2, check_column.iloc[row], column, row, myData)
            if confidence:
                print("Outlier data has been solved ")
            if not confidence:
                # 报告离群点
                report_outlier_data(myData, row, check_column_name, check_column.iloc[row])

    print("no more outliers in this column")


# 向用户报告离群点，等待用户选择操作
def report_outlier_data(myData, row, check_column_name, AbnormalValue):
    # 获取待检查列的数据
    check_column = myData.get_column(check_column_name)

    print("\n\"" + str(check_column.iloc[row]) + "\" is an outlier in attribute \"" + check_column_name + "\"")
    print(myData.get_row(row + 1))

    #  获取用户选择操作
    OutlierOperation = menu_repair_outlier_data()

    #  获取离群值所在列数
    column = myData.get_columnNumber_by_columnName(check_column_name)

    if OutlierOperation == "1":
        delete_outlier_data(myData, row)
        # 记录用户操作
        RecordUserOperation.GetUserClassifyOperation(1, AbnormalValue, column, row, 0)

    elif OutlierOperation == "2":
        value = repair_outlier_data(myData, row, column)
        # 记录用户操作
        RecordUserOperation.GetUserClassifyOperation(1, AbnormalValue, column, row, 1)
        # 记录用户修复的数据值
        RecordUserOperation.GetUserRepairValue(1, AbnormalValue, column, row, value)

    elif OutlierOperation == "3":
        pass
        # 记录用户操作
        RecordUserOperation.GetUserClassifyOperation(1, AbnormalValue, column, row, 2)

    else:
        print("invalid operation")


# 离群值数据修复选项菜单
def menu_repair_outlier_data():
    print("\nwhich operation do you prefer to solve the outlier data?")
    print("1. delete the row which includes the outlier data")
    print("2. Assign a value for the outlier data")
    print("3. Ignore and mark that this cell is correct")
    OutlierOperation = input()
    return OutlierOperation


# 修复离群值数据
def repair_outlier_data(myData, row, column):
    value = input("input the value to replace the outlier unit: ")
    myData.change_cell(row, column, value)
    return value


# 删除离群值数据所在行
def delete_outlier_data(myData, row):
    myData.delete_row(row)
