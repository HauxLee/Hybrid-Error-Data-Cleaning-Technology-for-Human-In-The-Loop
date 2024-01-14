#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pandas as pd
from keras import layers, models
from keras.utils import to_categorical
from tensorflow import keras
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

# 测试次数
test_times = 50

# 正确分类次数
correct_classify = 0

# 总的数据量
total_data = 1000000

# 正确有用数据和错误有用数据占总数据的比例
useful_data_ratio = 0.25

# 正确有用数据占有用数据的比例
correct_useful_data_ratio = 1

# 训练集路径
record_classify_path = 'ExperimentDataSet/' + str(total_data) + '_' + str(useful_data_ratio) + '_' + str(
    correct_useful_data_ratio) + '_exp1.csv'
for i in range(1, test_times):
    RecordedFile = pd.read_csv(record_classify_path)

    #  获取数据和标签
    RecordedData = RecordedFile.iloc[:, :-1]
    RecordedLabel = RecordedFile.iloc[:, -1]

    #  转换为numpy数组
    RecordedData = RecordedData.values
    RecordedLabel = RecordedLabel.values.reshape(-1, 1)

    # print(RecordedData)  # test
    # print(RecordedLabel)  # test

    # # 数据归一化
    # scaler = MinMaxScaler()
    # normalizedData = scaler.fit_transform(RecordedData)
    # normalizedLabel = scaler.fit_transform(RecordedLabel)
    #
    # print(normalizedData)  # test
    # print(normalizedLabel)  # test

    # 构建神经网络模型
    L0 = layers.Input(shape=(4,), name="inputLayer")  # 输入层
    L1 = layers.Dense(units=8, activation="relu", name="hiddenLayer")  # 隐藏层
    L2 = layers.Dense(units=4, activation="softmax", name="outputLayer")  # 输出层

    nn = models.Sequential([L0, L1, L2])

    nn.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])

    # 将标签数据转换为独热编码形式
    one_hot_labels = to_categorical(RecordedLabel, num_classes=4)

    # 训练模型
    nn.compile(loss="categorical_crossentropy", optimizer="adam")
    nn.fit(RecordedData, one_hot_labels)

    # 预测数据
    AbnormalReason = 1
    AbnormalValue = np.random.randint(27000, 28000)
    AbnormalColumn = 1
    AbnormalRow = np.random.randint(1, total_data + 1)

    input_data = [[AbnormalReason, AbnormalValue, AbnormalColumn, AbnormalRow]]
    predictResult = nn.predict(input_data)[0]
    print(predictResult)  # test

    # 获取预测结果
    confidence_delete = predictResult[0]
    confidence_repair = predictResult[1]
    confidence_ignore = predictResult[2]

    if confidence_repair > confidence_ignore and confidence_repair > confidence_delete:
        correct_classify = correct_classify + 1

print(correct_classify / test_times)

