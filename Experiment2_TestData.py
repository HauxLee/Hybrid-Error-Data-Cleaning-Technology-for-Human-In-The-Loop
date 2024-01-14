#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pandas as pd
from tensorflow import keras
from keras import layers,models
from keras.utils import to_categorical
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

# 测试次数
test_times = 50

# 正确回归次数
correct_regression = 0

# 总的数据量
total_data = 1000000

# 有用数据占总数据的比例
useful_data_ratio = 0.25

# 环境变化前有用数据占有用数据的比例
before_useful_data_ratio = 0.9

# 训练集路径
record_regression_path = 'ExperimentDataSet/' + str(total_data) + '_' + str(useful_data_ratio) + '_' + str(before_useful_data_ratio) + '_exp2.csv'

for i in range(1, test_times):
    RecordedFile = pd.read_csv(record_regression_path)

    #  获取数据和标签
    RecordedData = RecordedFile.iloc[:, :-1]
    RecordedLabel = RecordedFile.iloc[:, -1]

    #  转换为numpy数组
    RecordedData = RecordedData.values
    RecordedLabel = RecordedLabel.values.reshape(-1, 1)

    # print(RecordedData)  # test
    # print(RecordedLabel)  # test

    #  构建K近邻回归模型
    knn = KNeighborsRegressor(n_neighbors=int(0.0001 * total_data))
    knn.fit(RecordedData, RecordedLabel)

    #  预测修复值
    AbnormalReason = 1
    AbnormalValue = np.random.randint(27000, 28000)
    AbnormalColumn = 1
    if i < 0.5 * test_times:
        AbnormalRow = np.random.randint(0.1 * total_data, 0.25 * total_data)
    else:
        AbnormalRow = np.random.randint(0.75 * total_data, 0.9 * total_data)

    input_data = [[AbnormalReason, AbnormalValue, AbnormalColumn, AbnormalRow]]
    PredictedValue = int(knn.predict(input_data)[0][0])

    print(PredictedValue)  # test

    if i < 0.5 * test_times and 13000000 < PredictedValue < 13000100:
        correct_regression = correct_regression + 1
    elif i > 0.5 * test_times and 13000900 < PredictedValue < 13001000:
        correct_regression = correct_regression + 1


print(correct_regression / test_times)
