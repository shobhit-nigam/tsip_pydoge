#!/usr/bin/env python
# coding: utf-8

# In[1]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']

i = int(input())

print("val =", lista[i])


# In[2]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']

i = int(input())

print("val =", lista[i])


# In[4]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']
try:
    i = int(input())

    print("val =", lista[i])
except IndexError:
    print("your indes should have been within", len(lista)-1)
    print("defaulting to zero")
    i = 0
    
print("code continues")


# In[5]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']
try:
    i = int(input())

    print("val =", lista[i])
except IndexError:
    print("your indes should have been within", len(lista)-1)
    print("defaulting to zero")
    i = 0
    
print("code continues")


# In[6]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']
try:
    i = int(input())

    print("val =", lista[i])
except IndexError:
    print("your indes should have been within", len(lista)-1)
    print("defaulting to zero")
    i = 0
    
print("code continues")


# In[7]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']
try:
    i = int(input())

    print("val =", listb[i])
except IndexError:
    print("your indes should have been within", len(lista)-1)
    print("defaulting to zero")
    i = 0
    
print("code continues")


# In[8]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']
try:
    i = int(input())

    print("val =", listb[i])
except IndexError:
    print("your indes should have been within", len(lista)-1)
    print("defaulting to zero")
    i = 0
except NameError:
    print("please check again, there may be a typo")
    


# In[9]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']
try:
    i = int(input())

    print("val =", lista[i])
except IndexError:
    print("your indes should have been within", len(lista)-1)
    print("defaulting to zero")
    i = 0
except NameError:
    print("please check again, there may be a typo")
except:
    print("something went wrong")


# In[10]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']
try:
    i = int(input())

    print("val =", lista[i])
print("hello")
except IndexError:
    print("your indes should have been within", len(lista)-1)
    print("defaulting to zero")
    i = 0
except NameError:
    print("please check again, there may be a typo")
except:
    print("something went wrong")


# In[11]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']
try:
    i = int(input())

    print("val =", lista[i])
except:
    print("something went wrong")
except IndexError:
    print("your indes should have been within", len(lista)-1)
    print("defaulting to zero")
    i = 0
except NameError:
    print("please check again, there may be a typo")


# In[13]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']
try:
    i = int(input())

    print("val =", lista[i])
except IndexError:
    print("your indes should have been within", len(lista)-1)
    print("defaulting to zero")
    i = 0
except NameError:
    print("please check again, there may be a typo")
except:
    print("something went wrong")


# In[16]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']
try:
    try:
        i = int(input())

        print("val =", lista[i])
    except IndexError:
        print("your index should have been within", len(lista)-1)
        print("defaulting to zero")
        i = 0
except NameError:
    print("please check again, there may be a typo")
except:
    print("something went wrong")


# In[25]:


def funca(l):
    try:
        i = int(input())
        print("val =", la[i])
    except IndexError:
        print("your index should have been within", len(l)-1)
        print("defaulting to zero")
        i = 0


# In[26]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']
try:
    funca(lista)
except NameError:
    print("please check again, there may be a typo")


# In[27]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']

try:
    i = int(input())
    print("val =", lista[i])
    
except IndexError:
    print("your index should have been within", len(lista)-1)
    print("defaulting to zero")
    i = 0
    
except NameError:
    print("please check again, there may be a typo")
    
else:
    print("the else block executes")
    
finally:
    print("finally block executes")

print("code continues") 


# In[28]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']

try:
    i = int(input())
    print("val =", lista[i])
    
except IndexError:
    print("your index should have been within", len(lista)-1)
    print("defaulting to zero")
    i = 0
    
except NameError:
    print("please check again, there may be a typo")
    
else:
    print("the else block executes")
    
finally:
    print("finally block executes")

print("code continues") 


# In[29]:


lista = ['aa', 'gg', 'ee', 'tt', 'rr', 'dd']

try:
    i = int(input())
    print("val =", lista[i])
    
except IndexError:
    print("your index should have been within", len(lista)-1)
    print("defaulting to zero")
    i = 0
    
except NameError:
    print("please check again, there may be a typo")
    
else:
    print("the else block executes")
    
finally:
    print("finally block executes")

print("code continues") 


# In[ ]:




