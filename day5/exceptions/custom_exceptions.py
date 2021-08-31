#!/usr/bin/env python
# coding: utf-8

# In[1]:


class AppException(Exception):
    # some code
    pass


# In[2]:


class SmallValueError(AppException):
    """value is too small"""
    
class LargeValueError(AppException):
    """value is too large"""


# In[4]:


num = 25


# In[5]:


while True:
    try:
        val = int(input("enter the number:\n"))
        if val < num:
            raise SmallValueError
        elif val > num:
            raise LargeValueError
        else:
            print("you guessed it right")
            break
            
    except SmallValueError:
        print(SmallValueError.__doc__)
        print("try again")
    except LargeValueError:
        print(LargeValueError.__doc__)
        print("try again")


# In[ ]:




