#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import MissingDataOperation
import OutlierDataOperation


def user_operation(path):
    while True:
        # 选择清洗种类
        print("1. check missing data")
        print("2. check outlier data")
        print("0. exit")
        operation = input("choose operation: ")
        if operation == "0":
            break
        elif operation == "1":
            MissingDataOperation.check_missing_data(path)
        elif operation == "2":
            OutlierDataOperation.check_outlier_data(path)
        else:
            print("invalid operation")

        # 选择是否进行下一次清洗操作
        ContinueOperation = input("Continue cleaning? input [Y/N]: ")
        if ContinueOperation == "N":
            break
