# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:01:35 2020

@author: WangShensi
"""


#求2+4+6+8+...+100的求和，用Python该如何写
sum=0
number=2
while number<=100:
    sum=sum+number
    number=number+2
print(sum)

'''Action2 
统计全班的成绩
班里有5名同学，现在需要你用Python来统计下这些人在语文、英语、数学中的平均成绩、
最小成绩、最大成绩、方差、标准差。
然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）
姓名 语文 数学 英语
张飞 68 65 30
关羽 95 76 98
刘备 98 86 88
典韦 90 88 77
许褚 80 90 90'''

import numpy as np
import pandas as pd
from pandas import DataFrame
data = {"语文": [68, 95, 98, 90,80], "数学": [65,76,86,88,90], "英语": [30,98,88,77,90]}
df = DataFrame(data, index=["张飞","关羽","刘备","典韦","许褚"], columns=["语文","数学","英语"])
print(df)
print(df.describe())
df["总分"] = df.apply(lambda x: x.sum(), axis=1)
df=df.sort_values("总分",ascending=False)
df["名次"] = [1,2,3,4,5]
print(df)

# Action3 对汽车投诉信息进行分析
import pandas as pd

result = pd.read_csv('car_complain.csv')
#print(result)
# 将genres进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))

#品牌投诉总数
df= result.groupby(['brand'])['id'].agg(['count'])
df= df.sort_values('count', ascending=False)
print(df)

#车型投诉总数
df2= result.groupby(['car_model'])['id'].agg(['count'])
df2= df2.sort_values('count', ascending=False)
print(df2)

#品牌平均车型投诉数量
df3= result.groupby(['brand','car_model'])['id'].agg(['count']).groupby('brand').mean()
df3= df3.sort_values('count', ascending=False)
print(df3)