#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[3]:


stra = input()
pat = "^h..l$"

res = re.match(pat, stra)

if res:
    print("match found")
else:
    print("match not found")


# In[7]:


stra = input()
pat = "^h..l$"

res = re.match(pat, stra)

if res:
    print("match found")
else:
    print("match not found")


# In[8]:


stra = input()
pat = "\^h\.\.l\$"

res = re.match(pat, stra)

if res:
    print("match found")
else:
    print("match not found")


# In[10]:


stra = input()
pat = "[a-z][aeiou][ ][0-9]"

res = re.match(pat, stra)

if res:
    print("match found")
else:
    print("match not found")


# In[11]:


stra = input()
pat = "[a-z][aeiou][ ][0-9]"

res = re.findall(pat, stra)

if res:
    print("match found")
else:
    print("match not found")


# In[12]:


with open("data.txt", "r") as fa:
    stra = fa.read()
    
pat = "\d"

res = re.findall(pat, stra)

print(res)


# In[13]:


with open("data.txt", "r") as fa:
    stra = fa.read()
    
pat = "\d+"

res = re.findall(pat, stra)

print(res)


# In[14]:


with open("data.txt", "r") as fa:
    stra = fa.read()
    
pat = "\d{3,4}"

res = re.findall(pat, stra)

print(res)


# In[15]:


with open("avengers.txt", "r") as fa:
    stra = fa.read()
    
pat = "-"

res = re.split(pat, stra)

print(res)


# In[16]:


with open("avengers.txt", "r") as fa:
    stra = fa.read()
    
pat = "-"

res = re.split(pat, stra, 2)

print(res)


# In[18]:


with open("data.txt", "r") as fa:
    stra = fa.read()
    
pat = "\d+"
rep = "##"

res = re.sub(pat, rep, stra)

print(res)


# In[19]:


with open("data.txt", "r") as fa:
    stra = fa.read()
    
pat = "\s"
rep = "_"

res = re.sub(pat, rep, stra)

print(res)


# In[20]:


with open("data.txt", "r") as fa:
    stra = fa.read()
    
pat = "\s+"
rep = "_"

res = re.sub(pat, rep, stra)

print(res)


# In[21]:


with open("data.txt", "r") as fa:
    stra = fa.read()
    
pat = "\s+"
rep = "_"

res = re.sub(pat, rep, stra, 4)

print(res)


# In[23]:


with open("data.txt", "r") as fa:
    stra = fa.read()
    
pat = "\d+"
rep = "##"

res = re.subn(pat, rep, stra)

print(res)


# In[25]:


stra = "45 6789, 2 6789, 98 129"
    
pat = "(\d{2} \d{4})"

res = re.findall(pat, stra)

print(res)


# In[26]:


stra = "Hello says hello to hell and HELL"
    
pat = "hell"

res = re.findall(pat, stra)

print(res)


# In[27]:


stra = "Hello says hello to hell and HELL"
    
pat = "hell"

res = re.findall(pat, stra, re.IGNORECASE)

print(res)


# In[ ]:




