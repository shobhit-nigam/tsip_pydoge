#!/usr/bin/env python
# coding: utf-8

# In[1]:


fa = open("books.txt", "r")


# In[2]:


stra = fa.read(4)


# In[3]:


print(stra)


# In[4]:


strb = fa.read(4)
print(strb)


# In[5]:


strb = fa.read(6)
print(strb)


# In[6]:


fa.close()


# In[7]:


fa = open("books.txt", "r")
stra = fa.read()

print(stra)


# In[8]:


print(len(stra))


# In[9]:


fa.close()


# In[10]:


fa = open("books.txt", "r")
stra = fa.readline()

print(stra)


# In[11]:


stra = fa.readline()

print(stra)


# In[13]:


fa.tell()


# In[14]:


fa.seek(9)


# In[16]:


fa.read(4)


# In[17]:


fa.closed


# In[18]:


fa.close()


# In[19]:


fa.closed


# In[20]:


with open("books.txt") as fa:
    lista = fa.readlines()


# In[21]:


fa.closed


# In[22]:


lista


# In[23]:


with open("books.txt") as fa:
    stra = fa.read()


# In[24]:


stra.split()


# In[25]:


stra.splitlines()


# In[26]:


fb = open("new_books.txt", "w")


# In[27]:


fb.write("selected books are:\n")


# In[28]:


fb.close()


# In[29]:


lista


# In[30]:


fb = open("new_books.txt", "a")


# In[33]:


for line in lista:
    if "the" in line:
        fb.write(line)


# In[34]:


fb.close()


# In[35]:


with open("data.txt", "r") as fa:
    stra = fa.read()


# In[36]:


lista = stra.splitlines()


# In[37]:


lista


# In[38]:


for line in lista:
    print(line)


# In[39]:


for line in lista:
    temp = line.split()
    print(temp)


# In[40]:


for line in lista:
    temp = line.split()
    print(temp[1])


# In[41]:


col = []

for line in lista:
    temp = line.split()
    col.append(temp[1])


# In[42]:


col


# In[43]:


col = []

for line in lista:
    col.append(line.split()[1])


# In[44]:


col


# In[45]:


with open("data.txt", "r") as fa:
    stra = fa.read()

lista = stra.splitlines()

col = []

for line in lista:
    col.append(line.split()[1])


# In[46]:


import os

os.path.exists("data.txt")


# In[55]:


def read_column(file, col):
    if os.path.exists(file):
        with open(file, "r") as fa:
            stra = fa.read()

        lista = stra.splitlines()

        listc = []

        for line in lista:
            listc.append(line.split()[col])
        return listc
            
    else:
        print("file not found, returning empt list")
        return []


# In[48]:


read_column("data.txt", 1)


# In[49]:


x = read_column("data.txt", 1)


# In[50]:


print(x)


# In[56]:


x = read_column("dataxxx.txt", 1)


# In[57]:


print(x)


# In[58]:


x = read_column("data.txt", 0)


# In[59]:


print(x)


# In[72]:


class File:
    def __init__(self, f):
        self.file = f
        if not os.path.exists(self.file):
            print("file not found, defaulting to None")
            print("please do not use class methods")

    def read_column(self, col):
        with open(self.file, "r") as fa: 
            stra = fa.read()

        lista = stra.splitlines()

        listc = []

        for line in lista:
            listc.append(line.split()[col])
        return listc
    
    def read_int_column(self, col):
        with open(self.file, "r") as fa: 
            stra = fa.read()
        
        lista = stra.splitlines()

        listc = []

        for line in lista:
            temp = line.split()
            if type(temp[col]) is str:
                print("type of column non integer, written empty list")
                return []
            listc.append(int(temp[col]))
        return listc


# In[66]:


objf = File("data.txt")


# In[67]:


num = objf.read_int_column(0)


# In[68]:


num


# In[69]:


sum(num)


# In[73]:


objf = File("data.txt")
num = objf.read_int_column(1)


# In[74]:


num


# In[ ]:




