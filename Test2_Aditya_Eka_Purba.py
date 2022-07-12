#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
import random

Mulai = input("Mulai: ")
Mulai = int(Mulai[:])
Selesai = input("Selesai: ")
Selesai = int(Selesai[:])
data1= np.arange(Mulai, Selesai, 1)
d = {1,  2, 3}
a =0

while (a<4):
    a=a+1
    if(a==1): print(data1)
    if(a==2):print(data1.reshape(3,9))
    if(a==3):print(data1.reshape(3,3,3))
    



# In[94]:


import random
banyak_data = input("Banyak Data: ")
banyak_data = int(banyak_data[:])
Mulai = input("Mulai: ")
Mulai = int(Mulai[:])
Selesai = input("Selesai: ")
Selesai = int(Selesai[:])
randomlist = []
for i in range(banyak_data):
    n = random.randint(Mulai,Selesai)
    randomlist.append(n)

print(randomlist)
data_array2=np.array(randomlist)
data_array2=data_array2.reshape(4,4)
print(data_array2)
data_putar=data_array2[:,::-1]
print(data_putar)


# Soal 3
# Buatlah sebuah array 2 dimensi dengan ukuran 10 x 10! Isi dari array tersebut adalah:
# • Sisi luarnya merupakan angka 4.
# • Selain sisi luar, angka yang ditampilkan adalah 0.

# In[88]:


x=np.ones((10,10))*4
x[1:-1,1:-1]=0
#x[1:9,1:9]
x


# In[ ]:




