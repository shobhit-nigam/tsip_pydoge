#!/usr/bin/env python
# coding: utf-8

# In[1]:


def funca():
    print("plain ganesha")


# In[2]:


def funcb(gen):
    def funcc():
        gen()
        print("decorated ganesha")
    return funcc


# In[3]:


funcb(funca)


# In[4]:


funcx = funcb(funca)      #  funcx = funcc


# In[5]:


funca()


# In[6]:


funcx()


# In[7]:


def sample():
    print("in sample")


# In[8]:


x = sample()
y = sample 


# In[ ]:


# x()   same as None


# In[9]:


print(x)


# In[10]:


y()


# In[11]:


def funca():
    print("plain ganesha")
    
def funcb(gen):
    def funcc():
        gen()
        print("decorated ganesha")
    return funcc

funcx = funcb(funca)


# In[12]:


funcx()


# In[13]:


def funca():
    print("plain ganesha")
    
def funcb(gen):
    def funcc():
        gen()
        print("decorated ganesha")
    return funcc

funca()
print("-------")
funca = funcb(funca)       #funca = funcc
funca()


# In[14]:


def funcb(gen):
    def funcc():
        gen()
        print("decorated ganesha")
    return funcc

def funca():
    print("plain ganesha")

funca()
print("-------")
funca = funcb(funca)       #funca = funcc
funca()


# In[15]:


def funcb(gen):
    def funcc():
        gen()
        print("decorated ganesha")
    return funcc

def funca():
    print("plain ganesha")

funca = funcb(funca)       #funca = funcc


# In[16]:


def funcb(gen):
    def funcc():
        gen()
        print("decorated ganesha")
    return funcc

@funcb
def funca():
    print("plain ganesha")


# In[17]:


funca()


# In[18]:


def hashtag(gen):
    def inner():
        print("########")
        gen()
        print("########")
    return inner
    
@hashtag    
def display():
    print("hello there")


# In[19]:


display()


# In[20]:


@hashtag
def funca():
    print("plain ganesha")


# In[21]:


funca()


# In[24]:


def hashtag(gen):
    def inner(*args):
        print("########")
        gen(*args)
        print("########")
    return inner
    
@hashtag    
def display(stra):
    print(stra)


# In[26]:


display("hello there")


# In[ ]:


# not to be executed
def hashtag(display):
    def inner():
        print("########")
        display()
        print("########")
    return inner
    
@hashtag    
def display():
    print("hello there")


# In[ ]:


# not to be executed
def hashtag(display):
    def inner():
        print("########")
        # content of original display function
        print("########")
    return inner
    
@hashtag    
def display():
    print("hello there")


# In[27]:


def hashtag(gen):
    def inner(*args):
        print("########")
        gen(*args)
        print("########")
    return inner
    
@hashtag    
def display(stra):
    print(stra)


# In[28]:


display("happy september")


# In[29]:


def hashtag(gen):
    def inner(*args):
        print("########")
        gen(*args)
        print("########")
    return inner


# In[30]:


def star(gen):
    def inner(*args):
        print("********")
        gen(*args)
        print("********")
    return inner


# In[31]:


@hashtag
def display(stra):
    print(stra)


# In[32]:


display("hi")


# In[33]:


def hashtag(gen):
    def inner(*args):
        print("########")
        gen(*args)
        print("########")
    return inner

def star(gen):
    def inner(*args):
        print("********")
        gen(*args)
        print("********")
    return inner


# In[34]:


@star
def display(stra):
    print(stra)
    
display("hi")


# In[35]:


def star(gen):
    def inner(*args):
        print("********")
        gen(*args)
        print("********")
    return inner

def hashtag(gen):
    def inner(*args):
        print("########")
        gen(*args)
        print("########")
    return inner

@star
@hashtag
def display(stra):
    print(stra)


# In[36]:


display("hi")


# In[ ]:


******
######
hi
######
******


# In[ ]:




