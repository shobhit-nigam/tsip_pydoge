#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


# In[3]:


print("hi")
time.sleep(10)
print("hello")


# In[4]:


import datetime


# In[5]:


objd = datetime.datetime.now()


# In[6]:


print(objd)


# In[7]:


objd = datetime.date.today()

print(objd)


# In[8]:


objd.year


# In[10]:


lockdown = datetime.date(year=2020, month=3, day=24)


# In[11]:


print(lockdown)


# In[12]:


print(objd-lockdown)


# In[13]:


objd = datetime.datetime.now()


# In[17]:


objd.strftime("%b")


# In[18]:


import os


# In[19]:


os.getcwd()


# In[20]:


os.listdir()


# In[21]:


os.path.exists("hell.txt")


# In[23]:


os.path.exists("/Users/shobhit/Desktop/pydoge/day2")


# In[24]:


import sys


# In[25]:


sys.version


# In[26]:


print(sys.version)


# In[27]:


from datetime import date


# In[28]:


date.today()


# In[29]:


from colours import yellow, green


# In[30]:


yellow()


# In[31]:


blue()


# In[32]:


green()


# In[33]:


green()


# In[34]:


green = 20


# In[35]:


green()


# In[36]:


import colours


# In[37]:


colours.blue()


# In[38]:


colours.red()


# In[39]:


import importlib

importlib.reload(colours)


# In[40]:


colours.red()


# In[41]:


import colours


# In[43]:


colours.lista


# In[44]:


import importlib

importlib.reload(colours)


# In[45]:


colours.lista


# In[ ]:




