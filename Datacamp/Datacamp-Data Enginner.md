# Datacamp-Data Enginner

## Introduction to python

### list

~~~python
#1 list中可以运算
[1+2，"a"*5]
[3,'aaaaa']

#2  复制副本后更改不改变原list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = areas[:]	# 使用该操作后更改副本不会影响原list

~~~

### Function and Package

### 有选择输入

~~~python
from math import pi
~~~





### Numpy

~~~python
#1 使用布尔值和array配合输出目标值
#light = np.array(bmi < 21)
#print(bmi[light])	bmi + [!]
# 只提取[True]对应的元素
实例
import numpy as np
arr = np.array([1,2,3,4,4,5,6,7])
a = np.array(arr>3)
print(a)
print(arr[a])

# 注意点：
'''
内部元素类型相同——类型强制
常规的四则运算对于numpy有特殊意义——内部元素对应相加
切片操作和list相同——依旧可以使用index

'''

#2 2维数组
# 输出形状：
array.shape

#3 选择np_baseball的整个第二列
print(np_baseball[:,1])

#4 计算平均值，中位数
print(np.mean(array),np.median(array))

#5 相关性corrcoef
print(np.corrcoef(array[:,0],array[:,1]))

~~~





### 连接SQL 了？





### Pandas

~~~python
#1 头部
df.head()

#2 尾部
df.tail()

#3 概览
df.info()

#4 将df 中的值提取出来
df.values

#5 使用zip构建字典
dict_name={k:v for k,v in zip(range(1,len(names)+1),names) }

#6 读取CSV文件
df1 = pd.read_csv(wenjanming )	#文件名不需要加引号！

#7 箱型图 同一张表中
df[cols].plot(kind = 'box',subplots =True )	#subplots:子图

#8 df 观测中某一列数据时写法
df.xx.median()	#xx是具体的某一个column名称，且不需要使用''！
#9 输出Enginner最小值？
print(df["Engineering"].min())
'''
Print summary statistics of the 'fare' column of df with .describe() and print(). Note: df.fare and df['fare'] are equivalent.
'''
#10 新式绘图——箱型图
years = ['1800','1850','1900','1950','2000']
df[years].plot(kind='box')

#11 条件输出提取
As an example, you can extract the rows that contain 'US' as the country of origin using df[df['origin'] == 'US'].

#12 仅访问条件行——df.loc[]
us = df.loc[df['origin'] == 'US']	# 输入错误！
~~~

**df.loc[]和df.iloc[]区别**

~~~python
import pandas as pd
from pandas import DataFrame
s = pd.DataFrame([['data',1],['beta',2],['series',3]],index = [1,2,3],columns = ['name','number'])

iloc[number]	#输出——index = number
loc[number]		#index = number-1

# 提取文本应使用loc
~~~



#### datetime

~~~python
pd.datetime()

my_datetimes = pd.to_datetime(date_list, format=time_format)  
# 提取一段时间
ts1 = ts0.loc['2010-10-11 21:00:00':'2010-10-11 22:00:00']

# 重新取样
august_highs = august.resample('D').max()	#.mean() 可以更改

# 将时间改为美国中部时间
times_tz_central = times_tz_none.dt.tz_localize('US/Central')
~~~

### 数据清洗

~~~python
# 设置DataFrame的index
df_clean = df_dropped.set_index(date_times)
~~~

~~~python
# Select the visibility and dry_bulb_faren columns and resample them: weekly_mean
weekly_mean = df_clean[['visibility','dry_bulb_faren']].resample('W').mean()
~~~



