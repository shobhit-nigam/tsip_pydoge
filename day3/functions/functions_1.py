#!/usr/bin/env python
# coding: utf-8

# ### learning functions

# In[2]:


def funca():
    print("hello")
    print("guten tag")


# In[3]:


funca()


# In[4]:


def funca(la, lb):
    print("la =", la)
    print("lb =", lb)


# In[5]:


listx = [5, 8, 10]


# In[6]:


listx[0]


# In[7]:


def funca(la, lb):
    print("la =", la)
    print("lb =", lb)


# In[8]:


funca(100, 200)


# In[9]:


funca(100)


# In[10]:


funca(100, 200, 300)


# In[11]:


funca()


# In[12]:


def funca(la, lb=200, lc=100):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)


# In[13]:


funca(11, 22, 33)


# In[14]:


funca(11, 22)


# In[15]:


funca()


# In[16]:


def funca(la=300, lb, lc=100):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)


# In[18]:


def funca(la=300, lb=200, lc=100):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc)


# In[19]:


funca(lb=22)


# In[20]:


funca(lb=22, la=11, lc=33)


# In[21]:


print("hey")
print("hello")
print("how are you?")


# In[22]:


print("hey", end=', ')
print("hello", end = ', ')
print("how are you?")


# In[23]:


help(print)


# In[24]:


def funca():
    print("hello")
    print("guten tag")


# In[25]:


x = funca()


# In[26]:


print(x)


# In[27]:


def funca(la, lb):
    # code
    return la+lb


# In[28]:


x = funca(100, 200)


# In[29]:


print(x)


# In[30]:


def funca(la, lb):
    # code
    return la+lb, la*lb, la-lb


# In[31]:


x, y, z = funca(100, 20)


# In[32]:


x


# In[33]:


y


# In[34]:


z


# In[35]:


def funca(la, lb, *lc):
    print("la =", la)
    print("lb =", lb)
    print("lc =", lc) 


# In[36]:


funca(100, 200, 300, 400, 500, 600)


# In[37]:


def funca(la, lb, *args):
    print("la =", la)
    print("lb =", lb)
    print("args =", args) 


# In[38]:


funca("hi", "ho", "hello", [3, 6, 7], 3.4)


# In[39]:


def funca(la, lb, *args, **kwargs):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)
    print("kwargs =", kwargs)


# In[40]:


funca(100, 200)


# In[41]:


def funca(la, lb, *args, **kwargs):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)
    print("kwargs =", kwargs)


# In[42]:


funca(100, 200, 300, 400, india='delhi', norway='oslo')


# In[44]:


def funca(la, lb, **kwargs):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)
    print("kwargs =", kwargs)


# In[45]:


funca(100, 200, 300, 400, india='delhi', norway='oslo')


# In[46]:


def funca(la, lb, *args):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)
    #print("kwargs =", kwargs)


# In[47]:


funca(100, 200, 300, 400, india='delhi', norway='oslo')


# In[49]:


def funca(la, lb, *args):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)
    print("args =", list(args))


# In[50]:


funca(100, 200, [4, 5, 6])


# In[52]:


def funca(la, lb, *args):
    print("la =", la)
    print("lb =", lb)
    print("args =", args)
    print("kwargs =", kwargs)


# In[53]:


funca(100, lb=200, 300, 400, india='delhi', norway='oslo')


# In[54]:


x, y, z = 100, 200, 300


# In[55]:


y


# In[56]:


x = 100, 200, 300


# In[57]:


x


# In[58]:


type(x)


# In[59]:


def funca():
    return 11, "hello", 20


# In[60]:


x, y, z = funca()


# In[61]:


y


# In[62]:


z


# In[63]:


x, y = funca()


# In[64]:


x = funca()


# In[65]:


x


# In[66]:


type(x)


# In[ ]:




