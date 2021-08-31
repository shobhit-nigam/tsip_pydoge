#!/usr/bin/env python
# coding: utf-8

# In[2]:


class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m
        
    def __call__(self):
        print(self.hours, "hours and", self.minutes, "minutes")


# In[3]:


class sample():
    def funca(self):
        print("in funca")


# In[4]:


objs = sample()
objt = sample()


# In[5]:


objs()


# In[6]:


print(objs)


# In[7]:


class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m
        
    def __call__(self):
        print(self.hours, "hours and", self.minutes, "minutes")
        
    def __repr__(self):
        return "hello from time"


# In[8]:


friday = time(1, 35)


# In[9]:


friday()


# In[10]:


print(friday)


# In[11]:


class sample():
    data = 100
    
    def funca(self, val):
        print("in funca changing data")
        self.data = val
        
    def funcb(self, val):
        print("in funcb changing data")
        self.data = val
        
    def funcc(self, val):
        print("in funcc changing data")
        self.data = val


# In[12]:


objx = sample()


# In[13]:


objx.data


# In[14]:


objx.funca(200)


# In[15]:


objx.data


# In[16]:


objy = sample()


# In[17]:


objy.data


# In[18]:


class sample():
    data = 100
    
    def funca(self, val):
        print("in funca changing data")
        self.data = val
        
    @classmethod
    def funcb(cls, val):
        print("in funcb changing data")
        cls.data = val
        
    def funcc(self, val):
        print("in funcc changing data")
        self.data = val


# In[19]:


objx = sample


# In[20]:


objx.data


# In[21]:


objx.funcb(200)


# In[22]:


objy = sample()


# In[23]:


objy.data


# In[24]:


class PotatotFries():
    data = 100
    
    def boil(self, val):
        print("in funca changing data")
        self.data = val
        
    def fry(cls, val):
        print("in funcb changing data")
        cls.data = val
        
    @staticmethod
    def putOnTheKitchenLight():
        print("put on the light")


# In[25]:


objp = PotatotFries()


# In[26]:


objp.putOnTheKitchenLight()


# In[ ]:




