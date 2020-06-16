# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:39:46 2020

@author: ZhuangWenjia
"""

import pandas as pd

#数据加载
result = pd.read_csv('D:/car_complain.csv')

# 将genres进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）逗号为分割符
result = result.drop('problem', axis=1).join(result.problem.str.get_dummies(','))
print(result.columns)

#对品牌投诉进行排序
df1= result.groupby(['brand'])['id'].agg(['count'])
print('品牌投诉排名：')
print(df1.sort_values('count', ascending=False))

#对车型投诉进行排序
df2=result.groupby(['car_model'])['id'].agg(['count'])
print('车型投诉排名：')
print(df2.sort_values('count',ascending=False))

#品牌的平均车型投诉排名
df3=result.groupby(['brand','car_model'])['id'].agg(['count'])
df3.reset_index(inplace=True)
df3=df3.groupby(['brand'])['count'].agg('mean')
print('品牌平均车型投诉排名：')
print(df3.sort_values(ascending=False))

