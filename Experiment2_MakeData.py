#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

# 总的数据量
total_data = 1000000

# 有用数据占总数据的比例
useful_data_ratio = 0.25

# 环境变化前有用数据占有用数据的比例
before_useful_data_ratio = 0.9

# 环境变化后有用数据占有用数据的比例
after_useful_data_ratio = 1 - before_useful_data_ratio

# 有用数据数量
useful_data_count = int(total_data * useful_data_ratio)

# 环境变化前有用数据的数量
before_useful_data_count = int(useful_data_count * before_useful_data_ratio)

# 环境变化后有用数据的数量
after_useful_data_count = int(useful_data_count * after_useful_data_ratio)

# 无用数据的数量
useless_data_count = total_data - useful_data_count

# 环境改变前有用数据的生成
before_correct_useful_data = pd.DataFrame({
    '参数一': np.ones(before_useful_data_count),
    '参数二': np.random.randint(27000, 28000, before_useful_data_count),
    '参数三': np.ones(before_useful_data_count),
    '参数四': np.random.randint(0.1 * total_data, 0.25 * total_data, before_useful_data_count),
    '参数五': np.random.randint(13000000, 13000100, before_useful_data_count)
})

# 环境改变后有用数据的生成
after_correct_useful_data = pd.DataFrame({
    '参数一': np.ones(after_useful_data_count),
    '参数二': np.random.randint(27000, 28000, after_useful_data_count),
    '参数三': np.ones(after_useful_data_count),
    '参数四': np.random.randint(0.75 * total_data, 0.9 * total_data, after_useful_data_count),
    '参数五': np.random.randint(13000900, 13001000, after_useful_data_count)
})

# 无用数据的生成
useless_data = pd.DataFrame({
    '参数一': np.random.choice([0, 1], useless_data_count),
    '参数二': np.random.randint(1, 50000, useless_data_count),
    '参数三': np.ones(useless_data_count),
    '参数四': np.random.randint(1, total_data + 1, useless_data_count),
    '参数五': np.random.randint(13000000, 13001000, useless_data_count)
})

# 合并所有数据
all_data = pd.concat([before_correct_useful_data, after_correct_useful_data, useless_data])

# 打乱数据
all_data = all_data.sample(frac=1).reset_index(drop=True)

# 输出数据到csv文件
all_data.to_csv('ExperimentDataSet/' + str(total_data) + '_' + str(useful_data_ratio) + '_' + str(before_useful_data_ratio) + '_exp2.csv', index=False)


