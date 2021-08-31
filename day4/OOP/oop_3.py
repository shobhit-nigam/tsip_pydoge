#!/usr/bin/env python
# coding: utf-8

# In[1]:


stra = "hello"
strb = "hi"


# In[2]:


stra + strb


# In[3]:


strb*3 + stra


# In[4]:


lista = [10, 30, 40]
listb = [60, 20, 70]


# In[5]:


lista + listb


# In[6]:


lista - listb


# In[7]:


seta = {10, 30, 40}
setb = {60, 20, 70}


# In[8]:


seta + setb


# In[9]:


seta - setb


# In[10]:


# operator overloading


# In[12]:


class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m
        
    def display(self):
        print(self.hours, "hours and", self.minutes, "minutes")


# In[14]:


friday = time(1, 35)
saturday = time(1, 45)

total = time()


# In[15]:


friday.display()


# In[16]:


saturday.display()


# In[17]:


total.display()


# In[18]:


total = friday + saturday    # 3hrs 20 mnts
                             # 2 hrs 80 mnts


# In[19]:


class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m
        
    def display(self):
        print(self.hours, "hours and", self.minutes, "minutes")
        
    def __add__(self, other):
        temp = time()
        
        total_mnts = self.hours*60 + self.minutes + other.hours*60 + other.minutes
        temp.hours = total_mnts//60     #200//60 = 3
        temp.minutes = total_mnts%60    #200%60 = 20
        return temp


# In[20]:


friday = time(1, 35)
saturday = time(1, 45)

total = time()


# In[21]:


total = friday + saturday


# In[22]:


total.display()


# In[23]:


friday < saturday


# In[26]:


class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m
        
    def display(self):
        print(self.hours, "hours and", self.minutes, "minutes")
        
    def __add__(self, other):
        temp = time()
        
        total_mnts = self.hours*60 + self.minutes + other.hours*60 + other.minutes
        temp.hours = total_mnts//60     #200//60 = 3
        temp.minutes = total_mnts%60    #200%60 = 20
        return temp
    
    def __lt__(self, other):
        min1 = self.hours*60 + self.minutes
        min2 = other.hours*60 + other.minutes
        return min1 < min2
    
    def __gt__(self, other):
        min1 = self.hours*60 + self.minutes
        min2 = other.hours*60 + other.minutes
        return min1 > min2   


# In[27]:


friday = time(1, 35)
saturday = time(1, 45)

total = time()


# In[28]:


friday < saturday


# In[29]:


total > saturday


# In[30]:


10 < 20 > 30


# In[31]:


(10 < 20) and (20 > 30)


# In[32]:


friday = time(1, 35)
saturday = time(1, 45)
sunday = time(1, 50)

total = time()


# In[33]:


friday < saturday < sunday


# In[34]:


total = friday + saturday + sunday


# In[35]:


total.display()


# In[ ]:




