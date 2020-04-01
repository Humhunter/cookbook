#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/12/16 9:18


import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from pandasql import sqldf, load_births, load_meat

x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(x1, x2, sep='\n')
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
x3 = Series(d)
print(x3)

data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'Dianwei'],
                columns=['English', 'Math', 'Chinese'])
print(df1)
print(df2)

# 数据清理
# df2 = df2.drop(columns=['Chinese'])
#
df2 = df2.drop(index=['ZhangFei'])
# 改名
df2 = df2.rename(columns={'Chinese': 'yuwen', 'English': 'YingYu'})
# 更改数据格式
df2['Chinese'].astype('str')
df2['Chinese'].astype(np.int64)

# 删除数据间的空格
df2['Chinese'] = df2['Chinese'].map(str.strip)
df2['Chinese'] = df2['Chinese'].map(str.lstrip)
df2['Chinese'] = df2['Chinese'].map(str.rstrip)

# 删除特定符号
df2['Chinese'] = df2['Chinese'].str.strip('$')
# 全部大写
df2.columns = df2.columns.str.upper()
# 全部小写
df2.columns = df2.columns.str.lower()
# 首字母大写
df2.columns = df2.columns.str.title()

# 哪列存在空值
df2.isnull().any()

# 去重复行
df = df2.drop_duplicates()

# apply函数对数据进行清洗
df['name'] = df['name'].apply(str.upper)


def double_df(x):
    return 2 * x


df1[u'语文'] = df1[u'语文'].apply(double_df)


def plus(df, n, m):
    df['new1'] = (df[u'语文'] + df[u'英语']) * m
    df['new2'] = (df[u'语文'] + df[u'英语']) * n
    return df


# 其中axis为1代表列为轴， 为0代表行为轴
df1 = df1.apply(plus, axis=1, args=(2, 3,))
# 基于name这个列进行连接
df3 = pd.merge(df1, df2, on='name')
# inner内连接 交集
df3 = pd.merge(df1, df2, how='inner')
# 左连接，右连接
df3 = pd.merge(df1, df2, how='left')
df3 = pd.merge(df1, df2, how='right')
# outter外连接 并集
df3 = pd.merge(df1, df2, how='outer')

# 用SQL方式打开pandas
df1 = DataFrame({'name': ['ZhangFei', 'YuanMa', 'ZhaoYun', 'Qidian', 'a', 'b'], 'data1': range(5)})
pysqldf = lambda  sql:sqldf(sql, globals())
sql = "select * from df1 where name='Qidian'"
print(pysqldf(sql))