#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Bank:
    cid = 0
    name = "john doe"
    opn_bal = 0
    cur_bal = opn_bal


# In[2]:


obja = Bank()
objb = Bank()


# In[3]:


obja.cid


# In[4]:


obja.cid = 34008


# In[5]:


obja.cid


# In[6]:


objb.cid


# In[7]:


class Bank:
    cid = 0
    name = "john doe"
    opn_bal = 0
    cur_bal = opn_bal
    
    def update(self, i, n, o, c):
        self.cid = c
        self.name = n
        self.opn_bal = o
        self.cur_bal = c
        
    def display(self):
        print("welcome", self.name)
        print("your account balance is", self.cur_bal)


# In[8]:


obja = Bank()
objb = Bank()


# In[9]:


obja.update(34800, "batman", 600, 600)

# Bank.update(obja, 34800, "batman", 600, 600)


# In[10]:


obja.display()


# In[11]:


objb.display()


# In[12]:


class Bank:
    cid = 0
    name = "john doe"
    opn_bal = 0
    cur_bal = opn_bal
    
    def update(self, i, n, o, c):
        self.cid = c
        self.name = n
        self.opn_bal = o
        self.cur_bal = c
        
    def display(self):
        print("welcome", self.name)
        print("your account balance is", self.cur_bal)
        
    def funcx():
        print("hello there")


# In[13]:


obja = Bank()
objb = Bank()


# In[14]:


obja.funcx()


# Bank.funcx(obja)


# In[15]:


Bank.funcx()


# In[17]:


class Bank:
    cid = 0
    name = "john doe"
    opn_bal = 0
    cur_bal = opn_bal
    
    def update(self, i, n, o, c):
        self.cid = c
        self.name = n
        self.opn_bal = o
        self.cur_bal = c
        
    def display(self):
        print("welcome", self.name)
        print("your account balance is", self.cur_bal)
        
    def funcx(ttt):
        print("hello there")
        
        
obja = Bank()
objb = Bank()


# In[18]:


obja.funcx()


# In[19]:


class Bank:
    cid = 0
    name = "john doe"
    opn_bal = 0
    cur_bal = opn_bal
    
    def update(self, i, n, o, c):
        self.cid = c
        self.name = n
        self.opn_bal = o
        self.cur_bal = c
        
    def display(self):
        print("welcome", self.name)
        print("your account balance is", self.cur_bal)
        
    def funcx(ttt):
        print("hello there")
        ttt.extra = 200
        
        
obja = Bank()
objb = Bank()


# In[20]:


obja.funcx()


# In[21]:


obja.extra


# In[22]:


objb.extra


# In[ ]:


class Bank:
    cid = 0
    name = "john doe"
    opn_bal = 0
    cur_bal = opn_bal
    
    def __init__(self, i, n, o, c):
        self.cid = c
        self.name = n
        self.opn_bal = o
        self.cur_bal = c
        
    def display(self):
        print("welcome", self.name)
        print("your account balance is", self.cur_bal)
        
        
obja = Bank()
objb = Bank()


# In[23]:


class sample:
    def __init__(self):
        print("hello")


# In[24]:


objs = sample()


# In[28]:


class Bank:
    
    def __init__(self, i, n, ob):
        self.cid = i
        self.name = n
        self.opn_bal = ob
        self.cur_bal = self.opn_bal
        
    def display(self):
        print("welcome", self.name)
        print("your account balance is", self.cur_bal)
        
        
obja = Bank(46800, "batman", 600)
objb = Bank(46802, "shaktiman", 800)


# In[29]:


obja.display()


# In[30]:


objb.display()


# In[31]:


class Bank:
    
    def __init__(self, i, n, ob):
        self.cid = i
        self.name = n
        self.opn_bal = ob
        self.cur_bal = self.opn_bal
        
    def display(self):
        print("welcome", self.name)
        print("your account balance is", self.cur_bal)
        
    def deposit(self, amt):
        self.cur_bal = self.cur_bal + amt
        print("deposit successfully")
        
    def withdraw(self, amt):
        if self.cur_bal < amt:
            print("do not have sufficient balance")
        else:
            print("withdrawn successfully")
            self.cur_bal = self.cur_bal - amt


# In[32]:


obja = Bank(46800, "batman", 600)
objb = Bank(46802, "shaktiman", 800)


# In[33]:


objb.withdraw(1000)


# In[34]:


objb.deposit(300)


# In[35]:


objb.withdraw(1000)


# In[36]:


objb.display()


# In[37]:


sa = "hello"

sa.upper()


# In[41]:


class sample:
    data = 11
    _datb = 22
    __datc = 33
    __datd__ = 44
    
    def display(self):
        print("data =", self.data)
        print("_datb =", self._datb)
        print("__datc =", self.__datc)
        print("__datd__ =", self.__datd__)


# In[42]:


objs = sample()


# In[43]:


print("data =", objs.data)
print("_datb =", objs._datb)
print("__datc =", objs.__datc)
print("__datd__ =", objs.__datd__)


# In[44]:


print("__datd__ =", objs.__datd__)


# In[45]:


objs.display()


# In[48]:


class sample:
    data = 11
    _datb = 22
    __datc = 33
    __datd__ = 44
    
    def display(self):
        print("data =", self.data)
        print("_datb =", self._datb)
        print("__datc =", self.__datc)
        print("__datd__ =", self.__datd__)
        self.__func()
        
    def __func(self):
        print("hey")


# In[49]:


objs = sample()


# In[50]:


objs.__func()


# In[51]:


objs.display()


# In[52]:


class Bank:
    
    def __init__(self, i, n, ob):
        self.cid = i
        self.name = n
        self.opn_bal = ob
        self.cur_bal = self.opn_bal
        
    def display(self):
        print("welcome", self.name)
        print("your account balance is", self.cur_bal)
        
    def deposit(self, amt):
        self.cur_bal = self.cur_bal + amt
        print("deposit successfully")
        
    def withdraw(self, amt):
        if self.cur_bal < amt:
            print("do not have sufficient balance")
        else:
            print("withdrawn successfully")
            self.cur_bal = self.cur_bal - amt


# In[53]:


obja = Bank(46800, "batman", 600)


# In[54]:


# called init, values update
# job of init is done, wont be called again automatically for this onject


# In[55]:


obja.display()


# In[56]:


obja.deposit(1000)


# In[57]:


obja.display()


# In[ ]:




