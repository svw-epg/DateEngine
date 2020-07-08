import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from efficient_apriori import apriori


# header=None，不将第一行作为head
dataset = pd.read_csv('D:/d/Zhuangwenjia D/试验报告/学习/python视频/第四课/L4/MarketBasket/Market_Basket_Optimisation.csv', header = None) 
# shape为(7501,20)
print(dataset.shape)
#print(dataset[:10])

"""
#efficient_apriori方法
# 将数据存放到transactions中
transactions = []
for i in range(0, dataset.shape[0]):
    temp = []
    for j in range(0, 20):
        if str(dataset.values[i, j]) != 'nan':
           temp.append(str(dataset.values[i, j]))
    transactions.append(temp)



# 挖掘频繁项集和频繁规则
itemsets, rules = apriori(transactions, min_support=0.02,  min_confidence=0.4)
print("频繁项集：", itemsets)
print("关联规则：", rules)

"""
#mlxtend方法
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

pd.options.display.max_columns=100

#空值填写
dataset = dataset.fillna("")

#将所有列合并为一列
col=dataset.columns
dataset['new']=""
for i in col:
    dataset.new=dataset.new+'|'+dataset[i]

#独热编码
hot_encoded = dataset.drop(dataset.columns[:21],axis=1).join(dataset.new.str.get_dummies(sep='|'))
print(hot_encoded.head)
#hot_encoded.to_csv('D:/d/Zhuangwenjia D/试验报告/学习/python视频/第四课/L4/MarketBasket/Market_Basket_hotcode.csv')

# 挖掘频繁项集，最小支持度为0.02,结果排序
itemsets = apriori(hot_encoded,use_colnames=True, min_support=0.02)
itemsets = itemsets.sort_values(by="support" , ascending=False) 
print("频繁项集：", itemsets)


# 根据频繁项集计算关联规则，设置最小提升度为1.5，结果排序
rules =  association_rules(itemsets, metric='lift', min_threshold=1.5)
rules = rules.sort_values(by="lift" , ascending=False) 
print("关联规则：", rules)
