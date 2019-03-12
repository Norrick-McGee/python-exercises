#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


nx1 = [2,2]


# In[3]:


nx2 = [2,3]


# In[5]:


nx3 = [3,3]

ny1 = [2,4]
ny2 = [4,2]
ny3 = [2,4]

ox = [[3.5,3.5],[3.5,4.5],[3.5,4.5],[4.5,4.5]]
oy = [[2,4],[4,4],[2,2],[2,4]]

rx = [[5,5],[5,6],[5,6],[6,6],[5,6]]
ry = [[2,4],[4,4],[3.125,3.125],[4,3.125],[3.125,2]]

kx = [[6.5,6.5],[6.5,7.5],[6.5,7.5]]
ky = [[2,4],[3,2],[3,4]]


# In[10]:


plt.plot(nx1,ny1, c= 'blue')
plt.plot(nx2,ny2, c = 'blue')
plt.plot(nx3,ny3, c = 'blue')

for i in range(len(ox)):
    plt.plot(ox[i],oy[i],c='blue')

for i in range(len(rx)):
    plt.plot(rx[i],ry[i], c='blue')

for i in range(len(kx)):
    plt.plot(kx[i],ky[i],c='blue')


# In[14]:


x = range(-200,200)
y = [i**2 - i + 2 for i in range(-200,200)]


# In[15]:


plt.plot(x,y)
plt.annotate('0,0', xy=(0, 0), xytext=(-50, 10000),
             arrowprops={'facecolor': 'blue'})


# In[16]:


import math 


# In[19]:


x0 = range(100)
y0 = [math.sqrt(i) for i in x]


# In[20]:


plt.plot(x0,y0)


# In[21]:


x1 = range(-200,200)
y1 = [i**3 for i in x1]
plt.plot(x1,y1)


# In[23]:


x2 = range(-100,100)
y2 = [math.tan(i) for i in x2]
plt.plot(x2,y2)


# In[25]:


x3 = range(-10,100)
y3 = [2**i for i in x3]
plt.plot(x3,y3)


# In[26]:


plt.subplot(221)
plt.plot(x0,y0)
plt.subplot(222)
plt.plot(x1,y1)
plt.subplot(223)
plt.plot(x2,y2)
plt.subplot(224)
plt.plot(x3,y3)


# In[27]:


plt.plot(x0,y0)

plt.plot(x1,y1)

plt.plot(x2,y2)

plt.plot(x3,y3)


# In[ ]:




