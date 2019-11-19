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

