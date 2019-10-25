# 用python玩转数据-笔记

## 第二章 | 

### 2.1 range函数

- 语法：range(start,end,step= 1)  /range(end)
  - 可迭代(interable)与for联用

- while循环

  - 语法：

    - ~~~python
      #赋初值
      while expression：
      	suite_to_repeat
      ~~~

    - 避免死循环程序

- for循环

  - iterator 迭代器

  - 逐个迭代；索引迭代(字符串对应的下标（索引）)

  - ~~~python
    # 索引迭代
    s = 'python'
    for i in range(len(s)):
    	print(s[i],end = ' ')
    ~~~

- 迭代器：(iterator)

  - ~~~python
    x = iter(range(10))
    next(x)
    # 0~9
    
    from collections.abc import Iterator,Iterable
    isinstance(range(10),Iterator) 
    ~~~

- 案例：

  - ~~~python
    # 最大公约数
    ## 余数为新分子
    x = eval(input("x =  "))
    y = eval(input("y =  "))
    if x < y:
    	x,y = y,x
    while x % y != 0:
    	r = x%y
    	x = y
    	y = r
    print('result =  ',y)
    ~~~

  - ~~~python
    # 兑钱方案：1￥ 1，2,5分
    i = j = k = 0
    count = 0
    for i in range(21):
    	for  j in range(51):
    		k = 100 - 5*1 -j*2
    		if k >= 0:
    			count += 1
    print("count =  ",count)        
    ~~~

  ### 2.4 循环中的break，continue

  ```python
  # 累加 
  sumA = 0
  i = 1
  while True:
      sumA += 1
      i += 1
      if sumA > 10:
          break
  # 终止当前循环 ，执行循环之后的语句
  print("i = {},sumA = ()".format(i,sumA))
  ```

  

  ```python
  # 输出2~100之间的素数——能被[2~x^0.5] 整除
  ## 先搭框架
  from math import sqrt
  j = 2
  while j <= 10:
      i = 2
      k = sqrt(j)
      while i <= k:
          if j % i == 0:
              break
      # break 之后应接循环
          i += 1
      if i > k:
          print(j,end = ' ')
      j += 1
      
      
      # 2.4 flag?
  ```

  ```python
  sumA = 0
  i = 1
  while i <= 5:
      sumA += 1
      i += 1
      if i >= 3:
          continue
      # 条件满足则跳过该语句，并执行剩余循环周期
  print("i = {},sumA = ()".format(i,sumA))
  
  ```

  

  - while 中用于判断循环条件是否满足 for 循环中则判断迭代是否结束

  - 循环中的else： 如果代码从break处终止，则跳出循环 正常结束循环则执行else中代码

### 2.5 自定义函数

~~~
# 关键字——def
# 语法：def function_name（函数名）([arguement]（内部参数可选）):
# '''docstring''' 用于介绍函数的功能
# 查看函数docstring:  (print fn.__doc__)

#默认参数-可以改变
# 默认参数后面不可以跟非默认参数
# 默认参数放在参数最后！
# 关键字参数允许改变参数列表中的参数顺序


# 使用 lambda 匿名函数

~~~

