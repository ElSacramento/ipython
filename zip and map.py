
# coding: utf-8

# ## MAP function

# In[29]:

list1 = [2,  2,  3, 10,  1]
list2 = [1, -1,  5,  4, -6]

map(lambda x, y: x*y, list1, list2)


# In[30]:

list1 = [2,  2,  3, 10,  1]
list2 = [1, -1,  5,  4, -6]
list3 = [1,  0,  1,  0,  1]

a = map(lambda x, y, z: x*y*z, list1, list2, list3)
print type(a)
print a


# In[31]:

list3 = [1,  0,  1,  0,  1]
list4 = [1,  2,  3,  1, -1,  5]

map(lambda a, b: a + b, list3, list4)


# In[41]:

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 0}

print dict1
print dict2
print map(lambda a, b: a + b, dict1, dict2)


# In[37]:

map(lambda a, b: a * b, dict1, dict2)


# In[32]:

dict3 = {3: 1, 1: 2}
dict4 = {'a': 1, 'b': 2}

map(lambda a, b: a + b, dict3, dict4)


# In[44]:

dict3 = {3: 1, 1: 2}
dict5 = {5: 1, 7: 2}

print dict3
print dict5
result = map(lambda a, b: a + b, dict3, dict5)
print result
print type(result)


# In[45]:

dict1 = {'a': 1, 'b': 2}
dict2 = {'d': 3, 'c': 0}

print dict1
print dict2
print map(lambda a, b: a * b, dict1.values(), dict2.values())


# In[49]:

str1 = "abcd"
str2 = "thus"

map(lambda a, b: a + b, str1, str2)


# In[51]:

tuple1 = ((2, 'a'), (1, 'b'))
tuple2 = ((3, 's'), (0, 'f'))

map(lambda a, b: a + b, tuple1, tuple2)


# In[52]:

map(lambda a, b: a * b, tuple1, tuple2)


# In[57]:

set1 = set([2, 1, 4, 0])
set2 = set([4, 1, 6, 3])

print set1
print set2
print map(lambda a, b: a * b, set1, set2)


# In[59]:

set3 = set('hello')
set4 = set('cake')

print set3
print set4
print map(lambda a, b: a + b, set3, set4)


# ## ZIP function

# In[61]:

list1 = [2,  2,  3, 10,  1]
list2 = [1, -1,  5,  4, -6]

for x, y in zip(list1, list2):
    print x*y


# In[62]:

list1 = [2,  2,  3, 10,  1]
list2 = [1, -1,  5,  4, -6]

[x*y for x, y in zip(list1, list2)]


# In[63]:

list1 = [2,  2,  3, 10,  1]
list2 = [1, -1,  5,  4, -6]
list3 = [1,  0,  1,  0,  1]

a = [x*y*z for x, y, z in zip(list1, list2, list3)]
print type(a)
print a


# In[65]:

list3 = [1,  0,  1,  0,  1]
list4 = [1,  2,  3,  1, -1,  5, 6]

[x*y for x, y in zip(list3, list4)]


# In[66]:

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 0}

print dict1
print dict2
print [a + b for a, b in zip(dict1, dict2)]


# In[67]:

[a * b for a, b in zip(dict1, dict2)]


# In[68]:

dict3 = {3: 1, 1: 2}
dict4 = {'a': 1, 'b': 2}

[a + b for a, b in zip(dict3, dict4)]


# In[69]:

dict3 = {3: 1, 1: 2}
dict5 = {5: 1, 7: 2}

print dict3
print dict5
result = [a + b for a, b in zip(dict3, dict5)]
print result
print type(result)


# In[72]:

dict1 = {'a': 1, 'b': 2}
dict2 = {'d': 3, 'c': 0}

print dict1
print dict2
print [a * b for a, b in zip(dict1.values(), dict2.values())]


# In[73]:

str1 = "abcd"
str2 = "thus"

[a + b for a, b in zip(str1, str2)]


# In[74]:

tuple1 = ((2, 'a'), (1, 'b'))
tuple2 = ((3, 's'), (0, 'f'))

[a + b for a, b in zip(tuple1, tuple2)]


# In[75]:

[a * b for a, b in zip(tuple1, tuple2)]


# In[80]:

set1 = set([2, 1, 4, 0])
set2 = set([4, 1, 6, 3, 9])

print set1
print set2
print [a * b for a, b in zip(set1, set2)]


# In[77]:

set3 = set('hello')
set4 = set('cake')

print set3
print set4
print [a + b for a, b in zip(set3, set4)]


# In[ ]:



