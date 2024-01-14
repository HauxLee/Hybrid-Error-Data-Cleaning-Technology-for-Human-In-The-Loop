# Hybrid-Error-Data-Cleaning-Technology-for-Human-In-The-Loop
The framework includes detection and repair methods for missing points and outlier, two common data quality problems. This study enables human experts to continuously adjust the dynamic and reasonable value range of data to achieve more accurate detection and repair of outliers. Reduce labor costs while improving data cleaning quality.
### 一、项目名称和概述

该项目实现了毕业设计《人在环路的混合型错误数据清洗技术研究》提出的清洗框架，利用机器学习技术，
将清洗算法与人类专家的意见结合，完成对缺失点和离群值的清洗，以提高数据质量

### 二、执行环境

| 软件      | 版本         |
|---------|------------|
| windows | windows 10 |
| python  | Python 3.7 |

### 三、软件设置

**执行软件**：Pycharm

**配置**：

python包：pandas, keras, tensorflow, sklearn, numpy

### 四、程序介绍

| 模块                   | 模块描述             |
|:---------------------|------------------|
| main                 | 运行该模块以开始启动整体清洗框架 |
| data                 | 数据操作             |
| MissingDataOperation | 检查并修复缺失点         |
| OutlierDataOperation | 检查并修复离群点         |
| AutomaticCorrectData | 机器学习自动修复         |
| UserOperation        | 用户提供修复意见         |
| RecordUserOperation  | 记录用户意见记录         |
| Experiment1_MakeData | 生成用于实验一的数据       |
| Experiment1_TestData | 测试实验一结果          |
| Experiment2_MakeData | 生成用于实验二的数据       |
| Experiment2_TestData | 测试实验二结果          |

### 五、使用说明

执行`main.py` 以启动整体清洗框架

执行`Experiment1_MakeData.py` 以生成用于实验一的数据

执行`Experiment1_TestData.py` 以测试实验一结果

执行`Experiment2_MakeData.py` 以生成用于实验二的数据

执行`Experiment2_TestData.py` 以测试实验二结果
