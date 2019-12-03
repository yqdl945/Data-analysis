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

