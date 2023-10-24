#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# In[2]:


meliuz_data = pd.read_csv('C:/Users/marianasouza/Downloads/testemeliuz.csv')


# In[3]:


meliuz_data.info


# In[4]:


meliuz_data.head()


# In[9]:


meliuz_data = meliuz_data.groupby(['Estado'])['GMV'].sum().reset_index()
meliuz_data.head()


# In[12]:


import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()


# In[17]:


meliuz_data.head()


# In[18]:


meliuz_data.info


# In[ ]:


meliuz_data = meliuz_data.arange

