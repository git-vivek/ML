#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[6]:


df=pd.read_csv("http://52.66.247.33/com.csv")
df


# In[15]:


slices=[df['Salary']]
labels=df['Department']


# In[17]:


plt.pie(slices)


# In[28]:


y=df['Salary'].values
type(y)


# In[29]:


y


# In[30]:


min(y)


# In[31]:


max(y)


# In[ ]:




