#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# In[2]:


hariesh = print


# In[3]:


# print is an object
# hareish is also an object referring to the same address


# In[4]:


hariesh("hello")


# In[5]:


print(type(hariesh))


# In[6]:


print = 10


# In[7]:


type(print)


# In[8]:


print("hello")


# In[9]:


args = 10


# In[10]:


type(args)


# In[11]:


# print = __builtins__.print
# print = 100


# In[12]:


del print


# In[13]:


print("hello")


# In[14]:


print = __builtins__.print


# In[ ]:




