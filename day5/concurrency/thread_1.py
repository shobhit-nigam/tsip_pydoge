#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


# In[2]:


def taskA():
    for i in range(3, 0, -1):
        print(i, "seconds left for task A")
        time.sleep(1)


# In[4]:


taskA()


# In[5]:


def taskA():
    for i in range(3, 0, -1):
        print(i, "seconds left for task A")
        time.sleep(1)
        
def taskB():
    for i in range(9, 0, -1):
        print(i, "seconds left for task B")
        time.sleep(1)


# In[7]:


taskA()
taskB()
for i in range(6, 0, -1):
    print(i, "seconds left for task main")
    time.sleep(1)


# In[8]:


import threading


# In[10]:


ta = threading.Thread(target=taskA)
tb = threading.Thread(target=taskB)

ta.start()
tb.start()

for i in range(6, 0, -1):
    print(i, "seconds left for task main")
    time.sleep(1)


# In[11]:


def taskA(num):
    for i in range(num, 0, -1):
        print(i, "seconds left for task A")
        time.sleep(1)
        
def taskB(num):
    for i in range(num, 0, -1):
        print(i, "seconds left for task B")
        time.sleep(1)


# In[13]:


ta = threading.Thread(target=taskA, args=(3,))
tb = threading.Thread(target=taskB, args=(9,))

ta.start()
tb.start()

for i in range(6, 0, -1):
    print(i, "seconds left for task main")
    time.sleep(1)


# In[14]:


def taskA(num):
    fa = open("data.txt", "a")
    fa.write("hi\n")
    time.sleep(1)
    fa.write("hello\n")
    time.sleep(1)
    fa.write("one more line\n")
    time.sleep(1)
    fa.write("last line\n")
    fa.close()
        
def taskB(num):
    fa = open("data.txt", "r")
    stra = fa.read()
    print("length of data read is ", len(stra))
    print("read data is -->\n", stra)


# In[15]:


ta = threading.Thread(target=taskA, args=(3,))
tb = threading.Thread(target=taskB, args=(9,))

ta.start()
tb.start()


# In[16]:


loc = threading.Lock()

def taskA():
    global loc
    print("task A requests for lock")
    loc.acquire()
    print("task A gets the lock")
    fa = open("data.txt", "a")
    fa.write("hi\n")
    time.sleep(1)
    fa.write("hello\n")
    time.sleep(1)
    fa.write("one more line\n")
    time.sleep(1)
    fa.write("last line\n")
    fa.close()
    print("task A will release the lock")
    loc.release()    
        
def taskB():
    global loc
    time.sleep(0.5)
    print("task B requests for lock")
    loc.acquire()
    print("task B gets the lock")
    fa = open("data.txt", "r")
    stra = fa.read()
    print("length of data read is ", len(stra))
    print("read data is -->\n", stra)
    print("task B will release the lock")
    loc.release()    
    
ta = threading.Thread(target=taskA)
tb = threading.Thread(target=taskB)

ta.start()
tb.start()


# In[ ]:




