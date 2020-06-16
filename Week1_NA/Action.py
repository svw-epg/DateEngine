# # Action1: 求2+4+6+8+...+100的求和，用Python该如何写
#
# result = 0
# a = 2
# while a <= 100:
#     result = a + result
#     a += 2
# print(result)

# # Action2: 统计全班的成绩
# import pandas as pd
#
# score = pd.DataFrame({'语文': [68, 95, 98, 90, 80],
#                       '数学': [65, 76, 86, 88, 90],
#                       '英语': [30, 98, 88, 77, 90]},
#                      index=['张', '关', '刘', '典', '许'])
# score["max"] = score[['语文', '数学', '英语']].max(axis=1)
# score["min"] = score[['语文', '数学', '英语']].min(axis=1)
# score["var"] = score[['语文', '数学', '英语']].var(ddof=0, axis=1)
# score["std"] = score[['语文', '数学', '英语']].std(axis=1)
# score["sum"] = score[['语文', '数学', '英语']].sum(axis=1)
# score.sort_values(by=['sum'], inplace=True, ascending=False)
# print(score)

# Action3: 对汽车质量数据进行统计
import pandas as pd

result = pd.read_csv("car_complain.csv")
print(result)
# 将genres进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）
result = result.drop("problem", 1).join(result.problem.str.get_dummies(","))
print(result.columns)
tags = result.columns[7:]
print(tags)

df = result.groupby(['brand'])['id'].agg(['count'])
df2 = result.groupby(['brand'])[tags].agg(['sum'])
df2 = df.merge(df2, left_index=True, right_index=True, how='left')
print(df2)
# 通过reset_index将DataFrameGroupBy => DataFrame
df2.reset_index(inplace=True)
df2.to_csv('temp.csv')
df2 = df2.sort_values('count', ascending=False)
# print(df2)
# print(df2.columns)
# df2.to_csv('temp.csv', index=False)
query = ('A11', 'sum')
# print(df2.sort_values(query, ascending=False))
