#!/usr/bin/env python
# coding: utf-8

# In[1]:


import file_module as fm


# In[2]:


objd = fm.File("data.txt")


# In[3]:


objd.read_int_column(0)


# In[4]:


objd.read_int_column(3)


# In[5]:


objd.read_int_column(2)


# In[6]:


import pandas as pd


# In[9]:


dfa = pd.read_csv("data.txt", sep=" ", header=None)


# In[10]:


dfa


# In[11]:


dfa[0].sum()


# In[ ]:




