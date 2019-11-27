## 函数的默认参数

### 使用# 进行注释，使用’‘’ ‘’‘  进行注意点补充！

~~~python
def fun_ction(a,b,defult = True)

# 功能：联合if else实现两种或多种功能于一体
def fun_ction(a,b,defult = True/False)
	if defult:
        return xx
    else:
        return y
aim = fun_ction(a,b,defult = True)

# 不添加默认参数可以将目标函数均输出！

def fun_ction(a,b):
    sum_f = a + b
    difference_f = a - b
    return sum_f,difference_f
# 输出值和return后的返回值放置位置有关

'''变量赋值使用全部完成后再行提取！——returning Multiple varibles'''

'''! !return result1,result2——返回的是（result1，result2） 元组
! !要返回列表则使用return[result1,result2]'''

## https://app.dataquest.io/m/316/functions%3A-intermediate/8/functions-code-running-quirks



~~~

This kind of temporary memory storage doesn't apply to the code that is being run outside function definitions. If we define `x = 3.14` in our **main program** (outside function definitions), we can use `x` later on without having to worry that it was erased from memory.

区别于 **主程序和函数功能区！**

![img](https://s3.amazonaws.com/dq-content/316/py1m6_cb33.svg)

## 元组、列表

~~~python
'''使用元组和列表进行赋值'''
a_list = [1,2]
valiable1,valiable2 = a_list
等价于
v1 = a_list[0]
v2 = a_list[1]

'''结果进行赋值'''
def sum_and_difference(a,b):
    a_sum = a+b
    a_difference = a-b
    return a_sum,a_difference

a_sum,a_difference = sum_and_difference(15,5)
#输出结果a_sum = 20,a_difference = 10

~~~





## Q：如何输出字典中value值大于某个值的items？

- A

~~~python
# 使用if else语句：
# 两个空的list分别装重复，不重复的name
for name in google_data_list:
	if name in unique_app:
		duplicate_app.append(name)
    else:
        unique_app.append(name)

~~~



### 增加计数器控制容错率

~~~python
def function():
    f_name = 0
    for loop:
    	if "taiojian":
        	f_name += 1
"""第二个判断位置和 for 条件并列！"""
	if 'taiojian2':
        return Fale/True
    return False/True

~~~

##  否定之前既定情况 使用 if not xx:

~~~python
# 非上方的情况：
for row in moma:
    nationality = row[2]
    nationality = nationality.title()
    
    if not nationality:
        nationality = 'Nationality Unknown'
    row[2] = nationality
~~~

## 缩减代码！（减小报错）？？？Spyder行不通？？？

~~~python
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def stripped_test_data(test_data):

    # 该部分不使用字符串检验，直接进行替代？
    '''for string in test_data:
        for s in string:
            if s in bad_chars:
                string = string.replace(s,'')'''
    for char in bad_chars:
        test_data = test_data.replace(char,'')
    return test_data

stripped_test_data = []
for s in test_data():
    data = stripped_test_data(s)
    stripped_test_data.append(data)
    
print(stripped_test_data)
~~~

## 使用 split 分隔 生成的结果是list

~~~python
string = ‘1996-1997’
print(string.split('-'))
['1996','1997']
~~~

## 条件完成生成list

~~~python
ages = []
for  row in moma:
    date = row[6]
    birth = row[3]
    if type(birth) == int:	
# 因为此处的type（type（birth））是 type！——此处的int 不需要加''
        age = date - birth
        #ages.append(age)
        
    else:
        age = 0
        #ages.append(age)
	ages.append(age)		
    
'''
注意此时ages的位置和if 平齐！，
如果不注释掉两个append语句，导致结果只有一个unknown!
'''
~~~

## **If the item is not a key in decade_frequency,** add it as a key with a value of `1`

~~~python
# 不需要使用 dictory[keys]
decade_frequency = {}

for row in decades:
    if row not in decade_frequency:	#不需要写成decade_frequency[keys]
        decade_frequency[row] = 1
    else:
        decade_frequency[row] += 1

~~~

## 关于return

~~~python
#如果定义的函数中不包含return，虽然定义里面有print语句，但调用之后使用print输出的结果是None！

~~~

1. 如果return 后跟的参数是def 函数内的调用函数后不使用print依旧可以输出数据
2. 如果return 后跟的返回参数不是def 函数中的参数，那么调用完自定义函数后依旧需要print(fun)否则没有结果展示出来

##  关于print在for函数之后的什么位置

~~~python
1.在for函数内部——每次循环输出一个值
2.在for函数外部，只输出最后一个循环的结果！
~~~

## 使用format函数

~~~python
print('{位置：,.2f}'.format(rr))
1.数据定位
2.:
3.千位分隔符,
4.精度

# 使用字典之后 在format函数中对k-v再次进行替换（可以用原字符替代）
for g,n in gender_freq.items():
    print("There are {n:,} artworks by {g} artists".format(g = g,n = n ))
#这样也可以：
for g,n in gender_freq.items():
    print("There are {1:,} artworks by {0} artists".format(g,n ))
~~~

## 程序运行时长

~~~python
import time
 
start = time.clock()
 
#当中是你的程序
 
elapsed = (time.clock() - start)
print("Time used:",elapsed)
~~~

