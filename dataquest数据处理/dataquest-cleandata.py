#!/usr/bin/env python
# coding: utf-8

# # Introduction: The beginning of DA&DS
# ## Over there, 

# In[ ]:


from csv import reader
open_apple_file = open('AppleStore.csv')
open_google_file = open('googleplaystore.csv')
apple_data = reader(open_apple_file)
google_data = reader(open_google_file)

apple_data_list = list(apple_data)
google_data_list = list(google_data)

android_header = google_data_list[0]
android_ = google_data_list[1:]

apple_header = apple_data_list[0]
apple_ = apple_data_list[1:]




def explore_data(dataset,start,end,rows_and_columns = False):
    datas = dataset[start:end]
    for row in dataset:
        print(row)
        print('\n')
        
    if rows_and_columns:
        print('number of rows:',len(dataset))
        print('colums:',dataset[0])
        
print(android_header)
print('\n')
explore_data(android_,0,3,True)


print(apple_header)
print('\n')
explore_data(android_,0,3,True)


# In[ ]:


'''print(android_[10472])
print('\n')
print(android_header)
print('\n')
print(android_[0])'''

print(android_[10472])  # incorrect row
print('\n')
print(android_header)  # header
print('\n')
print(android_[0])      # correct row


# In[]:


print(len(android_))
del android_[10472]
print(len(android_))


# In[ ]:
duplicate_apps = [] # 重复的App
unique_apps = []    # 非重复

for app in android_:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
    
print('Number of duplicate apps:', len(duplicate_apps))
print('\n')
print('Examples of duplicate apps:', duplicate_apps[:15])


# In[]:

# 更新最大评分值！
reviews_max = {}

for app in android_:
    name = app[0]
    n_reviews = float(app[3])
    
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
        
    elif name not in reviews_max:
        reviews_max[name] = n_reviews
        
# In[]:
#数据清洗（android + Apple）
android_clean = []
already_added = []

for app in android_:
    name = app[0]
    n_reviews = float(app[3])
    
    if (reviews_max[name] == n_reviews) and (name not in already_added):
        android_clean.append(app)
        already_added.append(name) # make sure this is inside the if block
explore_data(android_clean,0,3,True)

# In[]:
# 移除非英语的app

def is_english(string):
    
    for character in string:
        if ord(character) > 127:
            return False
    
    return True

print(is_english('Instagram'))
print(is_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))


# In[]:

# 增加计数器功能，控制误差范围
def is_english(string):
    non_ascii = 0
    
    for character in string:
        if ord(character) > 127:
            non_ascii += 1
    
    if non_ascii > 3:
        return False
    else:
        return True

print(is_english('Docs To Go™ Free Office Suite'))
print(is_english('Instachat 😜'))

# In[]:
