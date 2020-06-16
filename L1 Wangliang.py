#HW1 求2+4+6+8+...+100的求和
sum=0
number=2
while number<=100:
    sum=sum+number
    number=number+2
print(sum)

#HW2

import pandas as pd
from pandas import DataFrame
#建立模型
data = {'语文': [68, 95, 98, 90,80],'数学': [65, 76, 86, 88, 90],'英语': [30, 98, 88, 77, 90]}
df = DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'], columns=['语文', '数学', '英语'])
print (df)
print ('平均成绩:')
print (df.mean())
print ('最小成绩:')
print (df.min())
print ('最大成绩:')
print (df.max())
print ('方差:')
print (df.var())
print ('标准差:')
print (df.std().astype('int64'))
#行求和axis=1
df['总分']=df.sum(axis=1)
#正向排序ascending=False
print(df.sort_values(by='总分',ascending=False))

#HW3
import pandas as pd

#数据加载
result = pd.read_csv('D:/car_complain.csv')

# 分列处理
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
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