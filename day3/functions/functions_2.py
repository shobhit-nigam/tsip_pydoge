#!/usr/bin/env python
# coding: utf-8

# In[1]:


ga = 100


# In[2]:


def funca():
    la = 100
    print("in func ga =", ga)
    print("in func la =", la)


# In[3]:


funca()


# In[4]:


print(ga)


# In[5]:


def funca():
    la = 100
    ga = 200
    print("in func ga =", ga)
    print("in func la =", la)


# In[6]:


print(ga)


# In[7]:


funca()


# In[8]:


print(ga)


# In[9]:


ga = 100


# In[11]:


def funca():
    global ga
    la = 100
    ga = 200
    print("in func ga =", ga)
    print("in func la =", la)


# In[12]:


print(ga)


# In[13]:


funca()


# In[14]:


print(ga)


# In[16]:


def outer():
    print("outer part")
    def inner():
        print("inner part")
    print("outer again")
    return


# In[17]:


outer()


# In[18]:


inner()


# In[19]:


def outer():
    print("outer part")
    def inner():
        print("inner part")
    print("outer again")
    inner()
    return


# In[20]:


outer()


# In[ ]:




