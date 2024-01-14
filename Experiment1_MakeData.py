#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

# 总的数据量
total_data = 10000

# 正确有用数据和错误有用数据占总数据的比例
useful_data_ratio = 0.25

# 正确有用数据占有用数据的比例
correct_useful_data_ratio = 1

# 错误有用数据占有用数据的比例
wrong_useful_data_ratio = 1 - correct_useful_data_ratio

# 有用数据数量
useful_data_count = int(total_data * useful_data_ratio)

# 正确有用数据的数量
correct_useful_data_count = int(useful_data_count * correct_useful_data_ratio)

# 错误有用数据的数量
wrong_useful_data_count = int(useful_data_count * wrong_useful_data_ratio)

# 无用数据的数量
useless_data_count = total_data - useful_data_count

# 正确有用数据的生成
correct_useful_data = pd.DataFrame({
    '参数一': np.ones(correct_useful_data_count),
    '参数二': np.random.randint(27000, 28000, correct_useful_data_count),
    '参数三': np.ones(correct_useful_data_count),
    '参数四': np.random.randint(1, total_data + 1, correct_useful_data_count),
    '参数五': np.ones(correct_useful_data_count)
})

# 错误有用数据的生成
wrong_useful_data = pd.DataFrame({
    '参数一': np.ones(wrong_useful_data_count),
    '参数二': np.random.randint(27000, 28000, wrong_useful_data_count),
    '参数三': np.ones(wrong_useful_data_count),
    '参数四': np.random.randint(1, total_data + 1, wrong_useful_data_count),
    '参数五': np.random.choice([0, 2], wrong_useful_data_count)
})

# 无用数据的生成
useless_data = pd.DataFrame({
    '参数一': np.random.choice([0, 1], useless_data_count),
    '参数二': np.random.randint(1, 10000000, useless_data_count),
    '参数三': np.ones(useless_data_count),
    '参数四': np.random.randint(1, total_data + 1, useless_data_count),
    '参数五': np.random.choice([0, 1, 2], useless_data_count)
})

# 合并所有数据
all_data = pd.concat([correct_useful_data, wrong_useful_data, useless_data])

# 打乱数据
all_data = all_data.sample(frac=1).reset_index(drop=True)

# 输出数据到csv文件
all_data.to_csv('ExperimentDataSet/' + str(total_data) + '_' + str(useful_data_ratio) + '_' + str(correct_useful_data_ratio) + '_exp1.csv', index=False)

