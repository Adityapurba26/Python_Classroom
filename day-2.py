#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x


# In[4]:


x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')


# In[5]:


ile "<ipython-input-3-6a9157bb9e54>", line 4
    print('(first suite)')
        ^
IndentationError: expected an indented block


# In[6]:


x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')


# In[7]:


hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")


# In[8]:


name = 'Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")


# In[21]:


if 'a' in 'br':
    print('foo')
#elif 1/0:
 #   print("This won't happen")
elif 1/1:
    print("This won't either")
    


# In[12]:


if 'f' in 'foo': print('1'); print('2'); print('3')


# In[26]:


x = 1

if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')


# In[25]:


x = 3
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')


# In[27]:


x = 3
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')


# In[30]:


raining = True
print("Let's go to the", 'beach' if not raining else 'class')


# In[31]:


age = 12
s = 'teen' if age < 21 else 'adult'
s


# In[33]:


'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'


# In[36]:


if ('qux' in ['qux', 'bar', 'baz']):
    print('foo')


# In[37]:


if True:
    pass

print('foo')


# In[41]:


if False:
    print('foo')
print('qux')


# In[42]:


n = 5
while n > 0:
    n -= 1
    print(n)


# In[43]:


i = 1
while i < 6:
  print(i)
  i += 1


# In[44]:


i = 1
while i < 6:
  print(i)
  i = i+1


# In[47]:


n = 7
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')


# In[48]:


n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')


# In[50]:


n= 5
while n > 0:
   n -= 1
   print(n)
   if n == 2:
       break
else:
   print('Loop done.')


# In[51]:


while True:
    print('foo')


# In[59]:


age = 8
gender = ('Mo')

if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')


# In[72]:


a = ['foo', 'bar','que']

while len(a):
    print(a.pop(0))
    
    b = ['baz', 'qux']
    
    while len(b):
        print('>', b.pop(0))


# In[61]:


n = 5
while n > 0: n -= 1; print(n)


# In[62]:


a = ['foo', 'bar', 'baz']
for i in a:
    print(i)


# In[67]:


d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

for k in d:
    print(d[k])

for k in d.values():
    print(k)

for k, v in d.items(): 
    print(k, ":", v)    


# In[64]:


for k in d:
    print(d[k])


# In[65]:


for k in d.values():
    print(k)


# In[66]:


for k, v in d.items(): 
    print(k, ":", v) 


# In[69]:


d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

for k in d:
    print(d[k])

for k in d.values():
    print(k)

for k, v in d.items(): 
    print(k, ":", v)  


# In[73]:


for i in ['foo', 'bar', 'baz', 'qux']:
    if i == 'bar':
        break
    print(i)
else:
    print('Done.')  # Will not execute


# In[74]:


temp = input("Ketikan temperatur yang ingin dikonversi, eg. 45F, 120C: ")
degree = int(temp[:-1])
i_convertion = temp[-1]

if i_convertion == "C":
    result = int(round((9 * degree) / 5 + 32))
elif i_convertion == "F":
    result = int(round((degree - 32) * 5 / 9))
else:
    print("Masukan input yang benar")

print("Temperaturnya adalah", result, "derajat")


# In[75]:


temp


# In[76]:


temp[-1]


# In[77]:


temp[:-1]


# In[78]:


while True:
    msg = input("Ketikan karakter: ").lower()
    print(msg)
    if msg == "stop":
        break


# In[ ]:




