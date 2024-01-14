#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pandas as pd
from keras import layers
from keras.utils import to_categorical
from tensorflow import keras
from sklearn.neighbors import KNeighborsRegressor

import RecordUserOperation

from sklearn.preprocessing import MinMaxScaler

# 设立置信度
confidence = 0.4


#  机器学习分类预测操作
def predict_operation_result(AbnormalReason, AbnormalValue, AbnormalColumn, AbnormalRow, myData):
    #  读取操作数据
    record_classify_path = RecordUserOperation.record_classify_path  # 记录用户操作文件的路径
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
    L0 = layers.Input(shape=4, name="inputLayer")  # 输入层
    L1 = layers.Dense(units=4, activation="softmax", name="haddenlayer")  # 隐藏层
    L2 = layers.Dense(units=4, activation="softmax", name="outputlayer")  # 输出层

    nnOutput = L2(L1(L0))
    nn = keras.models.Model(inputs=L0, outputs=nnOutput)  # 转换为Keras模型

    # 将标签数据转换为独热编码形式
    one_hot_labels = to_categorical(RecordedLabel, num_classes=4)

    # 训练模型
    nn.compile(loss="categorical_crossentropy", optimizer="adam")
    nn.fit(RecordedData, one_hot_labels)

    # 预测数据
    input_data = [[AbnormalReason, AbnormalValue, AbnormalColumn, AbnormalRow]]
    predictResult = nn.predict(input_data)[0]
    # print(predictResult)  # test

    # 获取预测结果
    confidence_delete = predictResult[0]
    confidence_repair = predictResult[1]
    confidence_ignore = predictResult[2]
    # print(confidence_delete)  # test

    # 判断是否满足置信度要求
    if confidence_delete > confidence:  # 删除置信度满足要求， 删除异常数据所在行
        myData.delete_row(AbnormalRow)
        return True
    elif confidence_repair > confidence:  # 修复置信度满足要求， 修复异常数据值
        #  回归模型得到修复值并输出到文件
        predict_repair_value(AbnormalReason, AbnormalValue, AbnormalColumn, AbnormalRow, myData)
        return True
    elif confidence_ignore > confidence:  # 忽略置信度满足要求， 忽略异常数据
        return True
    else:
        return False  # 不满足置信度要求，由用户选择操作


#  机器学习回归得到修复值
def predict_repair_value(AbnormalReason, AbnormalValue, AbnormalColumn, AbnormalRow, myData):
    #  读取操作数据
    record_repair_path = RecordUserOperation.record_repair_path  # 记录用户提供修复值文件的路径
    RecordedFile = pd.read_csv(record_repair_path)

    #  获取数据和标签
    RecordedData = RecordedFile.iloc[:, :-1]
    RecordedLabel = RecordedFile.iloc[:, -1]

    #  转换为numpy数组
    RecordedData = RecordedData.values
    RecordedLabel = RecordedLabel.values.reshape(-1, 1)

    # print(RecordedData)  # test
    # print(RecordedLabel)  # test

    #  构建K近邻回归模型
    knn = KNeighborsRegressor(n_neighbors=3)
    knn.fit(RecordedData, RecordedLabel)

    #  预测修复值
    input_data = [[AbnormalReason, AbnormalValue, AbnormalColumn, AbnormalRow]]
    PredictedValue = int(knn.predict(input_data)[0][0])

    # print(PredictedValue)  # test

    #  将预测的修复值写入文件
    myData.change_cell(AbnormalRow, AbnormalColumn, PredictedValue)
