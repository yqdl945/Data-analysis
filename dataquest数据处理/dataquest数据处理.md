### dataquest数据处理

1. 展开+探索

   ~~~python
   from csv import reader
   
   ### The Google Play data set ###
   opened_file = open('googleplaystore.csv')
   read_file = reader(opened_file)
   android = list(read_file)	#将file转换成list 否则无法读取
   android_header = android[0] #头部标签
   android = android[1:]		#主体内容！
   
   ~~~

   ~~~python
   # 设定函数-探索数据
   # 
   def explore_data(dataset, start, end, rows_and_columns=False):
       dataset_slice = dataset[start:end] #从数据主体部分选定0-2 3行数据   
       for row in dataset_slice:
           print(row)
           print('\n') # adds a new (empty) line between rows
           
       if rows_and_columns:	# 默认是True？输入True之后便能打印
           print('Number of rows:', len(dataset))
           print('Number of columns:', len(dataset[0]))
   
   print(android_header)
   print('\n')
   explore_data(android, 0, 3, True)
   ~~~

2. 删除错误值（感觉使用DataFrame比较方便一些--decrible）



3. 移除重复数据

   ~~~python
   # 使用循环将重复和非重复提取出来！
   duplicate_apps = []	#重复
   unique_apps = []	#非重复
   
   for app in android:
       name = app[0]
       if name in unique_apps:
           duplicate_apps.append(name)
       else:
           unique_apps.append(name)
       
   print('Number of duplicate apps:', len(duplicate_apps))
   print('\n')
   print('Examples of duplicate apps:', duplicate_apps[:15])
   ~~~

   ~~~python
   # 确认评分最高值——不重不漏
   
   reviews_max = {}
   
   for app in android:
       name = app[0]
       n_reviews = float(app[3])
       
       if name in reviews_max and reviews_max[name] < n_reviews:
           reviews_max[name] = n_reviews
           
       elif name not in reviews_max:
           reviews_max[name] = n_reviews
           
   
   android_clean = []
   already_added = []
   
   for app in android:
       name = app[0]
       n_reviews = float(app[3])
       
       if (reviews_max[name] == n_reviews) and (name not in already_added):
           android_clean.append(app)
           already_added.append(name) # make sure this is inside the if block
   ~~~

   

4. 清洗数据

   ~~~python
   # 移除非英语app ord(string)唯一——A-Z,a-z(127)
   
   def is_english(string):
       non_ascii = 0		# 添加计数器，控制误差范围
       
       for character in string:
           if ord(character) > 127:
               non_ascii += 1
       
       if non_ascii > 3:
           return False
       else:
           return True
   
   print(is_english('Docs To Go™ Free Office Suite'))
   print(is_english('Instachat 😜'))
   
   ~~~

   ~~~python
   android_english = []
   ios_english = []
   
   for app in android_clean:
       name = app[0]
       if is_english(name):# 符合is_english函数？——加入到android_clean中？
           android_english.append(app)#完整的App信息！
           
   for app in ios:
       name = app[1]
       if is_english(name):
           ios_english.append(app)        
   ~~~

   ~~~python
   # 提取免费软件的信息！
   android_final = []
   ios_final = []
   
   for app in android_english:
       price = app[7]
       if price == '0':
           android_final.append(app)
           
   for app in ios_english:
       price = app[4]
       if price == '0.0':
           ios_final.append(app)
           
   print(len(android_final))
   print(len(ios_final))
   ~~~

   

