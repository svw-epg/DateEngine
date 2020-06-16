# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:50:36 2020

@author: ZhuangWenjia
"""


from pandas import Series,DataFrame
data={'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
df1=DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'],columns=['语文','数学','英语'])
print('平均成绩')
print(df1.mean())
print('最高成绩')
print(df1.max())
print('最低成绩')
print(df1.min())
print('成绩方差')
print(df1.var())
print('成绩标准差')
print(df1.std())
df1['总分']=df1.sum(axis=1)
print(df1.sort_values('总分',ascending=False))
