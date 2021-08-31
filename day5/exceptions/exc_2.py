#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    val = 1/0
except ZeroDivisionError:
    print("don't divide by zero")


# In[2]:


try:
    val = 1/0
except :
    print("something went wrong")


# In[3]:


import traceback


# In[8]:


try:
    val = 1/0
except:
    print("something went wrong")
    with open("error.txt", "w") as fa:
        data = traceback.print_exc()
        fa.write(data)


# In[9]:


try:
    val = 1/0
except:
    print("something went wrong")
    traceback.print_exc()


# In[10]:


import sys


# In[12]:


try:
    val = 1/0
except:
    print("something went wrong")
    print(sys.stderr())


# In[15]:


try:
    val = 1/0
except Exception as obje:
    print("something went wrong")
    print(obje)


# In[16]:


try:
    val = 1/0
except Exception as obje:
    print("exception is : ", type(obje).__name__)
    print("message is : ", obje)


# In[17]:


try:
    val = 1/0
except Exception as obje:
    print("exception is : ", type(obje).__name__)
    print("message is : ", obje)
    print("line number is ", obje.__traceback__.tb_lineno)


# In[ ]:




