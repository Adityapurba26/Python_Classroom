#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
import matplotlib.pyplot as plt
import seaborn as sns
#import folium

pd.set_option('display.max_columns',500)


# In[7]:


df_datas = pd.read_csv('melb_data.csv')
print ('Data read')


# In[21]:


df_datas.head(100)


# In[32]:


df_datas['Price']


# In[74]:


df_datas['Price'].plot(kind='hist', figsize=(15, 6), bins=100)
plt.title('Distribusi Harga Rumah',size =15) # add a title to the histogram

plt.show()


# In[20]:


df_datas.describe()


# In[79]:


sns.boxplot(x=df_datas['Distance'], y=df_datas['Regionname'])
plt.title('Distribusi Jarak Region to CBD', size =15)
plt.ylabel('Region Name')
plt.show()


# In[83]:


sns.barplot(x=df_datas['Type'], y=df_datas['Price'], estimator=np.median)
plt.title('Perbandingan Nilai Median Harga Rumah', size =15)

plt.show()


# In[86]:


sns.scatterplot(x=df_datas['Price'], y=df_datas['Distance'], hue=df_datas.Type)
plt.title('Korelasi Harga Rumah dan Jarak Rumah ke CBD', size =15)


# In[91]:


df_datas['Date'] = pd.to_datetime(df_datas['Date'])
df_datas['Month'] = pd.DatetimeIndex(df_datas['Date']).month
plt.figure(figsize=(8,6))
sns.lineplot(x=df_datas.Month, y=df_datas.Price, hue=df_datas.Type)
plt.title('Tren Harga Rumah per Bulan Berdasarkan Tipe Rumah', size =15)


# In[ ]:




