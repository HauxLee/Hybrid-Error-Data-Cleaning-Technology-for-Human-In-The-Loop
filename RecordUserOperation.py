#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import pandas as pd

# 记录用户操作文件路径
record_classify_path = 'RecordUserOperation/record_user_operation.csv'
record_repair_path = 'RecordUserOperation/record_repair_value.csv'


#  记录用户修改数据方式

# 参数一：数据异常原因
#       0 - 数据缺失
#       1 - 数据离群

# 参数二：原数据值
#       0 - 数据值缺失
#       非0整数 - 原数据值

# 参数三：异常数据值所在列数

# 参数四：异常数据值所在行数

# 参数五：用户修改方式
#       0 - 数据被删除
#       1 - 数据被修改
#       2 - 数据被忽略异常

def GetUserClassifyOperation(AbnormalReason, AbnormalValue, AbnormalColumn, AbnormalRow, ModifiedMethod):
    # 添加记录数据
    NewRecordedData = {'AbnormalReason': [AbnormalReason], 'AbnormalValue': [AbnormalValue],
                       'AbnormalColumn': [AbnormalColumn], 'AbnormalRow': [AbnormalRow],
                       'ModifiedMethod': [ModifiedMethod]}

    # 写入记录表单
    df = pd.DataFrame(NewRecordedData)
    df.to_csv(record_classify_path, mode='a', index=False, header=False)


#
#
#  记录用户修复数据的值

# 参数一 0 - 数据值缺失
#       1 - 数据值存在

# 参数二：原数据值
#       0 - 数据值缺失
#       非0整数 - 原数据值

# 参数三：异常数据值所在列数

# 参数四：异常数据值所在行数

# 参数五：用户修改的数据值

def GetUserRepairValue(AbnormalReason, AbnormalValue, AbnormalColumn, AbnormalRow, RepairedValue):
    # 添加记录数据
    NewRecordedData = {'AbnormalReason': [AbnormalReason], 'AbnormalValue': [AbnormalValue],
                       'AbnormalColumn': [AbnormalColumn], 'AbnormalRow': [AbnormalRow],
                       'RepairedValue': [RepairedValue]}

    # 写入记录表单
    df = pd.DataFrame(NewRecordedData)
    df.to_csv(record_repair_path, mode='a', index=False, header=False)
