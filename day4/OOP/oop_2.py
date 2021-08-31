#!/usr/bin/env python
# coding: utf-8

# In[1]:


class unix:
    def cmd(self):
        print("great command line")
    
    def secure(self):
        print("rwx for ugo gives good security")


# In[2]:


class linux(unix):
    def free(self):
        print("is a free kernel")


# In[3]:


obju = unix()
objl = linux()


# In[4]:


objl.free()


# In[5]:


objl.cmd()


# In[6]:


class unix:
    def cmd(self):
        print("great command line")
    
    def secure(self):
        print("rwx for ugo gives good security")
        
class linux(unix):
    def free(self):
        print("is a free kernel")
        
class mobileOS:
    def portable(self):
        print("portable to mini devices")
        
class android(linux, mobileOS):
    def ui(self):
        print("great GUI")


# In[7]:


obja = android()


# In[8]:


obja.portable()


# In[9]:


class unix:
    def cmd(self):
        print("great command line")
    
    def secure(self):
        print("rwx for ugo gives good security")
        
class linux(unix):
    def free(self):
        print("is a free kernel")
        
    def scalable(self):
        print("scalable to any larger or smaller device")
        
class mobileOS:
    def portable(self):
        print("portable to mini devices")
        
    def scalable(self):
        print("designed to be scalable")
        
class android(linux, mobileOS):
    def ui(self):
        print("great GUI")


# In[10]:


obja = android()


# In[11]:


obja.scalable()


# In[14]:


class unix:
    def cmd(self):
        print("great command line")
    
    def secure(self):
        print("rwx for ugo gives good security")
        
class linux(unix):
    def free(self):
        print("is a free kernel")
        
    def scalable(self):
        print("scalable to any larger or smaller device")
        
class mobileOS:
    def portable(self):
        print("portable to mini devices")
        
    def scalable(self):
        print("designed to be scalable")
        
class android(mobileOS, linux):
    def ui(self):
        print("great GUI")


# In[15]:


obja = android()


# In[16]:


obja.scalable()


# In[17]:


objl = linux()


# In[18]:


objl.scalable()


# In[20]:


class unix:
    def cmd(self):
        print("great command line")
    
    def secure(self):
        print("rwx for ugo gives good security")
        
class linux(unix):
    def free(self):
        print("is a free kernel")
        
    def scalable(self):
        print("scalable to any larger or smaller device")
        super().secure()
        


# In[21]:


objl = linux()


# In[22]:


objl.scalable()


# In[23]:


class unix:
    def cmd(self):
        print("great command line")
    
    def secure(self):
        print("rwx for ugo gives good security")
        
    def openSource(self):
        print("you get the source code, but you need to buy the OS")
        
class linux(unix):
    def free(self):
        print("is a free kernel")
        
    def scalable(self):
        print("scalable to any larger or smaller device")
    
    def openSource(self):
        print("source code available for free on net")


# In[24]:


obju = unix()
objl = linux()


# In[25]:


obju.openSource()


# In[26]:


objl.openSource()


# In[27]:


class unix:
    def cmd(self):
        print("great command line")
    
    def secure(self):
        print("rwx for ugo gives good security")
        
    def openSource(self):
        print("you get the source code, but you need to buy the OS")
        
class linux(unix):
    def free(self):
        print("is a free kernel")
        
    def scalable(self):
        print("scalable to any larger or smaller device")
    
    def openSource(self):
        print("source code available for free on net")
        super().openSource()


# In[28]:


obju = unix()
objl = linux()


# In[29]:


obju.openSource()


# In[30]:


objl.openSource()


# In[33]:


unix.cmd("hi")


# In[35]:


class unix:
    def __init__(self):
        print("init of unix")
        
    def cmd(self):
        print("great command line")
    
    def secure(self):
        print("rwx for ugo gives good security")
        
class linux(unix):
    def free(self):
        print("is a free kernel")

#    def __init__(self):
#        print("init of linux")


# In[36]:


obju = unix()


# In[37]:


objl = linux()


# In[38]:


obju.__init__()


# In[39]:


class unix:
    def __init__(self):
        print("init of unix")
        
    def cmd(self):
        print("great command line")
    
    def secure(self):
        print("rwx for ugo gives good security")
        
class linux(unix):
    def free(self):
        print("is a free kernel")

    def __init__(self):
        print("init of linux")


# In[40]:


obju = unix()


# In[41]:


objl = linux()


# In[ ]:




