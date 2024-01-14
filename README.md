### I. Project Overview

This study introduces a hybrid human-in-the-loop framework for erroneous data cleaning. The framework comprises methods for detecting and repairing two common data quality issues: missing points and outliers. The algorithm first assesses whether it can automatically correct anomalies. If it does not meet the confidence threshold, it interacts with human experts, involving them in the repair while recording their opinions. This approach allows human experts to continuously adjust the dynamic rational value range of the data, achieving more accurate detection and repair of anomalies. It aims to improve data cleaning quality while reducing manual labor costs. The study conducts experiments on the classification accuracy of the proposed cleaning framework under different noise data ratios and regression accuracy after changes in the rational value environment. It considers changes in classification accuracy and predictive regression accuracy when multiple variables change. Experiments show that the framework has good application value in improving data quality when variables meet the requirements.

### II. Execution Environment

| Software | Version     |
|----------|-------------|
| Windows  | Windows 10  |
| Python   | Python 3.7  |

### III. Software Setup

**Execution Software**: Pycharm

**Configuration**:

Python packages: pandas, keras, tensorflow, sklearn, numpy

### IV. Program Introduction

| Module                | Module Description          |
|-----------------------|-----------------------------|
| main                  | Run this module to start the entire cleaning framework |
| data                  | Data operations             |
| MissingDataOperation  | Check and repair missing points  |
| OutlierDataOperation  | Check and repair outliers   |
| AutomaticCorrectData  | Machine learning-based automatic repair |
| UserOperation         | User-provided repair suggestions |
| RecordUserOperation   | Record user opinion logs    |
| Experiment1_MakeData  | Generate data for Experiment 1  |
| Experiment1_TestData  | Test results of Experiment 1 |
| Experiment2_MakeData  | Generate data for Experiment 2  |
| Experiment2_TestData  | Test results of Experiment 2 |

### V. Usage Instructions

Run `main.py` to start the entire cleaning framework.

Run `Experiment1_MakeData.py` to generate data for Experiment 1.

Run `Experiment1_TestData.py` to test the results of Experiment 1.

Run `Experiment2_MakeData.py` to generate data for Experiment 2.

Run `Experiment2_TestData.py` to test the results of Experiment 2.
